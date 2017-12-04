#! /usr/bin/python
# -*- coding:UTF-8 -*-

import os

fp = open("./test/D014_file.txt", "rb")

str = fp.readline()
print str
print fp.tell()
print "-------------"

str = fp.readline()
print str
print fp.tell()
print "-------------"

fp.seek(0, 0)

str = fp.read(100)
print str

print fp.tell()
print os.getcwd()

fp.close()
