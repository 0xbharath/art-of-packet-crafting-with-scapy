#---------------------------------------------------------------------#
#           A script to discover live hosts on a network              #
#                   Bharath(github.com/yamakira)                      #
#                                                                     #
#---------------------------------------------------------------------#


from __future__ import print_function          # importing print as a function feature(just a best practice)
from scapy.all import IP, TCP, sr1, sr         # Importing only the necessary classes from scapy
import sys
import logging                                 #Surpress scapy warnings by logging them
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)



def help_text():
    print("\nUsage:\n python hd_tcp_syn.py network_range\n")
    sys.exit()
        
def host_discovery(network_range):
    ans,unans=sr( IP(dst=network_range)/TCP(dport=80,flags="S"),verbose=0,timeout=1)
    ans.summary( lambda(s,r) : r.sprintf("\n %IP.src% is alive\n") )
    #for packet in ans:
     #   print (packet.summary)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help_text()
    network_range = sys.argv[1]
    host_discovery(network_range)
