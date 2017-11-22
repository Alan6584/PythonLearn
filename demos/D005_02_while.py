#! /usr/bin/python
# -*- coding:UTF-8 -*-

import random

rnum = int(random.uniform(1, 10))
print rnum

uin = int(input('请输入整数：'))

while rnum != uin:
    if uin > rnum:
        print '大了'
    elif uin < rnum:
        print '小了'
    else:
        print '猜对了'
        break
    uin = int(input('请输入整数：'))
else:
    print '退出！'
