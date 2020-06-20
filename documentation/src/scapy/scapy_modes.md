# Scapy Modes

## Scapy - Interactive mode

- Just run scapy command in your terminal. You will be presented with an interactive interpreter.
- It’s just a Python interpreter disguised as a Domain Specific Language i.e. python interpreter loaded with scapy classes and objects
- Scapy in interactive mode suits well for one-liners

```
$ scapy
Welcome to Scapy (2.3.1)
>>> 
>>> 
>>> sniff()
^C<Sniffed: TCP:281 UDP:0 ICMP:0 Other:2>
>>>
```

## Importing Scapy as a module

Scapy can be imported as an externam module into any python scipt.

```
>>> from scapy.all import *
>>> dir()
['AES', 'AH', 'ARC2', 'ARC4', 'ARP', 'ARPHDR_ETHER', 'ARPHDR_LOOPBACK', 'ARPHDR_METRICOM'   [...snipped...]
>>> IP
<class 'scapy.layers.inet.IP'>
>>> TCP
<class 'scapy.layers.inet.TCP'>
```