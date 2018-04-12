#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@Time    : 2018-04-11 17：58
@Author  : jianjun.wang
@Email   : alanwang6584@gmail.com
"""

import sys

def main():
	print 'arg num : ', len(sys.argv)
	print 'args : ', sys.argv
	print 'script name : ', sys.argv[0]

	for i in range(len(sys.argv)):
		print "arg[{0}] = {1}".format(i, sys.argv[i])

if __name__ == "__main__":
    main()