#! /usr/bin/python
# -*- coding:UTF-8 -*-

fp = open("./test/D014_file.txt", "rb")
str = fp.read(60)
print str

fp.close()
