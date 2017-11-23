#! /usr/bin/python
# -*- coding:UTF-8 -*-

list = ['a', 'b', 'c', 'd', 'e', 'f']
print 'len = ',len(list)

print '-------------------------------------'
for letter in list:
	print 'letter = ',letter

print '-------------------------------------'
for index in range(len(list)):
	print 'letter = ',list[index]

print '-------------------------------------'
for index, letter in enumerate(list):
	print 'index = %s, letter = %s' % (index, letter)

print '-------------------------------------'
for index, letter in enumerate(list[2:5]):
	print 'index = %s, letter = %s' % (index, letter)
