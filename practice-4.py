# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 10:43:50 2023

@author: Suhit
"""

import cv2

#original image
img1 = cv2.imread("D:\\images\\thor.jpg")
img1 = cv2.resize(img1,(700,700))
print("original image",img1)
cv2.imshow("original image",img1)

#gray scale image
img2 = cv2.imread("D:\\images\\thor.jpg",0)
img2 = cv2.resize(img2,(400,400))
print("grayscale image",img2)
cv2.imshow("gray scale image",img2)

#fliping image
print(''' enter 0 = for rotating upside down.
enter 1 = for miror iamge of gray scale.
enter -1 = for upside down miror image of gray scale''')

a=int(input("enter the value for rotating the image:"))
img3 = cv2.flip(img2,a)
print("fliped image",img3)
cv2.imshow("fliped image",img3)


#saving the flipped gray scale image
k = cv2.waitKey()
if k==ord("s"):
    cv2.imwrite("D:\\images\\thor_flipped_gray.jpg",img3)
    cv2.destroyAllWindows()
else:
    cv2.destroyAllWindows()
