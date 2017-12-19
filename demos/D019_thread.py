#! /usr/bin/python
# -*- coding:UTF-8 -*-

import threading
import time

class MyThread(threading.Thread):
	'自定义线程'
	def __init__(self, threadID, count):
		threading.Thread.__init__(self)
		self.threadID = threadID 
		self.count = count 

	def run(self):
		print "MyThread:%d -->run start......count:%d" % (self.threadID, self.count)

t1 = MyThread(1, 5)
t2 = MyThread(2, 6)
t1.start()
t2.start()
