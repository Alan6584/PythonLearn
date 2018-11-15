#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@Time    : 2018-11-13 21：20
@Author  : jianjun.wang
@Email   : alanwang6584@gmail.com
"""

import numpy as np
import cv2 as cv
 
img = np.zeros((320, 320, 3), np.uint8) #生成一个空灰度图像
print img.shape # 输出：(320, 320, 3)



# 绘制一个红色椭圆
ptCenter = (160, 160) # 中心点位置
axesSize = (100, 45) # 长轴半径为 90，短轴半径为 60
rotateAngle = 90 # 旋转角度为 90
startAngle = 0
endAngle = 360

point_color = (0, 0, 255) # BGR
thickness = 1 
lineType = 4
cv.ellipse(img, ptCenter, axesSize, rotateAngle, startAngle, endAngle, point_color, thickness, lineType)



# 绘制一个绿色椭圆
ptCenter = (160, 160) # 中心点位置
axesSize = (90, 60) # 长轴半径为 90，短轴半径为 60
rotateAngle = 0 # 旋转角度为 0
startAngle = 0
endAngle = 360

point_color = (0, 255, 0) # BGR
thickness = 1 
lineType = 4
cv.ellipse(img, ptCenter, axesSize, rotateAngle, startAngle, endAngle, point_color, thickness, lineType)



# 绘制一个蓝色上半椭圆
ptCenter = (160, 60) # 中心点位置
axesSize = (100, 45) # 长轴半径为 90，短轴半径为 60
rotateAngle = 0 # 旋转角度为 90
startAngle = 180
endAngle = 360

point_color = (255, 0, 0) # BGR
thickness = 1 
lineType = 4
cv.ellipse(img, ptCenter, axesSize, rotateAngle, startAngle, endAngle, point_color, thickness, lineType)


cv.namedWindow("AlanWang")
cv.imshow('AlanWang', img)
cv.waitKey (10000) # 显示 10000 ms 即 10s 后消失
cv.destroyAllWindows()