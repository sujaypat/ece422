#!/usr/bin/python2.7
import dpkt
import sys
import socket

def ip_to_str(address):
    """
    transform a int ip address to a human readable ip address (ipv4)
    """
    return socket.inet_ntoa(address)


def mac_addr(mac_string):
    """
    transform a int mac address to a human readable mac address (EUI-48)
    """
    return ':'.join('%02x' % ord(b) for b in mac_string)



if (len(sys.argv) < 2):
    print "error: need argument"
    sys.exit(1)

filename = sys.argv[1]

srcpkt = {}
dstpkt = {}

with open(filename, 'rb') as f:
    pcap = dpkt.pcap.Reader(f)
    assert (pcap.datalink() == dpkt.pcap.DLT_EN10MB), "the datalink is not ethernet, aborting"

    for ts, buf in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            if eth.type == dpkt.ethernet.ETH_TYPE_IP:
                ip = eth.data
                if ip.p == dpkt.ip.IP_PROTO_TCP:
                    tcp = ip.data
                    if (tcp.flags & dpkt.tcp.TH_SYN != 0) and (tcp.flags & dpkt.tcp.TH_ACK == 0):
                        # This is a SYN send message
                        srcpkt[ip_to_str(ip.src)] = srcpkt.get(ip_to_str(ip.src), 0) + 1
                    if (tcp.flags & dpkt.tcp.TH_ACK != 0) and (tcp.flags & dpkt.tcp.TH_SYN != 0):
                        # This is an SYN-ACK recieve message
                        dstpkt[ip_to_str(ip.dst)] = dstpkt.get(ip_to_str(ip.dst), 0) + 1
        except:
            pass
# Done counting, now do analysis
outData = []
for k, v in srcpkt.iteritems():
    # Check if k exists in dst, if it doesn't then we automatically have 3x
    if k not in dstpkt:
        if k not in outData:
            outData.append(k)
    else:
        # K does exist, so get the count and check if 3x
        dstCount = dstpkt[k]
        if v > (dstCount * 3):
            if k not in outData:
                outData.append(k)
for ip in outData:
    print(ip)
