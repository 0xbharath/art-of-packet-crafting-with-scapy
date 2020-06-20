# The Art of Packet Crafting with Scapy

Online notes for this workshop is available at - https://scapy.disruptivelabs.in/

Virtual machine for the workshop is available at - https://archive.org/details/pysos_class3_labs_32bit.7z

**Documentation is being tracked as part of `documentation` branch. If you want to contribute to the documentation then make changes to `documentation` branch and raise a PR.**

## Prerequisites
- Little bit of programming experience in some language, not necessarily Python is preferable. (enough to know what's a "variable" or "if statement" etc)
- Knowledge of Linux command-line skills is necessary but we'll pick it up in the workshop. (Usage of commands like cd, ls, grep, less...)
- Must have knowledge of basic networking concepts(enough to know what's an IP address, port number, OSI Model etc).

## Overview
- This is an intense workshop on crafting packets using Python and Scapy.
- We'll explore Scapy and craft packets using the framework.
- We'll leverage Scapy as a framework to build custom network tools/utilities.

## Objective
- The objective is to understand network programming abstractions, use raw sockets & Scapy to craft packets, improvise in network reconnaissance phase.
- We will work on practical network reconnaissance techniques like host discovery, service discovery, Remote OS finger printing, promiscuous node detection.
- We'll learn how to launch Layer 2 attacks and detection techniques for these attacks.
- We'll leverage Scapy to build custom tools/utilities such as sniffers, pcap analyser, Wi-Fi scanners and simple honeypots.

## Environment & Labs

### Mysterious boxes
A network with bunch of machines is provided where audience task is to find out as much as they can about the network, machines and security policies using Scapy.
One of the machines on this network is a pre-packaged VM with all the necessary packages for attacking installed that we'll use as an attacker box and the other machines act as victims.

### Network Hunting - CTF
A mini-CTF on a Software Defined Network. The audience task is to crack a set of challenges, circumvent security measures, subvert systems, perform network attacks to find and obtain the flag.
