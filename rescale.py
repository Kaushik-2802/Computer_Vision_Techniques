import cv2 as cv
def rescaleFrame(frame,scale=0.5):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

vid=cv.VideoCapture(0)
if not vid.isOpened():
    print("Error: cannot open web cam")
    exit()

while True:
    ret,frame=vid.read()
    resized_frame=rescaleFrame(frame)
    if not ret:
        print("Cannot recieve frame")
        break
    # cv.imshow('Web Cam feed',frame)
    cv.imshow('Resized frame',resized_frame)
    if cv.waitKey(1) & 0xFF==ord('d'):
          break