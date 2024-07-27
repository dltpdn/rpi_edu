from flask import Flask, Response
import cv2
import time

app = Flask(__name__)
header = 'multipart/x-mixed-replace; boundary=mjpg'
cap = None

@app.route('/')
def main():
    return app.send_static_file('cam.html')
    
@app.route('/cam_mjpg')
def oncam():
    global cap
    if cap == None:
        cap = cv2.VideoCapture(0)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
    def gen():
        ret, data = cap.read()
        while ret:
            ret, data = cap.read()
            ret, jpg = cv2.imencode('.jpg', data)
            jpg_str = jpg.tobytes()
            res_str = b"--mjpg\r\n"
            res_str += b"Content-Tpe: image/jpegbase64\r\n"
            res_str += b"Content-length: " + f'{len(jpg_str)}'.encode()
            res_str += b"\r\n\r\n"
            res_str += jpg_str
            res_str += b"\r\n"
            yield res_str
            time.sleep(0.05)
    return Response(gen(), mimetype=header)
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
