#!/usr/bin/env python

#---------------------------------------------------------------------#
# A script to perform idle scan i.e. scanning victim through zombie   #
#                   Bharath(github.com/yamakira)                      #
#           More info: http://nmap.org/book/idlescan.html             #
#---------------------------------------------------------------------#


from __future__ import print_function          # importing print as a function feature(just a best practice)
from scapy.all import IP, TCP, sr1, send       # Importing only the necessary classes from scapy
import sys
import logging                                 #Surpress scapy warnings by logging them
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)


def help_text():
    print("\nUsage:\n python ipidscanner.py zombie_ip victim_ip victim_port\n")
    sys.exit()


def ipid_scanner(zombie_ip, victim_ip, victim_port):
   
    synack_to_zombie = IP(dst=zombie_ip)/TCP(dport=3322, flags='SA')     # Creating SYNACK packet. attacker -->  zombie
    zombie_response = sr1(synack_to_zombie, verbose=0)                   # Sending SYNACK.         attacker -->  zombie
    print("\n[+] Sending syn-ack to zombie")
    initial_ipid = zombie_response.id                                    # Recording the initial IPID value of zombie
    print("\n[+] Recording initial IPID")
    
                                                         #Creating spoofed SYN packet. Zombie(spoofed) --> victim    
    syn_to_victim = IP(src = zombie_ip, dst=victim_ip)/TCP(dport=int(victim_port), flags='S')
    send(syn_to_victim, verbose=0)                                       # Sending SYN. Zombie(spoofed) --> victim
    print("\n[+] Sending spoofed syn to victim")    
    
    zombie_response = sr1(synack_to_zombie, verbose=0)                   # Sending SYNACK. Attacker --> Zombie
    print("\n[+] Sending syn-ack to zombie")
    final_ipid = zombie_response.id                                      # Recording the final IPID value of zombie
    print("\n[+] Recording final IPID\n")

    print("[*] Initial IPID of zombie: {}\n[*] Final IPID of zombie: {}".format(initial_ipid,final_ipid))
    return initial_ipid, final_ipid    
    
def check_port_status(initial_ipid, final_ipid):

    if initial_ipid == final_ipid-1:
        print("\n[*] The port {} on {} is closed | filtered\n".format(victim_port, victim_ip))
    elif initial_ipid == final_ipid-2:
        print("\nThe port {} on {} is open\n".format(victim_port,victim_ip))
    else:
        print("\n{} is a Bad zombie, try another!!\n".format(victim_ip))
    
if __name__ == '__main__':

    if len(sys.argv) < 4:
        help_text()
    zombie_ip = sys.argv[1]                         # Assigning zombie IP, victim IP and victim port values
    victim_ip = sys.argv[2]
    victim_port = sys.argv[3]
    i, f = ipid_scanner(zombie_ip, victim_ip, victim_port)    
    check_port_status(i,f)
