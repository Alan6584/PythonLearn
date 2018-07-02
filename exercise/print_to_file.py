#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@Time    : 2018-07-01 17：41
@Author  : jianjun.wang
@Email   : alanwang6584@gmail.com

说明：目录处理的练习
"""

import os
import sys
import codecs



def main():

	#将输出重定向到txt文件
	output = sys.stdout
	outputfile = codecs.open("/Users/wangjianjun/Alan/me/audio/data/story.txt", 'w', encoding='utf-8')
	sys.stdout = outputfile

	print 'arg num : ', len(sys.argv)
	print 'args : ', sys.argv
	print 'script name : ', sys.argv[0]

	for i in range(len(sys.argv)):
		print "arg[{0}] = {1}".format(i, sys.argv[i])

	outputfile.close()
	sys.stdout = output


if __name__ == "__main__":
    main()