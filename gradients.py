import cv2 as cv
import numpy as np

img=cv.imread("photos/astronaut.jpg")
cv.imshow("Original",img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)

#Laplacian
lap=cv.Laplacian(gray, cv.CV_64F)
lap=np.uint8(np.absolute(lap))
cv.imshow("Laplacian",lap)

#Sobel
sobelx=cv.Sobel(gray,cv.CV_64F,1,0)
sobely=cv.Sobel(gray,cv.CV_64F,0,1)
cv.imshow("Sobel_X",sobelx)
cv.imshow("Sobel_Y",sobely)
combined_sobel=cv.bitwise_or(sobelx,sobely)
cv.imshow("Sobel",combined_sobel)

#Canny
canny=cv.Canny(gray,150,175)
cv.imshow("Canny",canny)


cv.waitKey(0)