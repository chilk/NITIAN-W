#!/usr/bin/python2.6
# -*- coding: utf-8 -*-
#这是中文输入
import cv2
import numpy as np





#读图
frame = cv2.imread("hq.jpg")
#转变通道
hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

#取阀的范围
lower_blur=np.array([0,43,46])
upper_blur=np.array([10,255,255])

#二值图
thresh = cv2.inRange(hsv,lower_blur,upper_blur,cv2.THRESH_BINARY)


#显示图片
cv2.imshow('frame',frame)
cv2.imshow('thresh',thresh)

#找到thresh中的轮廓
a,cnt,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

#取最大轮廓
b = cnt[0]

#找到轮廓的半径和圆心坐标
(x,y),radius = cv2.minEnclosingCircle(b)

#将圆心坐标的值变成整数，并结合成一个元组
center = (int(x),int(y))

#将半径变成整数
radius = int(radius)
#画轮廓
img  = cv2.drawContours(frame,cnt,-3,(0,255,0),1)
print(x,y)
cv2.imshow('img',img)
#等待显示
k=cv2.waitKey(0)

cv2.destroyAllWindows()