import cv2 as cv
import numpy as np

blank=np.zeros((400,400),dtype='uint8')

img1=cv.imread("photos/cat1.jpg")
img2=cv.imread("photos/cat2.jpg")

rectangle=cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)

circle=cv.circle(blank.copy(),(200,200),200,255,-1)

cv.imshow("Rectangle",rectangle)
cv.imshow("Circle",circle)

#bitwise AND
Bitwise_and=cv.bitwise_and(rectangle,circle)
cv.imshow("AND",Bitwise_and)

#bitwise OR
Bitwise_or=cv.bitwise_or(rectangle,circle)
cv.imshow('OR',Bitwise_or)

#bitwise NOT
Bitwise_not=cv.bitwise_not(rectangle)
cv.imshow('NOT',Bitwise_not)

#bitwise XOR
Bitwise_xor=cv.bitwise_xor(rectangle,circle)
cv.imshow('XOR',Bitwise_xor)
cv.waitKey(0)



