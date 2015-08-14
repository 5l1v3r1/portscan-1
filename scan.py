#!/usr/bin/env python
# Hades.y2k
# 13/Aug/2015
# GNU GPL <v2.0>
from socket import *
import threading
import sys, time

ip = ''
host = ''

class main():
	def __init__(self):
		self.banner()
		self.askhost()
		self.start(host, ip)

	def banner(self):
		print "\n\t\t+--------------------------------+"
		print "\t\t+------ Port Scanner ------------+"
		print "\t\t+------------------- Hades.y2k --+"
		print "\t\t+--------------------------------+"

	def askhost(self):
		global host
		host = raw_input('Enter the Host: ')
		try:
			global ip
			ip = gethostbyname(host)
		except Exception as e:
			print "[!]", e
			sys.exit(1)

	# Threads
	def thread1(self, host, port):
		for port in range(1, 512):
			s = socket(AF_INET, SOCK_STREAM)
			s.settimeout(0.5)
			try:
				sent = s.connect((host, port))
				print "[+] Port %d open" % port
			except:
				pass
			s.close()
	def thread2(self, host, port):
		for port in range(513, 1024):
			s = socket(AF_INET, SOCK_STREAM)
			s.settimeout(0.5)
			try:
				sent = s.connect((host, port))
				print "[+] Port %d open" % port
			except:
				pass
			s.close()

	def start(self, host, ip):
		print "[*] Host: %s IP: %s" % (host, ip)
		print "[*] Process started at %s....\n" % time.strftime("%H:%M:%S")
		try:
			first = threading.Thread(target=self.thread1(host,ip))
			second = threading.Thread(target=self.thread2(host,ip))
			first.start()
			second.start()
		except:
			pass
		print "\n[*] Port scanning completed at %s...." % time.strftime("%H:%M:%S")

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print "\n[!] User interrupted the process"
		print "[!] Program terminating........."
		sys.exit(0)
