#!/usr/bin/python
# -*- coding:UTF-8 -*-
a = 2
b = 3
c = a / b

print "a = ", a, "b = ", b
print "a / b = ", c #如果两个都是整数，结果也为整数，如果想得到小数部分，可将其中一个改成浮点型即可

b = 3.0
c = a / b
print "a / b = ", c 

c = a ** b #值为a的b次方
print "a ** b = ", c

print "-----------------------------------------------"
a = 6
b = 4
print "a = ", a, "b = ", b
c = a % b #取模，返回商的整数部分
print "a % b = ", c

c = a // b #取整除，返回商的整数部分
print "a // b = ", c

print "-----------------------------------------------"

a = 5
b = 8
c = a and b
print "a = ", a, ", b = ", b
print "(a and b) = ",c #如果a为 False，a and b 返回 False，否则它返回b 的计算值。(a and b) 返回 8

a = 0 
print "a = ", a, ", b = ", b
c = a and b
print "(a and b) = ",c 
if (a and b):
    print "a and b is true"
else:
    print "a and b is false"
print "-----------------------------------------------"

a = 1 
print "a = ", a, ", b = ", b
c = a or b #如果a为非0值，返回a的值，否则返回b的值
print "(a or b) = ",c 
print "-----------------------------------------------"

a = 0 
print "a = ", a, ", b = ", b
c = a or b #如果a为非0值，返回a的值，否则返回b的值
print "(a or b) = ",c 
print "-----------------------------------------------"


a = 1 
print "a = ", a, ", b = ", b
c = not a
print "(not a) = ",c
print "-----------------------------------------------"

