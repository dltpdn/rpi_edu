import cv2
import cv2.cv as cv

cascade_xml = 'haarcascade_frontalface_default.xml'
cascade = cv2.CascadeClassifier(cascade_xml)

cam = cv2.VideoCapture(0)
cam.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 320)
cam.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 240)

while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    
    faces = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3, minSize=(80,80), flags=cv.CV_HAAR_SCALE_IMAGE)
    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255,0),2)
    cv2.imshow('facedetect', img)
    if 0xFF & cv2.waitKey(5) == 27:
        break
cv2.destroyAllWindows()

