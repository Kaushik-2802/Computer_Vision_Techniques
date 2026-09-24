import cv2 as cv
# import matplotlib.pyplot as plt

img=cv.imread("photos/astronaut.jpg")
cv.imshow("Original image",img)

# plt.imshow(img)
# plt.show()

#BGR to Gray scale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray scale",gray)

#BGR to HSV
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("HSV",hsv)

#BGR to LAB
lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow("lab",lab)

#BGR to LUV
luv=cv.cvtColor(img,cv.COLOR_BGR2LUV)
cv.imshow("luv",luv)

xyz=cv.cvtColor(img,cv.COLOR_BGR2XYZ)
cv.imshow("xyz",xyz)

hsl=cv.cvtColor(img,cv.COLOR_BGR2HLS)
cv.imshow("rgba",hsl)

cv.waitKey(0)