#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@Time    : 2018-11-13 21：03
@Author  : jianjun.wang
@Email   : alanwang6584@gmail.com
"""

import numpy as np
import cv2 as cv
 
img = np.zeros((320, 320, 3), np.uint8) #生成一个空灰度图像
print img.shape # 输出：(320, 320, 3)

# 矩形左上角和右上角的坐标，绘制一个绿色矩形
ptLeftTop = (60, 60)
ptRightBottom = (260, 260)
point_color = (0, 255, 0) # BGR
thickness = 1 
lineType = 4
cv.rectangle(img, ptLeftTop, ptRightBottom, point_color, thickness, lineType)

# 绘制一个红色矩形
ptLeftTop = (120, 100)
ptRightBottom = (200, 150)
point_color = (0, 0, 255) # BGR
thickness = 1
lineType = 8
cv.rectangle(img, ptLeftTop, ptRightBottom, point_color, thickness, lineType)

cv.namedWindow("AlanWang")
cv.imshow('AlanWang', img)
cv.waitKey (10000) # 显示 10000 ms 即 10s 后消失
cv.destroyAllWindows()