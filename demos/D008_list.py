#!/usr/bin/python
# -*- coding:UTF-8 -*-

list = ['a', 'b', 'c', 'd']
print list

print max(list)
print min(list)

print list.count('a')

print '------------------------------'
del list[3]
print list
list.append('e')
print list
print list.index('e')
list.insert(3, 'd')
print list
list.remove('e')
print list

print '------------------------------'
list2 = [1, 3, 2, 5, 4]
list2.sort()
print list2

print '------------------------------'
list.extend(list2)
print list
list.reverse()
print list
