# PCAP Analysis


- Scapy has pretty handy functions for handling PCAP files
- Although there are dedicated tools like dpkt, pcapy etc to deal with packet captures (using Python), Scapy is still a go-to tool for PCAP analysis because of it’s dense methods that aid you in number of packet analysis operations
- Although Scapy is all powerful, it’s takes a lot of memory when reading packets so analysing larger packet captures will take toll on your system memory

## PCAP operations

> **Memory matters!**
> 
> Scapy looks at each packet as a class which takes toll on the system memory, so it is not a right choice for analysing large PCAPs
> 
> When investigating large PCAP’s(several Giga Bytes) use light-weight tools like Tshark for initial analysis, when investigation boils down to smaller set of packets, use Scapy.

### Reading PCAP

You can read a PCAP file in Scapy using rdpcap function.

```
>>> rdpcap('port_knock_seq.pcap')
<port_knock_seq.pcap: TCP:6 UDP:0 ICMP:0 Other:0>
```

```
>>> pkts = sniff(offline="temp.cap")
```

### Writing pcap

You can write a set of packets into a PCAP file using wrpcap function.

```
>>> wrpcap("attack.pcap",packets)
```

### Simple tcp-replay tool

- You can write a very simple tcp-replay tools in one line of scapy
This piece of code send packets in a PCAP over the network, very handy in some forensic analysis situations

```
>>> sendp(rdpcap("/tmp/pcapfile")) # tcpreplay
...........
Sent 11 packets.
```

## Exercise time - packet hunting

Please solve Exercise 5- packet hunting (Misc exercises)

Please solve Exercise 6 (Misc exercises)
