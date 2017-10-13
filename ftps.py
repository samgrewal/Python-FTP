#!/usr/bin/python
#Sangram Grewal

#FOR THE SERVER

#import relevant modules
import socket
import os
import sys

#confirm args are valid for this script
if len(sys.argv) < 2:
	exit(1)

#get listening port from args
port = int(sys.argv[1])	

#create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#get the server's address for the socket
host = socket.gethostname()

#bring the socket online
s.bind((host, port))

#establish only one client served at a time
s.listen(1)

#begin service
c, a = s.accept()

#get size of file from client- it's always 4 bytes as per the protocol
file_size = c.recv(4)
print("Size of file: " + file_size.decode().strip() + " bytes")

#get name of file from client- it's always 20 bytes as per the protocol
filename_b = c.recv(20)
filename = filename_b.decode('utf-8')
filename = str(filename).strip()
print("Filename: " + filename)


#create a destination
os.makedirs('./recv', exist_ok=True)

#open the destination file
ofile = open('./recv/'+filename, 'wb+')

#read first 1000 bytes from client
data = c.recv(1000)

#loop and receive/write data in 1000 byte chunks
while data:
	ofile.write(data)
	data = c.recv(1000)

#close files & cleanup
c.close()
s.close()

