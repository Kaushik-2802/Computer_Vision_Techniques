import cv2 as cv

# img=cv.imread('photos/cat1.jpg') #imread() function is used for reading images and convert them into matrix
# print(img)
# cv.imshow('cat1',img) #imshow() function is used for displaying images in a new window it accepts (original_img,matrix_img)
# cv.waitKey(0)


#CODE FOR RECORDING FROM THE COMPUTER WEB CAM
vid=cv.VideoCapture(0)
if not vid.isOpened():
    print("Error: cannot open web cam")
    exit()

while True:
    ret,frame=vid.read()
    if not ret:
        print("Cannot recieve frame")
        break
    cv.imshow('Web Cam feed',frame)
    cv.waitKey(1)

