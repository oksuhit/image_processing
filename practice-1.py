# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 11:22:10 2023

@author: Suhit
"""

import numpy as np
import cv2

def mouse_event(event,x,y,flags,param):
    print("events=",event)
    print("x=",x)
    print("y=",y)
    print("flags=",flags)
    print("param=",param)
    
    font = cv2.FONT_HERSHEY_PLAIN
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,",",y)
        
        cord = "."+str(x)+','+str(y)
        cv2.putText(img,cord,(x,y),font,1,(155,125,100),2)
        cv2.imshow('image',img)
    
    if event == cv2.EVENT_RBUTTONDOWN:
        b = img[y,x,0] #for blue channel is 0
        g = img[y,x,1] #for green channel is 1
        r = img[y,x,2] #for red channel is 2
        
        color_bgr = "."+str(b)+','+str(g)+','+str(r)
        cv2.putText(img,color_bgr,(x,y),font,1,(152,255,130),2)
        cv2.imshow('image',img)
        
cv2.namedWindow(winname = "res")

#img = np.zeros((600,600,3),np.uint8)
img = cv2.imread("D:\\images\\ironman.jpg")
img = cv2.resize(img,(900,600))
cv2.setMouseCallback("res",mouse_event)

while True:
    cv2.imshow("res",img)
    if cv2.waitKey(1) & 0xFF == 27: # press escape key
        break

cv2.destroyAllWindows()
