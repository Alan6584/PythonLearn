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
# ord() 
print "ord('a')",ord('a')
print "ord('b')",ord('b')

print "----------------------------------"

print "***********************************"
# range() 可创建一个整数列表，一般用在 for 循环中

print "range(5):",range(5)
print "range(1, 10, 2):",range(1, 10, 2)
print "range(10, 0, -2):",range(10, 0, -2)
print "----------------------------------"

print "***********************************"
# reverse() 用于反向列表中元素

list = [1, 2, 3, 4, 5]
print list
list.reverse()
print list
print "----------------------------------"


print "***********************************"
# round() 四舍五入

a = 2.345631
print a
print "round(a, 1)",round(a, 1)
print "round(a, 2)",round(a, 2)
print "round(a, 3)",round(a, 3)
print "----------------------------------"

print "***********************************"
# set() 创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等

x = set([1, 2, 3, 4])
y = set([3, 4, 5, 6])
print x
print y 

print "x | y : ",x | y
print "x & y : ",x & y
print "x - y : ",x - y
print "----------------------------------"

print "***********************************"
# sorted() 对所有可迭代的对象进行排序操作,返回新列表
#  key 和 reverse 比一个等价的 cmp 函数处理速度要快。这是因为对于每个列表元素，cmp 都会被调用多次，而 key 和 reverse 只被调用一次

students = [('Army', 'A', 16), ('Jane', 'B', 17), ('Tom', 'C', 15)]
print students
print sorted(students, cmp=lambda x,y:cmp(x[2],y[2])) #按年龄排序
print sorted(students, key=lambda x:x[1]) #按成绩排序
print sorted(students, key=lambda x:x[2], reverse=True) #按年龄降序排列
print "----------------------------------"
print "***********************************"

print "----------------------------------"
print "***********************************"

print "----------------------------------"
print "***********************************"

print "----------------------------------"
print "***********************************"

print "----------------------------------"

