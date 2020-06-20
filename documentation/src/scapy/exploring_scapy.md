# Exploring Scapy

## List of protocols supported

```
>>> ls()
ARP        : ARP
DNS        : DNS
Dot11      : 802.11
TCP        : TCP
Ether      : Ethernet
[...]
```

## Dissecting protocols


```
>>> ls(IP)
version    : BitField             = (4)
ihl        : BitField             = (None)
tos        : XByteField           = (0)
len        : ShortField           = (None)
id         : ShortField           = (1)
flags      : FlagsField           = (0)
frag       : BitField             = (0)
ttl        : ByteField            = (64)
proto      : ByteEnumField        = (0)
chksum     : XShortField          = (None)
src        : Emph                 = (None)
dst        : Emph                 = ('127.0.0.1')
options    : PacketListField      = ([])
```

## List of all the scapy commands

```
>>> lsc()
rdpcap     : Read a pcap file and return a packet 
send       : Send packets at layer 3
sendp      : Send packets at layer 2
sendpfast  : Send packets at layer 2 using tcpreplay
[...]
```

## Getting help on any function


```
>>> help(arpcachepoison)

Help on function arpcachepoison in module scapy.layers.l2:

arpcachepoison(target, victim, interval=60)
    Poison target's cache with (your MAC,victim's IP) couple
    arpcachepoison(target, victim, [interval=60]) -> None

[...]
```

## Change Scapy configuration

```
>>> conf
iface      = 'eth3'
iface6     = 'wlan0'
wepkey     = ''
sniff_promisc = 1
[...]
```

> Assembling and sending raw packets requires UID 0 (root access). Use `sudo` to become root.
