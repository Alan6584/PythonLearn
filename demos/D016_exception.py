#! /usr/bin/python
# -*- coding:UTF-8 -*-

def div(a, b):
	ret = 0
	try:
		ret = a / b
		print "1-->ret :",ret
	except Exception as e:
		print "0不能被除"
	else:
		print "2-->执行成功，ret :",ret
	finally:
		print "3-->finally, ret :",ret

div(1.0,2)
print "------------------------------"
div(1.0,0)
