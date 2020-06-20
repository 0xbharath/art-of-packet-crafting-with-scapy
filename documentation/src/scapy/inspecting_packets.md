# Inspecting Packets

Get detailed description of the packet along with datatypes

```
>>> packet = IP()/TCP()
>>> ls(packet)
version    : BitField             = 4               (4)
ihl        : BitField             = None            (None)
tos        : XByteField           = 0               (0)
len        : ShortField           = None            (None)
id         : ShortField           = 1               (1)
flags      : FlagsField           = 0               (0)
frag       : BitField             = 0               (0)
ttl        : ByteField            = 64              (64)
proto      : ByteEnumField        = 6               (0)
chksum     : XShortField          = None            (None)
src        : Emph                 = '127.0.0.1'     (None)
dst        : Emph                 = '127.0.0.1'     ('127.0.0.1')
options    : PacketListField      = []              ([])
[-- snipped --]
```

## show()

Displays detailed headers but does not assemble the packet

```
>>> packet.show()
###[ IP ]###
  version= 4
  ihl= None
  len= None
  [...]
  proto= hopopt
  chksum= None
  src= 192.168.1.100
  dst= Net('8.8.8.8/30')
```

## show2

Similar to `show()` but also assembles the packet and calculates the checksums and IHL.

```
>>> packet.show2()
###[ IP ]###
  version= 4L
  ihl= 5L
  [...]
  ttl= 64
  proto= hopopt
  chksum= 0xa8cd
  src= 192.168.1.100
  dst= 8.8.8.8
```

## Get only user supplied values

```
>>> b.hide_defaults( )
```

## summary

Display short & interesting summary of a packet.

```
>>> packet.summary()
'Ether / IP / TCP 192.168.1.100:ftp_data > 8.8.8.8:domain S'
```

## nsummary

Display short & interesting summary of a packet with numbering.

```
>>> pkts[0].nsummary()
0000 IP / TCP 192.168.1.103:ftp_data > 198.58.109.32:tcpmux S ==> IP / TCP 198.58.109.32:tcpmux > 192.168.1.103:ftp_data SA
0001 IP / TCP 192.168.1.103:ftp_data > 198.58.109.32:3128 S ==> IP / TCP 198.58.109.32:3128 > 192.168.1.103:ftp_data SA
0002 IP / TCP 192.168.1.103:ftp_data > 198.58.109.32:http_alt S ==> IP / TCP 198.58.109.32:http_alt > 192.168.1.103:ftp_data SA
```

`summary()` and `nsummary()` supports advanced features such as:

- Filtering packets by individual header field values using `lfilter` argument
- Printing only necessary parts of packet using `prn` argument


```
>>> egadz[0].nsummary(lfilter= lambda (s,r): r[TCP].sport == 3128 or r[TCP].sport==1)
0000 IP / TCP 192.168.1.103:ftp_data > 198.58.109.32:tcpmux S ==> IP / TCP 198.58.109.32:tcpmux > 192.168.1.103:ftp_data SA
0001 IP / TCP 192.168.1.103:ftp_data > 198.58.109.32:3128 S ==> IP / TCP 198.58.109.32:3128 > 192.168.1.103:ftp_data SA
```


```
>>> egadz[0].nsummary(lfilter= lambda (s,r): r[TCP].sport == 3128, prn = lambda (s,r): s.dst)
0001 198.58.109.32
```

## Interacting with fields inside packet

### To access a specific field: [packet_name].[field]

```
>>> packet.dst
'd8:55:a3:fe:80:78'
```

### For fields that are not unique [packet_name][proto].[field]

```
>>> packet[Ether].dst
'd8:55:a3:fe:80:78'
>>> packet[IP].dst
'8.8.8.8'
```

### `.payload` ignores the lowest layer and parses the next layer.

```
>>> packet.payload.flags
0
>>> packet.payload.payload.flags
2
```

## Checking for presence of layer in packet

### `haslayer` method

checks for presence of a layer in a packet

```
>>> if packet.haslayer(TCP):
...     print packet[TCP].flags
... 
2
>>>
```

### Using an `in` construct

```
>>> pkt = IP()/TCP()/DNS()
>>>
>>> DNS in pkt
True
```

## Scapy’s `sprintf`

- `sprintf()` method is one of the very powerful features of `scapy.sprintf` comes very handy while writing custom tools
- `sprintf` fills a format string with values from the packet, much like it `sprintf` from C Library, except here it fills the format string with field values from packets.

```
sprintf format     -    % [ [ fmt ] [ r ] , ] [ layer [ :nb ] . ] field %
```

```
Example     -    %-5sr, TCP.flags%
```

```
>>> packet.sprintf("Ethernet source is %Ether.src% and IP proto is %IP.proto%")
'Ethernet source is 00:00:00:00:00:00 and IP proto is icmp'

>>> a=Ether( )/Dot1Q(vlan=42)/IP(dst="192.168.0.1")/TCP(flags="RA")
>>>
>>> a.sprintf("%dst% %IP.dst% vlan=%Dot1Q.vlan%")
'00:00:d4:ae:3f:71 192.168.0.1 vlan=42'
>>>
>>>a.sprintf(" %TCP.flags% | %5s,TCP.flags% | %#05xr,TCP.flags%")
' RA | RA    | 0x014'

```

```
>>> res.nsummary(lfilter = lambda (s,r): r[TCP].flags & 2)
0008 IP / TCP 192.168.5.20:ftp-data > 192.168.5.22:discard S ==>
IP / TCP 192.168.5.22:discard > 192.168.5.20:ftp-data SA / Padding
```

```
>>> res.nsummary(lfilter = lambda (s,r): r[TCP].flags & 2, prn = lambda (s,r):s.dport)
0008 9
0012 13
0021 22
0024 25
```

## Packet handlers

In the below example, we used lambda function to write a packet handler that can handle TCP packets but this function does not work with anything other than TCP packets.

```
>>> f=lambda x:x.sprintf("%IP.dst%:%TCP.dport%")
>>> f(IP(dst='8.8.8.8')/TCP())
'8.8.8.8:www'
>>> f(IP('8.8.8.8')/UDP())
'8.8.8.8:??'
```

Having a function that can work with various packets can be helpful in practical senarios, we can achieve this using conditional substrings in sprintf(). A conditional substring is only triggered when a layer is present in the packet or else it is ignored. You can also use ! for checking the absence of a layer.

```
Conditional substring format     -    { [ ! ] layer : substring }
```

```
>>> f=lambda x: x.sprintf("=> {IP:ip=%IP.dst% {UDP:dport=%UDP.dport%}\
... {TCP:%TCP.dport%/%TCP.flags%}{ICMP:type=%r,ICMP.type%}}\
... {!IP:not an IP packet}")
>>> 
>>> f(IP()/TCP())
'=> ip=127.0.0.1 http/S'
>>> 
>>> f(IP()/UDP())
'=> ip=127.0.0.1 dport=domain'
>>> 
>>> f(IP()/ICMP())
'=> ip=127.0.0.1 type=8'
>>>
>>> f(Ether()/ARP())
'=> not an IP packet'
```

## Python’s format method

- Python string format method generates beautiful output but unlike sprintf it prints literal values.

```
>>> "Ether source is: {} & IP proto is: {}".format(packet.src, packet.proto)
'Ether source is: 00:00:00:00:00:00 & IP proto is: 1'
```