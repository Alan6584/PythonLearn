#! /usr/bin/python
# -*- coding:UTF-8 -*-

import os

path = "./test/D014_file.txt"
ret = os.access(path, os.F_OK)
print "F_OK : %s" % ret

ret = os.access(path, os.R_OK)
print "R_OK : %s" % ret

ret = os.access(path, os.W_OK)
print "W_OK : %s" % ret

ret = os.access(path, os.X_OK)
print "X_OK : %s" % ret

print "----------------------"
print os.listdir("./")
