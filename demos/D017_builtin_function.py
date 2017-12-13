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
# divmod() 把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a // b, a % b)

print "divmod(7,2)",divmod(7,2)
print "divmod(9,3)",divmod(9,3)
print "----------------------------------"

print "***********************************"
# enumerate() 用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中

list = ['a', 'b', 'c']
for i, element in enumerate(list):
	print i, list[i], element
print "----------------------------------"

print "***********************************"
# filter() 用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表

def is_odd(n):
	return n % 2 == 1
list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
newlist = filter(is_odd, list)
print list
print newlist
print "----------------------------------"

print "***********************************"
# map() 会根据提供的函数对指定序列做映射

def square(x):
	return x ** 2
list = [1, 2, 3, 4, 5, 6]
list1 = map(square, list)
list2 = map(lambda x: x ** 2, list) #使用lambda匿名函数
print list
print list1
print list2
print "----------------------------------"

print "***********************************"

print "----------------------------------"

print "***********************************"

print "----------------------------------"

print "***********************************"

print "----------------------------------"



