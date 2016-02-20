#!/usr/bin/env python
# Port Scanner v<2.0>
# Hades.y2k (github.com/Hadesy2k/)
# 20/Feb/2016
# GNU GPL <v2.0>

from socket import *
import threading
import sys
import time

openPort = []

def scan(host, port):
	s = socket(AF_INET, SOCK_STREAM)
	s.settimeout(0.5)
	try:
		sent = s.connect((host, port))
		if port not in openPort:
			openPort.append(port)
			print "[+] Port %s open" % port
	except:
		s.close()

def help():
	print """-h --help  View help
Usage   :  python <filename>.py IP <PortRange>
           leaving blank in PortRange will scan from 1 to 1024
Example :  python scan.py localhost 1-443
www.github.com/Hadesy2k/portscan"""

class mainApp(threading.Thread):
	def __init__(self, address, port):
		threading.Thread.__init__(self)
		self.address = address
		self.port = port
		self.run()

	def run(self):
		scan(self.address, self.port)

def main(host, prange="1-1025"):
	try:
		print "[!] Scanning ", gethostbyname(host)
	except:
		print "\n[x] Host seems offline"; exit()
	print "[*] Process started at %s....\n" % time.strftime("%H:%M:%S")
	threadList = []
	global address
	address = host
	prange_split = prange.split("-")

	try:
		for port in range(int(prange_split[0]), int(prange_split[1])+1):
			newthread = mainApp(address, port)
			newthread.start()
			threadList.append(newthread)
		for threads in threadList:
			threads.join()
	except:
		print "[x] Error Occured, -h to view help"; exit()
	print "\n[*] Port scanning completed at %s...." % time.strftime("%H:%M:%S")

if __name__ == "__main__":
	if len(sys.argv) == 2:
		if sys.argv[1] == '-h' or sys.argv[1] == '--help':
			help()
		else:
			main(sys.argv[1])
	elif len(sys.argv) == 3:
		if sys.argv[1] != '-h':
			main(sys.argv[1], sys.argv[2])
		else:
			help()
	else:
		help()
