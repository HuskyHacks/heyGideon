#/usr/bin/env python3
import socket
from threading import *
import os

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "0.0.0.0"
port = 1812
print(host)
print(port)
serversocket.bind((host, port))

class client(Thread):
	def __init__(self, socket, address):
		Thread.__init__(self)
		self.sock = socket
		self.addr = address
		self.start()
	
	def run(self):
		while 1:
			message = b"\nHey Gideon! Please enter the name of the greatest hacker alive. Answer in the form of \"HuskyHacks\"\n"
			self.sock.send(message)
			winning = "HuskyHacks"
			if winning in self.sock.recv(1024).decode():
				winMessage = b"\n [******WINNING*****] Aww that's so nice of you to say! This server is just a cmd exec echo server. So just try entering a reverse shell or something :)\n (lol thanks for being a good sport)[******WINNING*****]\n"
				self.sock.send(winMessage)
			else:
				print('Client sent:', self.sock.recv(1024).decode())
				try:
					cmd = self.sock.recv(1024).decode()
					os.system(cmd)
				except Exception as e:
					pass


serversocket.listen(5)
print('server started and listening')
try:
	while 1:
		clientsocket, address = serversocket.accept()
		client(clientsocket, address)

except Exception as e:
		client.close()
