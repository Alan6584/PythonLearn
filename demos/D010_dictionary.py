#!/usr/bin/python
# -*- coding:UTF-8 -*-

dict = {'name':'Alan', 'email':'alan6584@gmail.com'}
print dict
print "dict['name'] =",dict['name']
print "dict['email'] =",dict['email']

print "len(dict) =",len(dict)
print "str(dict) =",str(dict) 
print "type(dict) =",type(dict) 

print dict.get("name", "Wang")
print dict.get("country", "China")

print "dict.has_key('email') =",dict.has_key("email")
print "dict.items() =",dict.items()

print "dict.keys() =",dict.keys()
print "dict.values() =",dict.values()
