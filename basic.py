import cv2 as cv

img=cv.imread("photos/astronaut.jpg")
cv.imshow("original",img)

#image convert to grayscale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray scale",gray)

#blurring an image
blur=cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
cv.imshow("Blurred image",blur)

#Edge cascade
canny=cv.Canny(blur,125,175)
cv.imshow("Edge detection",canny)

#Dilateing images
dilate=cv.dilate(canny,(3,3),iterations=3)
cv.imshow("Dilated image",dilate)

#Erroding images
erroded=cv.erode(dilate,(3,3),iterations=3)
cv.imshow("Erroded image",erroded)

#resizing images
resize=cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
cv.imshow("Resized image",resize)

#cropping image
cropped=img[50:200,200:400]
cv.imshow("Cropped image",cropped)

cv.waitKey(0)