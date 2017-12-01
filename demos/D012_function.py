#! /usr/bin/python
# -*- coding:UTF-8 -*-

def sum(a, b):
	s = a + b
	return s

print sum(1, 2)

print "-----------------------------"

def changeList(list):
	list.append(3)
	print "changeList-->",list
	return
list = [1,2,3,4,5]
print list
changeList(list)
print list

print "-----------------------------"


def printInfo(name, age=24):
	print "name =",name,",age =",age
	return
printInfo("Alan") #使用缺省参数
printInfo(age=26,name="Alan") #使用关键字参数允许调用时与声明时的顺序不一致
printInfo("Wang", 27)

print "-----------------------------"
def printParams(arg1, *vars):
	"可变参数"
	print "params:"
	print arg1
	for var in vars:
		print var
	return
printParams(1, 2, 3, 4, 5)
printParams(1, "a", 'b')

print "-----------------------------"
add = lambda a,b: a+b
print "add(2,3) :",add(2,3)
print "add(12,13) :",add(12,13)

print "-----------------------------"
globvar = 0
def globAdd(a):
	global globvar #使用global声明全局变量
	globvar += a
	return
print globvar
globAdd(3)
print globvar

