import cv2 as cv

img=cv.imread("photos/astronaut.jpg")
cv.imshow("Original image",img)

cv.waitKey(0)