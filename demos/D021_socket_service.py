#! /usr/bin/python
# -*- coding:UTF-8 -*-

import socket

serviceSocket = socket.socket()
host = socket.gethostname() #获取本地主机名
port = 12345

print "host = %s, port = %s" % (host, port)

serviceSocket.bind((host, port))

serviceSocket.listen(3)

while True:
	con, address = serviceSocket.accept()
	print "address : ", address
	con.send("welcome !!!")
	con.close()
