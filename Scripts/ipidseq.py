
#!/usr/bin/env python

#---------------------------------------------------------------------#
# A simple script to check pattern in IPID generation on a target     #
#                   Bharath(github.com/yamakira)                      #
#       More info: http://nmap.org/book/idlescan.html                 #
#---------------------------------------------------------------------#


from __future__ import print_function          # importing print as a function feature(just a best practice)
from scapy.all import IP, TCP, sr1             # Importing only the necessary classes from scapy
import sys
import logging                                 #Surpress scapy warnings by logging them
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

def help_text():
    print("\nUsage:\n python ipidseq.py target_ip\n")
    sys.exit()

def extract_ipids(target_ip):
    print("\nTarget => {}".format(target_ip))
    ip   =   IP(dst=target_ip)                               # Define IP layer
    tcp  =   TCP(dport = 4444, flags = 'S')                  # Define TCP layer
    syn_packet = ip/tcp                                      # Stacking IP/TCP to create a SYN packet

    ipids = []
    print("\n[+] Sending packets to the target")
    for i in xrange(5):                                       # Sending 5 SYN packets, Saving the IPID's of reply into a list
        response = sr1(syn_packet, verbose=0)
        ipids.append(response.id)
    # print(ipids)
    return ipids

def check_pattern(ipids):
    print("[+] Analyzing the IPID pattern")

    if all(v == 0 for v in ipids):                           # Checking if all IPID's are zeros
        return "all zeros"
    elif all(x==y for x, y in zip(ipids, ipids[1:])):        # Checking if all IPID's are constant
        return "constant"
    elif all(y-1==x for x, y in zip(ipids, ipids[1:])):      # Checking if all IPID's are incremental
        return "incremental"
    else:                                                    # If all else fails then it's a random pattern
        return "randomized"

if __name__ == '__main__':
   
    if len(sys.argv) < 2:
        help_text()
    target_ip = sys.argv[1]
    ipids = extract_ipids(target_ip)
    ipid_pattern = check_pattern(ipids)
    print("[*] IPID generation pattern on {} is {}\n".format(target_ip, ipid_pattern))
    
