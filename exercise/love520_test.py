# -*- coding: utf-8 -*-
# @Time    : 2018-04-11 09：58
# @Author  : jianjun.wang
# @FileName: devices.py

import time
import datetime

startMeetDate = datetime.datetime(2000, 9, 1) # 相识的时间
startLoveDate = datetime.datetime(2016, 3, 21) # 相恋的时间
marryDate = datetime.datetime(2017, 3, 13) # 结婚的时间

todayDate = datetime.datetime.today()


haveMeetDays = (todayDate - startMeetDate).days
inLoveDays = (todayDate - startLoveDate).days
haveMarriedDays = (todayDate - marryDate).days

'''
difDays = todayDate - startLoveDate
print difDays.total_seconds()
hours = difDays.total_seconds() / 60 / 60
print hours

testDays = hours / 24
print testDays

# print dir(datetime.timedelta)
'''

print "亲爱的宝贝儿："
print "我们相识 {0} 天".format(haveMeetDays)

print "我们相爱 {0} 天".format(inLoveDays)

print "我们结婚 {0} 天".format(haveMarriedDays)