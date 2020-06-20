# Misc Exercises

## Exercise 1
### Network sweeping

- Write a script to perform network sweeping i.e. given a IP address range, find all the machines that are alive
- Use any of the host discovery techniques that have been discussed but ARP tends to be neat and faster on local networks

```
$ sudo python hd_tcp_syn.py 192.168.56.99-110
 192.168.56.102 is alive
 192.168.56.103 is alive
 192.168.56.107 is alive
```

## Exercise 2
### Port scanning

- Write a script to perform port scanning i.e. given an IP address, find status of ports on the machine(atleast find any open ports under 1024)
- Use any of the port scanning techniques that have been discussed

```
$ sudo python tcp_syn_scan.py 192.168.56.107
'ftp_data    RA'
'21          RA
'ssh         SA'
'telnet      RA'
'24          RA'
```

## Exercise 3
### IP ID pattern finder

- Write a script that takes a target IP and checks for patterns in the IP ID generation
- Basic checks include: if the IP IDs generated are: all zeros, are all constant, are all randomized or if they are incremental.

Example:

```
$ sudo python ipidseq.py 192.168.56.101

Target => 192.168.56.101

[+] Sending packets to the target
[+] Analyzing the IPID pattern
[*] IPID generation pattern on scanme.nmap.org is randomized
```

#### Python/Scapy tips:

- Use `sr1` for sending packet and recieving first response
- Python has in-built function `all()` that comes handy when comparing elements in list. Looking at below examples, think about how you can use it to do other comparisions.

```
>>> lis = [0,0,0,0]
>>> all(v == 0 for v in lis)       # Checking if all elements in list are zero
True 
```

```
>>> lis = [1,4,6,9,22,65,98,354]
>>> 
>>> all(x<y for x, y in zip(lis, lis[1:]))  # Checking if the elements are in increasing order
True
```

## Exercise 4

### IP ID scanner

- Your might have found a potential ‘zombie’ from the previous scan
- Write a script that takes a `zombie_ip`, `victim_ip`. `victim_port` Performs a ipid scan (Details in the notes)

For more detailed discussion: Idle scan

Example:

```
$ sudo python ipidscanner.py 192.168.56.102 192.168.56.103 4444

[+] Sending syn-ack to zombie
[+] Recording initial IPID

[+] Sending spoofed syn to victim

[+] Sending syn-ack to zombie
[+] Recording final IPID

[*] Initial IPID of zombie: 14
[*] Final IPID of zombie: 16

The port 4444 on 192.168.56.103 is open
```

#### Python/Scapy tips:

- Use `sr1()` or `send()` to send packets
- Send `sr1()` and other packet sending functions take an extra argument verbose, set `verbose=0` to avoid scapy output

#### Solution

idle scan consists of three steps that are repeated for each port:

- Probe the zombie’s IPID and record it. (Send a syn-ack to zombie, record ipid in response)
- Forge a SYN packet with zombie IP as source and victim IP, victim port as destination.
- Probe the zombie’s IP ID again. The target port state is then determined by comparing this new IP ID with the one recorded in step 1.
- At this point, if the zombie’s IPID increased by one that the zombie hasn’t sent out any packets, except for its reply to the attacker’s probe. THis is an indication that the target port might be closed on victim.
- If the zombie’s IPID increased by two, it means the zombie sent out a packet between the two probes. This is an indication that the target port is open on the victim.
- If zombie IPIP increases by more than two, it usually indicates a bad zombie host. It might not have predictable IPID numbers, or might be engaged in communication unrelated to the idle scan.

## Exercise 5
### Packet hunting

- You are given a PCAP file - [boston2016](https://github.com/0xbharath/art-of-packet-crafting-with-scapy/blob/master/pcaps/Boston2016.pcap), this PCAP is suspected to be having covert channel activity. (someone trying to transfer data in a packet using unsual methods)
- Your task is to analyze this packet capture and find out the hidden data.

#### Python/Scapy tips:

- `rdpcap` to read a pcap
- `packet[protocol]` to extract protocol specific content
- `packet[protocol].field` to extract field
- `format(text,'04x')` is how you format into proper hex format in Python.
- Use `join` method to join elements of a list `".".join([192, 168, 99, 24]) –> 192.168.99.24`

#### Solution hints I:

This is not a packet analysis or CTF class so I’ll describe the solution in plain terms here, try to codify it using Scapy.

- The covert activity might be happening through UDP checksums.

#### Solution hints II:

Spoilers ahead

- The data is being exfiltrated by one party through checksums.
- To be specific, UDP checksums in DNS queries is where the data is. - Extract the checksums from DNS queries.
- You have to read the checksums in “0x:(hex) format first. format(text,'0x')
- Decode the hex checksums into ascii and that’s the exfiltrated data.

## Exercise 6
### Packet analysis

Given a pcap file, find all the unique hosts in that pcap file and try and determine their OS.

```
$ python list_scan.py evidence.pcap

List of all the hosts and possible OS
-------------------------------------
192.168.56.0   - Linux
45.65.29.124   - Windows
198.56.101.2   - Linux
```

## Exercise 7
### Dummy network scanner

A client wants you to do a security audit on their network. Client provided you with a network range to scan and set of IP addresses to exclude from scan.

Before you run an actual network scan, write a script that lists all the IP addresses that falls under scan(similar to Nmap list scan). (Network range provided by client minus IP addresses to be excluded)

Example:

```
$ python list_scan.py --range 192.168.56.1/30 --exclude 192.168.56.2
Range   => IPSet(['192.168.56.1/30'])
Exclude => IPSet(['192.168.56.2/32'])
192.168.56.0
192.168.56.1
192.168.56.3
```

Hints:

- `netaddr` library deals with Layer 3 addressing
- `netaddr.IPSet` has a remove method to remove elements


## Exercise 8
### Local network interface enumeration.

- Use a python library to list all the interfaces on your machine, find as much as you can(interface labels, addressing etc).
- When you print the output, make sure it’s easily readable.

Hints:

- `netifaces` helps enumerate local interfaces
- `string .format` method and pprint helps you print stuff beautifully in Python
