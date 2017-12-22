#! /usr/bin/python
# -*- coding:UTF-8 -*-

import re

str = "010-12345"

ret = re.match(r'^\d{3}\-\d{3,8}$', str)
if ret:
	print "OK"
else:
	print "Failed"


