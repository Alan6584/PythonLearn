#! /usr/bin/python
# -*- coding: UTF-8 -*-

print "{:.2f}".format(3.1415926)
print "{:.2%}".format(0.25)


a = -3.12134
print a
print "{:.2f}".format(a)
print "{:+.2f}".format(a) # +号表示正数前显示+，负数前显示-
print "{: .2f}".format(a) #  空格表示在正数前加空格，负数前还是显示-

a = 3.12134
print a
print "{:.2f}".format(a)
print "{:+.2f}".format(a)
print "{: .2f}".format(a)



a = 6
print "{:0>3d}".format(a) # >表示右对齐，填充左边，数字补零，宽度为3
print "{:x<3d}".format(a) # >表示左对齐，填充右边，数字补x，宽度为3
print "{:x^3d}".format(a) # >表示居中对齐，宽度为3
print "{: ^3d}".format(a) # >表示居中对齐，宽度为3


a = 18
print "{:b}".format(a) #以二进制输出
print "{:d}".format(a) #以十进制输出
print "{:o}".format(a) #以八进制输出
print "{:x}".format(a) #以十六进制输出


# 可以使用{}转义大括号
print "{} 对应的位置是{{0}}, {}对应的位置是{{1}}".format("Hello", "Alan")
