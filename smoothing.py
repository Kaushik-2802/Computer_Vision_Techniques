import cv2 as cv

img=cv.imread("photos/astronaut.jpg")
cv.imshow("Original image",img)

#Average blur
average=cv.blur(img,(7,7))
cv.imshow("Average blur",average)

#Gaussian blur
gauss=cv.GaussianBlur(img,(7,7),0)
cv.imshow("Gaussian blur",gauss)

#Median blur
median=cv.medianBlur(img,7)
cv.imshow("Median blur",median)

#Bilateral blur
bilateral=cv.bilateralFilter(img,5,15,15)
cv.imshow("Bilateral blur",bilateral)
cv.waitKey(0)