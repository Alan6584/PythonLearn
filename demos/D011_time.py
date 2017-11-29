#!/usr/bin/python
# -*- coding:UTF-8 -*-

import time; #引入time模块

ticks = time.time()
print "ticks =", ticks

localtime = time.localtime(time.time())
print localtime
print time.localtime()


print "----------------------------------"
localtime1 = time.asctime(localtime)
print("time.asctime(localtime) :\n" + localtime1)

localtime2 = time.asctime()
print("time.asctime() :\n" + localtime2)

localtime3 = time.ctime()
print("time.ctime() :\n" + localtime3)

print "----------------------------------"
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print time.strftime("%Y-%m-%d %H:%M:%S %d %b %B %a %A", time.localtime())
print time.strftime("%c", time.localtime())

print "----------------------------------"
print("time.clock()) : %f" % time.clock())
