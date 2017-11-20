#!/usr/bin/python
# -*- coding:UTF-8 -*-

list = [1,2,3,4,5,6]
a = 1
b = 8
if(a in list):
    print "a is in list"
else:
    print "a is not in list"

print '------------------------------------'

if(b not in list):
    print "b is not in list"
else:
    print "b is in list"

print '------------------------------------'

# is 与 == 的区别：is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。
# x is y, 类似 id(x) == id(y) , 如果引用的是同一个对象则返回 True，否则返回 False

a = b = 3.0
if(a is b):
    print 'a is b'
else:
    print 'a is not b'

if(a == b):
    print 'a == b'
else:
    print 'a != b'
print '------------------------------------'
