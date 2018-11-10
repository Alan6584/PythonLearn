#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@Time    : 2018-11-09 21：39
@Author  : jianjun.wang
@Email   : alanwang6584@gmail.com
"""

import numpy as np
import cv2 as cv
 
img = cv.imread('/Users/wangjianjun/Desktop/Debug/pics/aaa.jpeg', cv.IMREAD_UNCHANGED) # 按原始颜色格式读取图片
# img = cv.imread('/Users/wangjianjun/Desktop/Debug/pics/aaa.jpeg', cv.IMREAD_GRAYSCALE) # 按灰度图读取图片
print img.shape # 输出：(240, 240, 3)

cv.namedWindow("image")
cv.imshow('image', img)
cv.waitKey (0) # 如果没有这句显示后立马就消失了
cv.destroyAllWindows()