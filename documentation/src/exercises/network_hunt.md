# Network Hunt

Let’s go Network hunting!

## Challenge Overview

Terminal-based game in which you will use common network attack vectors and penetration testing methods to analyze and compromise a virtual network.

Involves Network Security challenges designed to educate users on packet manipulation and common network attacks.

The whole challenge happens over sort of a software defined network(SDN).

Originally created by James Sullivan (MIT License), modified by us for the workshop.

## Network Hunt

- The network hunt is a simple Software Defined Network
- The network is completely defined by handcrafted packets using Scapy/Python which simulates a typical network setup.

## The Goal

There is an FTP server some where on the network containing a document:

- Locate the FTP server
- Connect to the service &
- Retrieve the secret file!

## Concepts

- Bash terminal-fu
- Packet capture and manipulation in Scapy
- Packet analysis in Wireshark
- Router modes of operation
- Network topography, gateways
- Basic telnet/nc commands

## Hints

- You may need to find a way to see all of the traffic on the network
- Other clients on the network might give you useful clues, if you can coerce them
- The target will most likely be isolated from the immediate local network, and will have some preferred clients


## TASKS

### TASK 1

- Run the script & find the details about the new interface(ipconfig, route).

### TASK 2

Understand the network.

   - Is there any traffic on the network?
   - Are there devices connected to the network? Perform a network sweep?

### TASK 3

How to gain access to traffic beyond a switch?

Think about exploiting the way layer 2 switches operate?

Scapy tips:

- `RandMAC()` - Generates random MAC addresses.
- `RandIP()` - Generates random IP addresses.

### TASK 4

Were you able to gain access to traffic beyond switch? If so, is there something interesting about the traffic? Is there some strange pattern in the traffic?
    
Hint: Port knocking. (Reference docs has more details on what port knocking is)

### TASK 5

Did you manage to get access to some service on some machine? try some standard commands for that service to get more hints.

### TASK 6

The target is not in the same sub-network and also accepts connections from only specific machines.How do you compromise the machine?

Hint: ARP MitM

### TASK 7

Retrive the payload using standard FTP commands.
