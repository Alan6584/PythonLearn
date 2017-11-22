#! /usr/bin/python
# -*- coding:UTF-8 -*-

import sys

denum = input("输入十进制数:")
print denum,"(10)",
binnum = []
# 二进制数
while denum > 0:
    binnum.append(str(denum % 2)) # 栈压入
    denum //= 2
print '= ',
while len(binnum)>0:
    #print binnum.pop(),
    sys.stdout.write(binnum.pop()) # 无空格输出print ' (2)'
