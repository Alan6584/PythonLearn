#! /usr/bin/python
# -*- coding:UTF-8 -*-

import re

# str = "010-123" # OK
# str = "010-12345" # OK
str = "010-12345678" # OK
# str = "010-123456789" # Failed
# str = "0110-12345678" # O# Failed

# 匹配{三位数字}-{3到8位数字}
ret = re.match(r'^\d{3}\-\d{3,8}$', str)

if ret:
	print "OK"
else:
	print "Failed"


