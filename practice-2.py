# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 09:26:34 2023

@author: Suhit
"""

import cv2

#enter address and name form the user
path = input("enter the address and name of the jpg image:")

#original image
img1 = cv2.imread(path,1)
img1 = cv2.resize(img1,(900,700))
print("original image",img1)
cv2.imshow("original image",img1)

#gray scale image
img2 = cv2.imread(path,0)
img2 = cv2.resize(img2,(900,700))
print("gray scale image",img2)
cv2.imshow("gray scale image",img2)

#to save image
k = cv2.waitKey()
if k == ord("s"):
    cv2.imwrite("D:\images\ironman_gray.jpg",img2)
    cv2.destroyAllWindows()
else:
    cv2.destroyAllWindows()
    