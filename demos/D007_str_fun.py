#! /usr/bin/python
# -*- coding: UTF-8 -*-


str = 'alan'
print str.center(10) # center函数，返回一个原字符串居中，并使用空格填充至width的新字符
print str.center(10, '-')

print str.count('a') # 返回字符a在字符串中出现的次数

str = 'Hello Alan'
print str
str = str.encode('UTF-8', 'strict')
print 'Encoded str :', str 

str = str.decode('UTF-8', 'strict')
print 'Decoded str :', str 

print '-------------------------------------'
str = 'Hello my name is Alan, weight is 65kg'
print str.startswith('Hello')
print str.endswith('kg')
print str.find('Alan')
print str.isalnum() #如果str中至少有一个字符并且所有字符都是字母或数字则返回True否则返回False
print str.isalpha() #如果str中至少有一个字符并且所有字符都是字母则返回True否则返回False

print '-------------------------------------'
print str.isdigit() # 如果str中只包含数字则返回True
a = '12345'
print a.isdigit()

list = ['a', 'b', 'c', 'd']
print list
a = '-'
print a.join(list) # 以 string 作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串

print '-------------------------------------'
print str.lower()
print str.upper()
print str.title() #返回"标题化"的 string,就是说所有单词都是以大写开始，其余字母均为小写

print '-------------------------------------'
print str.split(',') #以 str 为分隔符切片 string

print '-------------------------------------'
a = '   hello world!  '
print a
print a.strip()
print a.lstrip()
print a.rstrip()

print '-------------------------------------'
a = '***hello world!***'
print a
print a.strip('*')
print a.lstrip('*')
print a.rstrip('*')



