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

import requests
from lxml import etree


def get_data():
	url = "https://movie.douban.com/subject/26861685/comments"
	# r = requests.get(url).text.encode('utf8','ignore')
	res = requests.get(url)
	res.encoding='utf-8'
	r = res.text

	# /html/body/div[6]/div[1]/div[2]/ul/li[1]/div/a
	# /html/body/div[6]/div[1]/div[2]/ul/li[2]/div/a

	# /html/body/div[6]/div[1]/div[2]/ul/li[2]/div


	# print r
	s = etree.HTML(r)


	# print s.xpath("//*[@id="comments"]/div[1]/div[2]/p/test()")
	# print s.xpath('//*[@id="comments"]/div[14]/div[2]/p/text()')

	print(s.xpath('//*[@id="comments"]/div[14]/div[2]/p/text()'))




	'''
	for i in xrange(1,20):
		xxpath = "/html/body/div[6]/div[1]/div[2]/ul/li[{0}]/div/a".format(i)
		print xxpath

		href = xxpath + "/@href"
		print href
		print s.xpath(href)

		title = xxpath + "/@title"
		print title
		print s.xpath(title)
	'''


def main():


	print 'arg num : ', len(sys.argv)
	print 'args : ', sys.argv
	print 'script name : ', sys.argv[0]

	for i in range(len(sys.argv)):
		print "arg[{0}] = {1}".format(i, sys.argv[i])

	#将输出重定向到txt文件
	output = sys.stdout
	outputfile = codecs.open("/Users/wangjianjun/Alan/me/audio/data/story.txt", 'w', encoding='utf-8')
	sys.stdout = outputfile

	get_data()

	outputfile.close()
	sys.stdout = output

	print "finish!!!"


if __name__ == "__main__":
    main()