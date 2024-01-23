# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 10:24:29 2023

@author: Suhit
"""
import cv2

#original image
img1 = cv2.imread("D:\images\ironman1.jpg")
img1 = cv2.resize(img1,(900,700))
print("original image",img1)
cv2.imshow("original image",img1)

#gray scale image
img2 = cv2.imread("D:\images\ironman1.jpg",0)
img2 = cv2.resize(img2,(900,700))
print("gray scale image",img2)
cv2.imshow("gray scale image",img2)

#to save image
k = cv2.waitKey()
if k == ord("s"):
    cv2.imwrite("D:\images\ironman_gray1.jpg",img2)
    cv2.destroyAllWindows()
else:
    cv2.destroyAllWindows()