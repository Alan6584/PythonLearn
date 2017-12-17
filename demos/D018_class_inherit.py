#! /usr/bin/python
# -*- coding:UTF-8 -*-

class Person:
	'Person基类'
	def __init__(self, name, age):
		self.name = name
		self.age = age
		print "Person()--->init()--->name = %s, age = %d" % (self.name, self.age)

	def display(self):
		print "Person()--->name = %s, age = %d" % (self.name, self.age)



class Student(Person):
	'学生类'
	def __init__(self, name, age, score):
		Person.__init__(self, name, age)
		self.score = score
		print "Student()--->init()--->name = %s, age = %d" % (self.name, self.age)


	def display(self):
		print "Student()---->name = %s, age = %d" % (self.name, self.age)

s = Student("Tom", 16, 96)
s.display()
