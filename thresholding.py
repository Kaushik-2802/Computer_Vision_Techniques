import cv2 as cv

img=cv.imread("photos/astronaut.jpg")
cv.imshow("Original",img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray Scale",gray)

#Simple Thresholding
threshold,thresh=cv.threshold(gray,120,255,cv.THRESH_BINARY)
cv.imshow("Threshold_img",thresh)

#Inverse threshold
threshold,thresh_inv=cv.threshold(gray,120,255,cv.THRESH_BINARY_INV)
cv.imshow("Inv_thresh",thresh_inv)

#Adaptive threshold
adaptive_threshold=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY_INV,11,7)
cv.imshow("Adaptive",adaptive_threshold)

cv.waitKey(0)