#! /usr/bin/python
# -*- coding:UTF-8 -*-

import socket

clientSocket = socket.socket()
host = socket.gethostname() #获取本地主机名
port = 12345

print "host = %s, port = %s" % (host, port)

clientSocket.connect((host, port))

data = clientSocket.recv(1024)
print "data : ", data 
clientSocket.close()
