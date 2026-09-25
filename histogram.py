import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img=cv.imread("photos/astronaut.jpg")
# cv.imshow("Original",img)

blank=np.zeros(img.shape[:2],dtype='uint8')

rectangle=cv.rectangle(blank,(img.shape[1]//2,img.shape[0]//2-200),(img.shape[1]//2+300,img.shape[0]//2),255,-1)


# gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow("Gray image",gray)

# masked_img=cv.bitwise_and(img,img,mask=rectangle)
# cv.imshow("Mask",masked_img)

# gray_hist=cv.calcHist([gray],[0],None,[256],[0,256])
# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

#color histogram
plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors=('b','g','r')
for (i,col) in enumerate(colors):
    hist=cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])

plt.show()



cv.waitKey(0)