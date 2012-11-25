#!/usr/bin/env python

from socket import socket
from thread import start_new_thread
from sys import exit
from time import sleep
import __builtin__

class ListServer:
	def __init__(self):
		try:
			__builtin__.server = dict()
			self.socket = socket()
			self.socket.bind(("0.0.0.0", 8001))
			self.socket.listen(1024)

			while True:
				client, address = self.socket.accept()
				print("CONNECT: " + address[0])
				start_new_thread(self.list, (client, address))

			self.socket.close()
		except Exception,e:
			print(str(e))
			pass
		except KeyboardInterrupt:
			exit("Abort ...")
		finally:
			return None

	def list(self, client, address):
		try:
			while True:
				line = client.recv(1024).rstrip()
				if not line:
					client.close()
					print("DISCONNECT: " + address[0])

				if len(line.split()) == 1:
					if line == "/LIST":
						for key in server.keys():
							client.send("0x0;" + server[key][0] + ";" + server[key][1] + ";" + server[key][2] + "\n")
					if line == "/QUIT":
						client.close()
				elif len(line.split()) > 1:
					if line.split()[0] == "/REGISTER":
						data = ' '.join(line.split()[1:])
						__builtin__.server[str(address[0]) + " " + str(data.split(";")[1])] =  [str(data.split(";")[0]), str(address[0]), str(data.split(";")[1])]
		except Exception,e:
			print(str(e))
			pass
		except KeyboardInterrupt:
			exit("Abort ...")
		finally:
			return None

ListServer()