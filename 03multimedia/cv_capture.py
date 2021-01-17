import cv2

cam = cv2.VideoCapture(0)

while True:
    ret,img = cam.read()
    if ret:
        cv2.imshow('Video Capture', img)
        key = cv2.waitKey(10)
        if key==27:
            break
        if key== ord(' '):
            cv2.imwrite('capture.jpg', img)