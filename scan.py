#!/usr/bin/env python
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
	print """-h --help     View help
Usage: python <filename>.py IP
  www.github.com/Hadesy2k/"""

class mainApp(threading.Thread):
	def __init__(self, address, port):
		threading.Thread.__init__(self)
		self.address = address
		self.port = port
		self.run()

	def run(self):
		scan(self.address, self.port)

def main(host):
	try:
		print "[!] Scanning ", gethostbyname(host)
	except:
		print "\n[x] Host seems offline"; exit()
	print "[*] Process started at %s....\n" % time.strftime("%H:%M:%S")
	threadList = []
	global address
	address = host
	for port in range(1, 1025):
		newthread = mainApp(address, port)
		newthread.start()
		threadList.append(newthread)
	for threads in threadList:
		threads.join()
	print "\n[*] Port scanning completed at %s...." % time.strftime("%H:%M:%S")

if __name__ == "__main__":
	if len(sys.argv) == 2:
		if sys.argv[1] == '-h' or sys.argv[1] == '--help':
			help()
		else:
			main(sys.argv[1])
	else:
		help()
