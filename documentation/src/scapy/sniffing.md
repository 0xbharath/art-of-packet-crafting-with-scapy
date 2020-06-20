# Sniffing

## Sniff()

- Scapy's in-built `sniff()` function helps us capture all traffic
- `sniff()` has `count`, `filter`, `iface`, `lfilter`, `prn`, `timeout` options
- Can apply BPF filters (Same as TCPDUMP)

```
>>> sniff(count=4, iface='eth3')
<Sniffed: TCP:0 UDP:0 ICMP:0 Other:4>
```

## Sniffing with Scapy

Scapy sniffer is not designed to be super fast so it can miss packets sometimes. Always use use tcpdump when you can, which is more simpler and efficient.

We can add filtering to capture only packets that are interesting to us. Use standard tcpdump/libpcap syntax:

```
>>> pkts = sniff(count=1,filter="tcp and host 64.233.167.99 and port 80")
```

```
>>> sniff(filter='arp', count=5, iface='vboxnet0')
<Sniffed: TCP:0 UDP:0 ICMP:0 Other:5>
>>>
>>> _.summary()
Ether / ARP who has 192.168.56.101 says 192.168.56.1
Ether / ARP who has 192.168.56.101 says 192.168.56.1
Ether / ARP who has 192.168.56.101 says 192.168.56.1
Ether / ARP who has 192.168.56.101 says 192.168.56.1
Ether / ARP who has 192.168.56.101 says 192.168.56.1
```

Simple traffic analyzer like tcpdump.

```
>>> pkts = sniff(count=5,filter="host 64.233.167.99",prn=lambda x:x.summary())
Ether / IP / TCP 192.168.1.100:33168 > 64.233.167.99:www S
Ether / IP / TCP 64.233.167.99:www > 192.168.1.100:33168 SA
Ether / IP / TCP 192.168.1.100:33168 > 64.233.167.99:www A
Ether / IP / TCP 192.168.1.100:33168 > 64.233.167.99:www PA / Raw
Ether / IP / TCP 64.233.167.99:www > 192.168.1.100:33168 A
```

Scapy can sniff packets offline from pcap files.

```
>>> pkts = sniff(offline='http_google.pcap')
>>> 
>>> pkts.nsummary()
0000 Ether / IP / TCP 172.16.16.128:1606 > 74.125.95.104:http S
0001 Ether / IP / TCP 74.125.95.104:http > 172.16.16.128:1606 SA
0002 Ether / IP / TCP 172.16.16.128:1606 > 74.125.95.104:http A
0003 Ether / IP / TCP 172.16.16.128:1606 > 74.125.95.104:http PA / Raw
0004 Ether / IP / TCP 74.125.95.104:http > 172.16.16.128:1606 A / Padding
```

```
>>> sniff(offline='http_google.pcap', lfilter = lambda s: s[TCP].flags == 18, prn = lambda x: x[IP].dst)
172.16.16.128
<Sniffed: TCP:1 UDP:0 ICMP:0 Other:0>
```
