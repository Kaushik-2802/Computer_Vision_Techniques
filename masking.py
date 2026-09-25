import cv2 as cv
import numpy as np


img=cv.imread("photos/astronaut.jpg")
cv.imshow("original",img)

blank=np.zeros(img.shape[:2],dtype='uint8')
cv.imshow("Blank",blank)

rectangle=cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle=cv.circle(blank.copy(),(200,200),200,255,-1)

mask=cv.bitwise_and(rectangle,circle)

#Masking this combo onto image
masked=cv.bitwise_and(img,img,mask=mask)
cv.imshow("Masked image",masked)

cv.waitKey(0)