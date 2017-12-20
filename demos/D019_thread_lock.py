#! /usr/bin/python
# -*- coding:UTF-8 -*-

import threading
import time

class MyThread(threading.Thread):
	'自定义线程'
	def __init__(self, threadID, count, lock):
		threading.Thread.__init__(self)
		self.threadID = threadID 
		self.count = count 
		self.lock = lock

	def run(self):
		print "MyThread:%d -->run start......count:%d" % (self.threadID, self.count)
		self.lock.acquire()
		try:
			self.__loop(self.count)
		except BaseException:
			print "occur exception"
		finally:
			self.lock.release()
		print "MyThread:%d -->run end......" % (self.threadID)

	def __loop(self, count):
		while (count > 0):
			time.sleep(1) #睡眠1秒
			print "MyThread:%d -->loop()......count:%d" % (self.threadID, count)
			count -= 1

lock = threading.Lock()
t1 = MyThread(1, 5, lock)
t2 = MyThread(2, 6, lock)
t1.start()
t2.start()
t1.join()
t2.join()
print "All Thread Exit"
