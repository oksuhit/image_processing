# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 13:57:33 2023

@author: Suhit
"""


#building color picker using track balls

import cv2
import numpy as np

def cross(x):
    pass

#create a blank image
img = np.ones((600,600,3),np.uint8)
cv2.namedWindow("color picker")

#create switch for on and off the trackbar
s1 = '0:OFF\n 1:ON'
cv2.createTrackbar(s1,"color picker",0,255,cross)

#create trackbar for adjusting color
cv2.createTrackbar("B","color picker",0,255,cross)
cv2.createTrackbar("G","color picker",0,255,cross)
cv2.createTrackbar("R","color picker",0,255,cross)

#logic for handeling trackbar
while True:
    cv2.imshow("color picker",img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    
    #set position for bars
    s = cv2.getTrackbarPos(s1,"color picker")
    r = cv2.getTrackbarPos("B","color picker")
    g = cv2.getTrackbarPos("G","color picker")
    b = cv2.getTrackbarPos("R","color picker")
    
    if s == 0:
        img[:] = 0
    else:
        img[:] = [r,g,b]
        
cv2.destroyAllWindows()