from flask import Flask, redirect, request
import cv2
import base64

app = Flask(__name__)

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 320)

@app.route('/')
def main():
    return app.send_static_file('cam.html')

@app.route('/cam')
def oncam():
    ret, data = cam.read()
    if ret:
        ret, png = cv2.imencode('.png', data)
        b64 = base64.encodestring(png.ravel())
        return b64
    else:
        return 'camera is not ready.'
    
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
