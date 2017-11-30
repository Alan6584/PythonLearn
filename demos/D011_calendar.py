#!/usr/bin/python
# -*- coding:UTF-8 -*-

import calendar
cal = calendar.month(2018, 1)
print cal

print calendar.firstweekday()

print "calendar.isleap(2018) : ",calendar.isleap(2018)

print "------------------------"
print calendar.monthcalendar(2018, 1)

print "------------------------"
print calendar.monthrange(2018, 1)

print "------------------------"
print calendar.weekday(2018,11,28)

print "------------------------"
#返回一个多行字符串格式的year年年历，3个月一行，间隔距离为c。 每日宽度间隔为w字符。每行长度为21* W+18+2* C。l是每星期行数。
# print calendar.calendar(2018, w=2, l=1, c=6)
