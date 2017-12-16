#! /usr/bin/python
# -*- coding:UTF-8 -*-

class Person:
	'Person基类'
	def __init__(self, name, age):
		self.name = name
		self.age = age
		print "init()--->name = %s, age = %d" % (self.name, self.age)

	def display(self):
		print "name = %s, age = %d" % (self.name, self.age)



class Student(Person):
	'学生类'

	def display(self):
		print "name = %s, age = %d" % (self.name, self.age)

s = Student("Tom", 16)
s.display()
