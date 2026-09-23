import cv2 as cv
import numpy as np

blank=np.zeros((500,500,3),dtype='uint8') 
# cv.imshow('Blank',blank)

#painting onblank image
# blank[:]=255,255,255
# cv.imshow('color',blank)

#draw a rectangle and circle
cv.rectangle(blank,(127,127),(250,250),(0,0,255),thickness=cv.FILLED)
cv.circle(blank,(188,90),40,(0,255,0),thickness=-1)
cv.rectangle(blank,(150,250),(180,350),(0,0,255),thickness=-1)
cv.rectangle(blank,(200,250),(230,350),(0,0,255),thickness=-1)
cv.line(blank, (127, 160), (80, 210), (0, 0, 255), 20)
cv.line(blank, (250, 160), (297, 210), (0, 0, 255), 20)
cv.imshow('rectangle',blank)

# img=cv.imread('photos/cat2.jpg')
# cv.imshow('Cat',img)

cv.waitKey(0)