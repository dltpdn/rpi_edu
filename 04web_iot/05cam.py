from flask import Flask, redirect, request
import cv2
import base64

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

cam = cv2.VideoCapture(0)
cam.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 320)
cam.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 240)

@app.route('/')
def main():
    return redirect('/static/cam.html')

@app.route('/cctv')
def oncctv():
    print 'cctv'
    ret, data = cam.read()
    if ret:
        ret, png = cv2.imencode('.png', data)
        b64 = base64.encodestring(png)
        return b64
    return 'camera is not ready.'
    
    
if __name__ == '__main__':
    app.run(host="0.0.0.0")
