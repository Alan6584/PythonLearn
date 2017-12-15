#! /usr/bin/python
# -*- coding:UTF-8 -*-

class Student:
	'学生类'
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def display(self):
		print "name = %s, age = %d" % (self.name, self.age)

s = Student("Tom", 16)
s.display()
