#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@Time    : 2018-06-22 08：23
@Author  : jianjun.wang
@Email   : alanwang6584@gmail.com

说明：目录处理的练习
"""

import os
import sys

def work_dir(file_dir):
	print'\n\n<><><><><><><><><><><><><><><><><><><><>><><> work dir <><><><><><><><><><><><><><><><><><><><><><><><>><>'
	for root, dirs, files in os.walk(file_dir):
		print'\n=========================================================='
		print "root : {0}".format(root)
		print "dirs : {0}".format(dirs)
		print "files : {0}".format(files)

		for file in files:
			try:
				print'------------------------------------------------------'

				file_name = os.path.splitext(file)[0]
				file_suffix = os.path.splitext(file)[1]
				file_path = os.path.join(root, file)
				file_abs_path = os.path.abspath(file)
				file_parent = os.path.dirname(file_path)

				print "file : {0}".format(file)
				print "file_name : {0}".format(file_name)
				print "file_suffix : {0}".format(file_suffix)
				print "file_path : {0}".format(file_path)
				print "file_abs_path : {0}".format(file_abs_path)
				print "file_parent : {0}".format(file_parent)
                
			except Exception, e:
				print "Exception", e


def list_dir(file_dir):
	'''
		通过 listdir 得到的是仅当前路径下的文件名，不包括子目录中的文件，如果需要得到所有文件需要递归
	'''
	print'\n\n<><><><><><><><><><><><><><><><><><><><><><><> listdir <><><><><><><><><><><><><><><><><><><><><><><><>><>'
	list_dir = os.listdir(file_dir) # 获取目录下的所有文件和目录（只访问一级）
	for cur_file in list_dir:
		# 获取文件的绝对路径
		path = os.path.join(file_dir, cur_file)
		if os.path.isfile(path): # 判断是否是文件还是目录需要用绝对路径
			print "{0} : is file!".format(cur_file)
		if os.path.isdir(path):
			print "{0} : is dir!".format(cur_file)


def handle_dir(file_dir):
	print file_dir
	if not file_dir.strip():
		print 'the dir path is null!\n'
		return

	# 判断文件或目录是否存在
	if not os.path.exists(file_dir): 
		print "the {0} is not exists!\n".format(file_dir)

		os.mkdir(file_dir) # 如果不存在创建目录，如果存在还调用该方法会抛 IOError
		print "{0} not exists! so create the dir!\n".format(file_dir)
		return

	# 判断是否是文件
	if os.path.isfile(file_dir):
		print("{0} is file!\n".format(file_dir))

	# 判断是否是目录
	if os.path.isdir(file_dir):
		print("{0} is dir!\n".format(file_dir))

		if file_dir.endswith('/'): # 去掉目录最后面的 '/'
			file_dir = file_dir.rstrip('/')

		list_dir(file_dir) 
		work_dir(file_dir)
	else:
		print("{0} is not dir!\n".format(file_dir))

def main():
	print 'arg num : ', len(sys.argv)
	print 'args : ', sys.argv
	print 'script name : ', sys.argv[0]

	for i in range(len(sys.argv)):
		print "arg[{0}] = {1}".format(i, sys.argv[i])

	if len(sys.argv) > 1:
		handle_dir(sys.argv[1])
	else:
		print 'Illegal arguments!\n'

if __name__ == "__main__":
    main()