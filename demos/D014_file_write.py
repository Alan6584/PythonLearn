#! /usr/bin/python
# -*- coding:UTF-8 -*-

fp = open("./test/D014_file.txt", "wb")

fp.write("My name is Alan.\n")
fp.write("My email is alanwang6584@gmail.com\n")
str = "Hello Alan!\nWelcome Python!\n"
fp.writelines(str)

fp.close()
