#!/usr/bin/python
#Sangram Grewal

#FOR THE CLIENT

#import relevant modules
import socket
import os
import sys

#confirm args are valid for this script
if len(sys.argv) < 4:
	exit(1)

#get name of file to be transferred from args
filename = sys.argv[3]

#confirm file exists, open it if it does
if len(filename) <= 1:
	sys.exit("File doesn't exist")
infile = open(filename, 'rb')

#create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#get destination ip address from args
ip = sys.argv[1]

#get destination port number from args
port = int(sys.argv[2])

#bring the socket online
s.connect((ip, port))

#transfer the file size first- packet will always be 4 bytes long
size = os.path.getsize(filename)
size_s = str(size)
#making sure the file size packet is always 4 bytes
#if size > 4 bytes, it is concatenated
if len(size_s) > 4:
	size_s = size_s[:5]
#if size < 4 bites, the packet is filled with whitespace until it's 4 bytes	
while len(size_s) < 4:
	size_s = ' ' + size_s
size_b = str(size_s).encode()
s.send(size_b)

#next transfer file name- packet will always be 20 bytes
name_s = filename
#make sure the name packet size is alwasy 20 bytes
if len(name_s) > 20:
	name_s = name_s[:21]
while len(name_s) < 20:
	name_s = ' ' + name_s	
name_b = name_s.encode('utf-8')
s.send(name_b)

#read and send first 1000 bytes from file
data = infile.read(1000)

#loop and read/send data in 1000 byte chunks
while data:
	s.send(data)
	data = infile.read(1000)

#cleanup
infile.close()
s.close()

