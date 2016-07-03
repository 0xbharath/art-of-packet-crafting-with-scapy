#!/usr/bin/env python
"""
    Purpose: Scan for hosts which are suitable to perform an idle scan.
    More info: http://nmap.org/book/idlescan.html
"""
import sys
import getopt
from scapy import *

def analyzeIPID(lipid):
    """
        Analyze the list of ipids to determine if it's incremental
        Shameless port from:
        https://metasploit.com/trac/browser/framework3/trunk/modules/auxiliary/scanner/ip/ipidseq.rb
    """
    allzeros = True
    allsame = True
    mul256 = True
    inc = True
    diffs = []
    i = 1
    if conf.verb > 0:
        print "[*] Analyzing %s" % lipid
        print "[*] Length  %s" % len(lipid)
    if len(lipid) < 2:
        return "Unknown"
    while i < len(lipid):
        p = lipid[i - 1]
        c = lipid[i]
        if p != 0 or c != 0:
            allzeros = False

        if p <= c:
            diffs.append(c - p)
        else:
            diffs.append(c - p + 65536)

        if len(lipid) > 2 and diffs[i - 1] > 20000:
            return "Randomized"

        i+=1

    if allzeros:
        return "All zeros"

    for diff in diffs:
        if diff > 1000 and ((diff % 256) != 0 or ((diff  % 256) == 0 and diff >= 25600)):
            return "Random positive increment"

        if diff != 0:
            allsame = False
            
        if diff > 5120 or (diff % 256) !=0:
            mul256 = False
            
        if diff >= 10:
            inc = False

    if allsame:
        return "Constant"

    if mul256:
        return "Broken little-endian incremental"

    if inc:
        return "Incemental!"
    
    return "unknown"

def txthelp():
    print "[*] DiabloHorn http://diablohorn.wordpress.com"
    print "[*] " + sys.argv[0] + " [-v] -t <target> [-w] <waittime>"
    sys.exit(0)

if __name__ == "__main__":
    
    if len(sys.argv) <= 1:
        txthelp()
    print 
    rawdata = dict()
    conf.verb=0
    pcktIPID=IP()
    try:
        opts, args = getopt.getopt(sys.argv[1:],"vht:w:",["verbose","help","target=","waittime="])
    except getopt.GetoptError, err:
        print str(err)
        txthelp()
        sys.exit(0)
    
    for o,a in opts:
        if o in ("-h","--help"):
            txthelp()
        elif o in ("-v","--verbose"):
            conf.verb = 2
        elif o in ("-t","--target"):
            pcktIPID.dst=a 
        elif o in ("-w","--wait"):
            to = float(a)
        else:
            print "Unknown option"
            sys.exit(1)
    if conf.verb > 0:
        print "[*] verbose set to: " + str(conf.verb)
        print "[*] target set to: " + str(pcktIPID.dst)
    print "[*] Starting scan"
   
    """
        Send the packets
    """ 
    for i in range(0,5):
        res,unans=sr(pcktIPID/TCP(dport=[80,443]),timeout=to)
        """
        Receive answers
        """
        for s,r in res:
            ipsrc = r[IP].src
            ipsrcid = r[IP].id
            if ipsrc in rawdata:
                rawdata[ipsrc].append(ipsrcid)
            else:
                rawdata[ipsrc] = [ipsrcid]
    """
        Analyze and print results
    """
    for k,v in rawdata.iteritems():
        rawdata[k] = analyzeIPID(v)
        print "[*] %s = %s" % (k,rawdata[k])
