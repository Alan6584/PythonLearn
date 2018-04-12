#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@Time    : 2018-04-11 19：26
@Author  : jianjun.wang
@Email   : alanwang6584@gmail.com
"""

import sys
import getopt

def main(args):
    file=''
    country=''
    version=''

    """
        语法格式：
        options, args = getopt.getopt(args, shortopts, longopts=[])

        参数含义：
        args：要解析的命令行参数列表，sys.argv[1:]，过滤掉 sys.argv[0]，它是执行脚本的名字，不算命令行参数
        shortopts：短格式参数串。shortopts 后的冒号(:)表示如果设置该选项，必须有附加的参数，不带冒号表示该选项没有附加参数
                如："hf:v:"
                h 后面没有冒号，表示该选项没有附加参数，如用于输出命令用法
                f 和 v 后面带有冒号，表示该选项有附加参数
        longopts：长格式参数列表。longopts 后的等号(=)表示如果设置该选项，必须有附加的参数，否则就没有附加参数
                如：["help", "file=", "version="]
                help 后面没有等号，表示该选项没有附加参数
                file 和 version 后面带冒号，表示如果设置该选项，必须有附加参数

        返回值含义：
        options：元组列表，每个元组的形式为：(选项, 附加参数)，如：('-f', 'data.csv')
        args：包含那些没有 '-' 或 '--' 的参数列表

        异常: 
        getopt.GetoptError：在没有找到参数列表，或选项的需要的参数为空时会触发该异常
        异常的参数是一个字符串，表示错误的原因，属性 msg 和 opt 为相关选项的错误信息

    """
    try:
        options, args = getopt.getopt(args, "hf:c:v:", ["help", "file=", "country=", "version="])
    except getopt.GetoptError:
        print 'Error: get_args.py -f <file> -c <country> -v <version>'
        print '   or: get_args.py --file=<file> --country=<country> --version=<version>'
        sys.exit(2)

    for opt, arg in options:
        if opt in ("-h", "--help"):
            print 'get_args.py -f <file> -c <country> -v <version>'
            print 'or: get_args.py --file=<file> --country=<country> --version=<version>'
            sys.exit()
        elif opt in ("-f", "--file"):
            file = arg
        elif opt in ("-c", "--country"):
            country = arg
        elif opt in ("-v", "--version"):
            version = arg

    for i in range(0, len(args)):
        print "args[{0}] = {1}".format(i, args[i])

    print 'file : ', file
    print 'country : ', country
    print 'version : ', version



if __name__ == "__main__":
	# 注意这里要排除 argv[0]，它是本脚本名，不算做命令行参数
    main(sys.argv[1:]) 