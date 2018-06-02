# -*- coding: utf-8 -*-
# @Time    : 2018-04-11 09：58
# @Author  : jianjun.wang
# @FileName: devices.py

import time



# print('\n'.join([''.join([('LoveTuTu'[(x-y)%8] if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ') for x in range(-30,30)]) for y in range(15,-15,-1)]))


print
print
item = "ILoveYou TuYing "
#要想实现打印出字符间的空格效果，此处添加：item = item+' '
letterlist = []#letterlist是所有打印字符的总list，里面包含y条子列表list_X
for y in range(12, -12, -1):
    list_X = []#list_X是X轴上的打印字符列表，里面装着一个String类的letters
    letters = ''#letters即为list_X内的字符串，实际是本行要打印的所有字符
    for x in range(-30, 30):#*是乘法，**是幂次方
        expression = ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3
        if expression <= 0:
            letters += item[(x-y) % len(item)]
        else:
            letters += ' '
    list_X.append(letters)
    letterlist += list_X
print('\n'.join(letterlist))

print
print
# item = "I ♡ U TuYing "
# item = "520 ty "
# item = "520 "
item = "LoveU"
#要想实现打印出字符间的空格效果，此处添加：item = item+' '
letterlist = []#letterlist是所有打印字符的总list，里面包含y条子列表list_X
for y in range(12, -12, -1):
    list_X = []#list_X是X轴上的打印字符列表，里面装着一个String类的letters
    letters = ''#letters即为list_X内的字符串，实际是本行要打印的所有字符
    for x in range(-30, 30):#*是乘法，**是幂次方
        expression = ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3
        if expression <= 0:
            letters += item[(x-y) % len(item)]
        else:
            letters += ' '
    list_X.append(letters)
    letterlist += list_X
print('\n'.join(letterlist))

'''
words = raw_input('Please input the words you want to say!:')
#例子：words = "Dear lili, Happy Valentine's Day! Lyon Will Always Love You Till The End! ♥ Forever!  ♥"
for item in words.split():
    #要想实现打印出字符间的空格效果，此处添加：item = item+' '
    letterlist = []#letterlist是所有打印字符的总list，里面包含y条子列表list_X
    for y in range(12, -12, -1):
        list_X = []#list_X是X轴上的打印字符列表，里面装着一个String类的letters
        letters = ''#letters即为list_X内的字符串，实际是本行要打印的所有字符
        for x in range(-30, 30):#*是乘法，**是幂次方
            expression = ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3
            if expression <= 0:
                letters += item[(x-y) % len(item)]
            else:
                letters += ' '
        list_X.append(letters)
        letterlist += list_X
    print('\n'.join(letterlist))
'''
