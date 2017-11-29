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

print '--------------------------------'
for key,value in dict.items():
	print ("key = " + key + " , value = " + value)

print '--------------------------------'
users = {
	"Alan":{
		"id":"0001",
		"email":"alanwang6584@gmail.com",
		"location":"HB"
	},
	"Jajuan":{
		"id":"0002",
		"email":"jajuan@gmail.com",
		"location":"BJ"
	}
}

print users

print '--------------------------------'
for username,userinfo in users.items():
	print("username:" + username + "\nuserId:" + userinfo["id"] + "\nuserEmail:" + userinfo["email"] + "\nuserLocation:" + userinfo["location"])
	print '--------------------------------'
