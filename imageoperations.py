import cv2 #opencv use as cv2 in python

img1 = cv2.imread("D:\\avengers.jpg",1) #here "1" specifies color in BGR
#usualy we specify color in RGB, but here in python the image color is read in BGR
img1 = cv2.resize(img1,(1280,700))#width,height
print("original image ==",img1)
cv2.imshow("original",img1) #window showing img with "original" as tab name


#cv2.IMREAD_GRAYSCALE:Loads image in grayscale mode
img2 = cv2.imread("D:\\avengers.jpg",0) #here "0" specifies color in gray scale
img2 = cv2.resize(img2,(1280,700))#width,height
cv2.imshow("gray scale image",img2) #window showing img with "gray scale image" as tab name
print("image in gray scale==\n",img2)

#in console window you can see the "original" image is 3D, wich is why its array is for 3 bracket.
#where as "image in gray scale==" is gray scale i.e it is either dark or light,which is why only one braket used.

#cv2.IMREAD_UNCHANGED: loads image as such including alpha channel
img3 = cv2.imread("D:\\avengers.jpg",-1) #here "-1" specifies more saturation of the image i.e it is includes more alpha channel.
img3 = cv2.resize(img3,(1280,700))#width,height
cv2.imshow("more saturation",img3)
print("image with more saturation==\n",img3)


cv2.waitKey() #waitKey() controls visualization
#in bracket() if we specify 0, it will hold for zero sec
#in bracket if we specify 3000, it will hold for 3 sec
#i.e it is specified in mili sec. (3000 msec= 3 sec) 
cv2.destroyAllWindows()
