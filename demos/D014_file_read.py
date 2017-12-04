#! /usr/bin/python
# -*- coding:UTF-8 -*-

import os

fp = open("./test/D014_file.txt", "rb")
str = fp.read(60)
print str

print fp.tell()
print os.getcwd()

fp.close()
