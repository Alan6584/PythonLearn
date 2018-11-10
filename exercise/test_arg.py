#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@Time    : 2018-11-09 21：39
@Author  : jianjun.wang
@Email   : alanwang6584@gmail.com
"""

import sys
import getopt

def main(args):
    file=''
    country=''
    version=''

    try:
        options, args = getopt.getopt(args, "hf:", ["help", "file="])
    except getopt.GetoptError:
        print 'Error: cv_readimage.py -f <file> '
        print '   or: cv_readimage.py --file=<file>'
        sys.exit(2)

    for opt, arg in options:
        if opt in ("-h", "--help"):
            print 'cv_readimage.py -f <file>'
            print 'or: cv_readimage.py --file=<file>'
            sys.exit()
        elif opt in ("-f", "--file"):
            file = arg

    for i in range(0, len(args)):
        print "args[{0}] = {1}".format(i, args[i])

    print 'file : ', file



if __name__ == "__main__":
	# 注意这里要排除 argv[0]，它是本脚本名，不算做命令行参数
    main(sys.argv[1:]) 