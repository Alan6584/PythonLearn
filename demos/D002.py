#! /usr/bin/python
# -*- coding: UTF-8 -*-
print "Hello Alan!"
a = 2
print a
a = "string"
print a

print "----------------------------------------"
list = [1, 'this', "is", "list"]
tinyList = [2, 3]
print "list = ", list  #输出整个列表
print "list[2] = ", list[2] #输出列表的第三个元素
print "list[1:3] = ", list[1:3] #输出第二和第四个之间的元素，不包括第四个元素
print "list[2:] = ", list[2:] #输出从第三个开始的元素
print "list * 2 = ", list * 2 #将列表输出两次, * 是重复操作
print "list + tinyList", list + tinyList #拼接列表

print "----------------------------------------"
tuple = (2, "this", 'is', "tuple")
#tuple[1] = 2 #元祖不能重新复制，属于只读列表
print tuple 

print "----------------------------------------"
dictionary = {"a":2, "name":"this is dictionary"}
print "dictionary[\"a\"] = ", dictionary["a"]
print "dictionary.keys() = ", dictionary.keys()
print "dictionary.values() = ", dictionary.values()
print dictionary
