from pcapfile import savefile
from pcapfile.protocols.linklayer import ethernet
from pcapfile.protocols.network import ip
import binascii

testcap = open('01.pcap', 'rb')
capfile = savefile.load_savefile(testcap, verbose=True)

eth_frame = ethernet.Ethernet(capfile.packets[0].raw())
print eth_frame

ip_packet = ip.IP(binascii.unhexlify(eth_frame.payload))
print ip_packet
