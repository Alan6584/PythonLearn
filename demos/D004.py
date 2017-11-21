#! /usr/bin/python
# -*- coding:UTF-8 -*-

num = 3
if num == 1:
    print 'the num is one'
elif num == 2:
    print 'the num is two'
elif num == 3:
    print 'the num is three'
else:
    print 'other nums'

if num >= 0 and num < 10:
    print 'this is valid num'
else:
    print 'this is valid num'


if num < 0 or num > 9:
    print 'the num is not in 0~9'
else:
    print 'the num is valid'


if (num >= 0 and num <= 5) or (num >= 10 and num <= 16):
    print "good num"
else:
    print 'unknown'
