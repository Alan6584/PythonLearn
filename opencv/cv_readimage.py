#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@Time    : 2018-11-09 21：39
@Author  : jianjun.wang
@Email   : alanwang6584@gmail.com
"""


import numpy as np
import cv2
 
# img = cv2.imread('/Users/wangjianjun/Desktop/Debug/pics/aaa.jpeg', cv2.IMREAD_UNCHANGED) # 按原始颜色格式读取图片
img = cv2.imread('/Users/wangjianjun/Desktop/Debug/pics/aaa.jpeg', cv2.IMREAD_GRAYSCALE) # 按灰度图读取图片
print img.shape

cv2.namedWindow("image")
cv2.imshow('image', img)
cv2.waitKey (0)
cv2.destroyAllWindows()