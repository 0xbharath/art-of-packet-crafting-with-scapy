# Scapy Intro

## Trivia

- Scapy is packet crafting, manipulating and analysis suite
- Python interpreter disguised as a Domain Specific Language
- Created by Philippe Biondi

## Overview

- Helps to forge packets, send & recieve packets, R&W pcaps, alter packets.
- Easy & faster packet desgining.
- Dozens of in-built functions to automate various network utilities/attacks..

## What’s different about Scapy?

You might be wondering that there are dozens of packet crafting tools, network scanners so why should we use Scapy?

Scapy is not just another packet crafting tool, it comes with a lot of new concepts and paradigms.

Scapy is not desgined as a simple but rather a framework upon which you can build other custom tools.

### Absolute freedom over packets

A lot of packet crafting tools does not have a way to set certain fields in packets (limitations of `sock_raw`) i.e. the kernel is still in control of certain fields and will calculate those fields on behalf of the tool (checksums, IHL)

Most packet crating tools let’s you fiddle with only limited fields/protocols, it is impossible to stack unrelated protocol headers into a single packet.

#### Try to find a tool that can do

- An ICMP echo request with some given padding data
- An IP protocol scan with the More Fragments flag
- Some ARP cache poisoning with a VLAN hopping attack
- A traceroute with an applicative payload (DNS, ISAKMP, etc.)

Scapy tries to overcome those problems. It enables you to build exactly the packets you want. Even if you think stacking a 802.1q layer on top of TCP makes no sense, it may have some for somebody else working on some product. 

Scapy has a flexible model that tries to avoid any arbitrary limits. You’re free to put any value you want in any field you want, and stack them like you want. You’re an adult after all.

#### Decode, Not Interpret

    Tool that interprets - “The port 80 is filtered”
    Tool that decodes - “I have recieved ICMP type 3; code 13 from port 80”

- Having a tool that interprets is convenient but it is not the the best approach all the time.
- Tools interpret results based on the tool authors logic but every network is unique, one interpretation does not fit all the senarios.
- Interpreting results can help users that don’t know what a port scan is but it can also make more harm than good, as it injects bias into the results. A more knowledgable penetration tester woud want to see all the information and make interpretation himself. Unfortunately many tools discard most information that is needed.
- Networks are complex especially with the advent of firewalls, cloud infrastructure etc so each pen test is unique and you have to pay attention to even the minute details rather than relying on some tools interpretation blindly.

#### Fast packet desgining & power of Python

Other tools stick to the program-that-you-run-from-a-shell paradigm. The result is an awful syntax to describe a packet. For these tools, the solution adopted uses a higher but less powerful description, in the form of scenarios imagined by the tool’s author. As an example, only the IP address must be given to a port scanner to trigger the port scanning scenario. Even if the scenario is tweaked a bit, you still are stuck to a port scan.

Scapy is not a simple shell command program; Scapy runs inside Python interpreter, provides you the whole language when dealing with packets but you don’t need to master Python to use Scapy though.

Scapy’s paradigm is to propose a Domain Specific Language (DSL) that enables a powerful and fast description of any kind of packet. Using the Python syntax and a Python interpreter as the DSL syntax and interpreter has many advantages: there is no need to write a separate interpreter, users don’t need to learn yet another language and they benefit from a complete, concise and very powerful language.

#### Probe Once, Interpret Many Times.

Network recon/Network mapping is not simply scanning ports, it’s far more complex and involves techniques like TTL analysis, understanding IP based trust relationships in the network etc.

Unlike many tools, which discard all the information which they deem irrelavent, Scapy gives all the information, i.e. all the stimuli sent and all the responses received. Scapy gives the complete raw data, which can be used many times during analysis. You’ll have all the Power of Python to dig through the data and perform analysis.

## Scapy Limitations

- Scapy is not designed for fast throughput. It’s written in Python which comes with many layers of abstraction.
- Scapy does not go easy on memory (Each packet is a class instance). Not a right choice for analysing large packet captures.

