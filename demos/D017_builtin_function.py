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

