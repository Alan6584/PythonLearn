#! /usr/bin/python
# -*- coding: UTF-8 -*-

str = "{} {}".format("Hello", "Alan") #不设置指定位置，按默认顺序
print str

str = "{0} {1}, {0} {2}".format('Hello', 'World', 'Alan') #设置指定位置
print str

str = "name : {name} \nemail : {email}".format(name = "Alan", email = "alan6584@gmail.com")
print str

#通过字典设置参数
info = {'name' : 'Alan', 'email':'alan6584@gmail.com'}
print info
str = "name : {name} \nemail : {email}".format(**info)
print str

infolist = ['Alan', 'alan6584@gmail.com']
print infolist
str = "name : {0[0]} \nemail : {0[1]}".format(infolist)
print str
