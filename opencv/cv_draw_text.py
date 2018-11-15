#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@Time    : 2018-11-13 21：47
@Author  : jianjun.wang
@Email   : alanwang6584@gmail.com

 Font type. One of FONT_HERSHEY_SIMPLEX, FONT_HERSHEY_PLAIN, FONT_HERSHEY_DUPLEX, FONT_HERSHEY_COMPLEX, 
 FONT_HERSHEY_TRIPLEX, FONT_HERSHEY_COMPLEX_SMALL, FONT_HERSHEY_SCRIPT_SIMPLEX, 
 or FONT_HERSHEY_SCRIPT_COMPLEX, where each of the font ID’s can be combined with FONT_ITALIC 

"""

import numpy as np
import cv2 as cv
 
img = np.zeros((320, 320, 3), np.uint8) #生成一个空灰度图像
print img.shape # 输出：(320, 320, 3)


text = 'AlanWang4523'
org = (40, 80)
fontFace = cv.FONT_HERSHEY_COMPLEX
fontScale = 1
fontcolor = (0, 255, 0) # BGR
thickness = 1 
lineType = 4
bottomLeftOrigin = 1
# cv.putText(img, text, org, fontFace, fontScale, fontcolor, thickness, lineType, bottomLeftOrigin)
cv.putText(img, text, org, fontFace, fontScale, fontcolor, thickness, lineType)


text = 'https://blog.csdn.net/u011520181'
org = (10, 180)
fontFace = cv.FONT_HERSHEY_TRIPLEX
fontScale = 0.5
fontcolor = (0, 0, 255) # BGR
thickness = 1 
lineType = 4
bottomLeftOrigin = 1
cv.putText(img, text, org, fontFace, fontScale, fontcolor, thickness, lineType)


cv.namedWindow("image")
cv.imshow('image', img)
cv.waitKey (10000) # 显示 10000 ms 即 10s 后消失
cv.destroyAllWindows()