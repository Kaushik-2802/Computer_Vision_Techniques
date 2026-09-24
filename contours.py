import cv2 as cv
import numpy as np

img=cv.imread("photos/astronaut.jpg")
cv.imshow("original image",img)

blank=np.zeros(img.shape,dtype='uint8')
cv.imshow('blank',blank)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray image",gray)

blur=cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

canny=cv.Canny(blur,125,175)
cv.imshow("canny edges",canny)

ret,thresh=cv.threshold(canny,125,255,cv.THRESH_BINARY)
cv.imshow('Threshold img',thresh)

#Contours detection
contours,hierarchies=cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(len(contours))

cv.drawContours(blank,contours,-1,(0,0,255),1)
cv.imshow('drawn contours',blank)

cv.waitKey(0)