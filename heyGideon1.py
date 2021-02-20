#/usr/bin/env python3
import socket
from threading import *

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "0.0.0.0"
port = 1738
print (host)
print (port)
serversocket.bind((host, port))

class client(Thread):
    def __init__(self, socket, address):
        Thread.__init__(self)
        self.sock = socket
        self.addr = address
        self.start()
        

    def run(self):
        while 1:
            print('Client sent:', self.sock.recv(1024).decode())
            message = (b"YOU DIDN'T SAY THE MAGIC WORD HAHAHAHA") * 65535
            self.sock.send(message)

serversocket.listen(5)
print ('server started and listening')
try:
	while 1:
	    clientsocket, address = serversocket.accept()
	    client(clientsocket, address)
except KeyboardInterrupt:
	sock.close()
