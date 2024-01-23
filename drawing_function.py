# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 13:26:36 2023

@author: Suhit
"""

import numpy as np
import cv2
img1 = cv2.imread("D:\\images\\thanos.jpg")
img1 = cv2.resize(img1,(900,600))

#for black screen
img2 = np.zeros([500,500,3],np.uint8)*255 #uint8= unsigned intiger 8
cv2.imshow("black screen",img2)

#for white screen
img3 = np.ones([500,500,3],np.uint8)*255
cv2.imshow("white screen",img3)

#to draw straight line it accepts 5 parameters(img,starting,ending,color{format BGR},thickness)
# to select color, open browser=> search online picker =>note the values of BGR color you want.
img1 = cv2.line(img1,(0,0),(300,300),(9,9,235),8)
img1 = cv2.line(img1,(0,40),(250,300),(235,9,145),8)
img1 = cv2.line(img1,(40,0),(300,250),(235,122,9),8)
img1 = cv2.line(img1,(0,80),(200,300),(23,199,4),8)
img1 = cv2.line(img1,(80,0),(300,200),(2,126,242),8)
img1 = cv2.line(img1,(0,120),(170,305),(2,242,234),8)

#to draw arowed line
img1 = cv2.arrowedLine(img1,(600,600),(400,400),(9,9,235),8)
img1 = cv2.arrowedLine(img1,(600,640),(330,380),(235,9,145),8)
img1 = cv2.arrowedLine(img1,(640,600),(380,330),(235,122,9),8)
img1 = cv2.arrowedLine(img1,(600,680),(260,360),(23,199,4),8)
img1 = cv2.arrowedLine(img1,(680,600),(360,260),(2,126,242),8)
img1 = cv2.arrowedLine(img1,(560,720),(210,345),(2,242,234),8)

#to draw rectangle it accepts 5 parameters (img,start_co,end_co,color,thickness)
img1 = cv2.rectangle(img1,(10,380),(128,512),(88,196,193),-1)#-1 for filling the complete rectangle
img1 = cv2.rectangle(img1,(30,510),(128,60),(88,196,193),8)

#to draw circle it accepts(img,start_co,radius,color,thickness)
img1 = cv2.circle(img1,(100,400),40,(4,5,5),4)

#to put text (img,text,start_co,font,fontsize,color,thickness,linetype)
font = cv2.FONT_HERSHEY_COMPLEX
linetype = cv2.LINE_AA
img = cv2.putText(img1,"thanos",(450,500),font,4,(189,15,44),2,linetype)

#ellipse_accept(img,start_cor,(length,height),angle,color,thickness)
img1 = cv2.ellipse(img1,(100,450),(100,50),90,90,180,(56,38,21),6)
print("original image:",img1)
cv2.imshow("original image",img1)



#for white screen
cv2.waitKey(0)
cv2.destroyAllWindows()

