#!/usr/bin/python
# -*- coding:UTF-8 -*-

tup = ('a', 'b', 'c')
print tup
print 'tup[0] =', tup[0]
# tup[1] = 'bb' # 非法操作，元组的元素不能修改，object does not support item assignment

print 'tup[1:3] =',tup[1:3] 
print 'tup[1:] =',tup[1:] 

print 'len(tup) =',len(tup)
print 'max(tup) =',max(tup)
print 'min(tup) =',min(tup)

list = [1, 2, 3, 4, 5]
print 'tuple(list) =',tuple(list)

tup1 = ('Hello')
print 'tup1 =',tup1

tup2 = ('Alan',) #括号()既可以表示tuple，又可以表示数学公式中的小括号,所以，如果元组只有1个元素，就必须加一个逗号，防止被当作括号运算
print 'tup2 =',tup2

