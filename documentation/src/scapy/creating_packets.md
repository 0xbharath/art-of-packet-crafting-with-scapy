# Creating Packets

## Creating a packet

- Scapy packet creation is consistent with layered approach in networking
- The basic building block of a packet is a layer, and a whole packet is built by stack- ing layers on top of one another
- In scapy, packets are constructed by defining packet headers for each protocol at different layers of TCP/IP and then stacking these layers in order
- To create a DNS query, you need to build Ether(sometimes optional), IP,UDP headers and stack them using / operator

## Creating packet in one line

```
>>> packet = Ether()/IP(dst='8.8.8.8')/TCP(dport=53,flags='S')

    A full-fledged DNS request packet

>>> dns_query = IP(dst="8.8.8.8")/UDP(dport=53)/DNS(rd=1,qd=DNSQR(qname="null.co.in"))
>>> 
>>> dns_query
<IP  frag=0 proto=udp dst=8.8.8.8 |<UDP  sport=domain dport=domain |<DNS  rd=1 qd=<DNSQR  qname='null.co.in' |> |>>>
```

## Create each layer individually and stack them using ‘/’ operator

```
>>> l2 = Ether()
>>> l3 = IP(dst='8.8.8.8/30')
>>> l4 = TCP(dport=53, flags = 'S')
>>> packet = l2/l3/l4
```

## Scapy IP notations

Scapy accepts plain dotted-quad IP notation, CIDR notation, hostnames.

```
>>> packet = IP(dst = '8.8.8.8')
>>> 
>>> packet = IP(dst = 'scanme.nmap.org')
>>> 
>>> packet = IP(dst = '8.8.8.8/30')
# Above line created 4 packets in one statements implicitly.
# Using list comprehensions to view all the packets.
>>> [a for a in packet]
[<IP  dst=8.8.8.8 |>, <IP  dst=8.8.8.9 |>, <IP  dst=8.8.8.10 |>, <IP  dst=8.8.8.11 |>]

>>> packet = IP(dst = 'egadz.metasploit.com/30')
```

## Creating set of packets

We can create a set of packets implicitly using Scapy.

```
pkts = IP(ttl=[1,3,5,(7,10)])/TCP()
```

For inspecting set of packets you can use list comprehensions

```
[pkt for pkt in pkts]

>>> [pkt for pkt in pkts]
[<IP  frag=0 ttl=1 proto=tcp |<TCP  |>>, <IP  frag=0 ttl=3 proto=tcp |<TCP  |>>, <IP  frag=0 ttl=5 proto=tcp |<TCP  |>>, <IP  frag=0 ttl=7 proto=tcp |<TCP  |>>, <IP  frag=0 ttl=8 proto=tcp |<TCP  |>>, <IP  frag=0 ttl=9 proto=tcp |<TCP  |>>, <IP  frag=0 ttl=10 proto=tcp |<TCP  |>>]
>>>
>>> from pprint import pprint
>>> pprint([pkt for pkt in pkts])
[<IP  frag=0 ttl=1 proto=tcp |<TCP  |>>,
 <IP  frag=0 ttl=3 proto=tcp |<TCP  |>>,
 <IP  frag=0 ttl=5 proto=tcp |<TCP  |>>,
 <IP  frag=0 ttl=7 proto=tcp |<TCP  |>>,
 <IP  frag=0 ttl=8 proto=tcp |<TCP  |>>,
 <IP  frag=0 ttl=9 proto=tcp |<TCP  |>>,
 <IP  frag=0 ttl=10 proto=tcp |<TCP  |>>]
```

```
>>> IP(dst="192.168.*.1-10")/TCP(dport=(0,1024))
```

