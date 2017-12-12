#! /usr/bin/python
# -*- coding:UTF-8 -*-

# abs() 取绝对值
print "abs(-15):",abs(-45)
print "abs(99.2):",abs(99.2)

print "***********************************"
# all() 用于判断给定的可迭代参数 iterable 中的所有元素是否不为 0、''、False 或者 iterable 为空，如果是返回 True，否则返回 False。

list = [1 , 2, 3, 4]
print list
print "all(list):",all(list)
print "----------------------------------"

list = ['a', '', 'c']
print list
print "all(list):",all(list)
print "----------------------------------"

tuple = (0, 1, 2)
print tuple
print "all(tuple):",all(tuple)
print "----------------------------------"

print "all([]):",all([]) # 注意：空元组、空列表返回值为True，这里要特别注意
print "all(()):",all(())

print "***********************************"
# any() 用于判断给定的可迭代参数 iterable 是否全部为空对象，如果都为空、0、false，则返回 False，如果不都为空、0、false，则返回 True

list = [1, 2, 3]
print list
print "any(list):",any(list)
print "----------------------------------"

list = ['a', '', 'b']
print list 
print "any(list):",any(list)
print "----------------------------------"

list = [0, '', False]
print list
print "any(list):",any(list)
print "----------------------------------"

print "any([]):",any([])
print "any(())",any(())
print "----------------------------------"

print "***********************************"
# bin() 返回一个整数 int 或者长整数 long int 的二进制表示

print "bin(8)",bin(8)
print "bin(12)",bin(12)
print "----------------------------------"

print "***********************************"
# cmp() 用于比较2个对象，如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1。

print "cmp(1, 2) :",cmp(1, 2)
print "cmp(1, 1) :",cmp(1, 1)
print "cmp(2, 1) :",cmp(22, 1)
print "----------------------------------"
print "***********************************"
print "***********************************"
print "***********************************"



