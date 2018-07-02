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

def encode_utf8(string):
	return string.encode('utf-8')

def decode_utf8(string):
	return unicode(string, encoding='utf-8')


def get_data():
	url = "http://www.qbaobei.com/jiaoyu/tj/tjgs/List_2.html"
	res = requests.get(url)
	res.encoding='utf-8'
	r = res.text

	# print r
	s = etree.HTML(r)

	
	'''
	a_node = "//div[@class='channel-l']/div[2]/ul/li[{0}]/a".format(1)
	print(s.xpath(a_node + '/img/@alt')[0])
	print(s.xpath(a_node + '/@href')[0])
	print(s.xpath(a_node + '/img/@src')[0])
	'''


	for i in xrange(1,21):
		a_node = "//div[@class='channel-l']/div[2]/ul/li[{0}]/div[1]/a".format(i)
		title = s.xpath(a_node + '/text()')[0]
		link = s.xpath(a_node + '/@href')[0]
		print title, ",", link

		# print("1: {0}, {1}".format(title, link))


def save_story(file_path, url):
	pass
	


def main():


	print 'arg num : ', len(sys.argv)
	print 'args : ', sys.argv
	print 'script name : ', sys.argv[0]

	for i in range(len(sys.argv)):
		print "arg[{0}] = {1}".format(i, sys.argv[i])

	#将输出重定向到txt文件
	output = sys.stdout
	outputfile = codecs.open("/Users/wangjianjun/Alan/me/audio/data/storys/story.csv", 'w', encoding='utf-8')
	sys.stdout = outputfile

	print "story_name", ",", "story_link"
	get_data()

	outputfile.close()
	sys.stdout = output

	print "finish!!!"


if __name__ == "__main__":
    main()