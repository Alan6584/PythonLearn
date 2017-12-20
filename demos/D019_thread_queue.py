#! /usr/bin/python
# -*- coding:UTF-8 -*-

import Queue
import threading
import time

exitFlag = 0

class MyThread(threading.Thread):
	'自定义线程'
	def __init__(self, threadID, queue, lock):
		threading.Thread.__init__(self)
		self.threadID = threadID 
		self.queue = queue 
		self.lock = lock

	def run(self):
		print "MyThread:%d -->run start......" % (self.threadID)
		self.__loop(self.queue)
		print "MyThread:%d -->run end......" % (self.threadID)

	def __loop(self, queue):
		while not exitFlag:
			try:
				self.lock.acquire()
				if not self.queue.empty():
					data = self.queue.get()
					print "MyThread : %d--->>data = %s" % (self.threadID, data)
			except BaseException:
				print "occur exception"
			finally:
				self.lock.release()

			time.sleep(1) #睡眠1秒
		print "MyThread:%d -->loop()......end" % (self.threadID)

lock = threading.Lock()
queue = Queue.Queue()
threadList = []

for index in range(3):
	thread = MyThread(index, queue, lock)
	thread.start()
	threadList.append(thread)

lock.acquire()
for i in range(8):
	s = "num_%d" % (i)
	queue.put(s)
lock.release()

while not queue.empty():
	pass

exitFlag = 1

for t in threadList:
	t.join()

print "All Thread Exit"
