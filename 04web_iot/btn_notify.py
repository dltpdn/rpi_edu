from flask import Flask, request, redirect
from flask_socketio import SocketIO, send
import RPi.GPIO as GPIO

app = Flask(__name__)
socketio = SocketIO(app,async_mode='threading')

GPIO.setmode(GPIO.BCM)
pin_btn = 23

GPIO.setup(pin_btn, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

@app.route('/')
def main():
    return app.send_static_file('btn_notify.html')

@socketio.on('connect')
def connect():
    print("client connected.")
    
def my_callback(channel):
    print('Edge detected on channel %s state %s'% (channel, GPIO.input(channel))) 
    val =GPIO.input(channel)
    if val == 1:
        socketio.emit('notify', '1')
    else:
        socketio.emit('notify', '0')

if __name__ == '__main__':
    try:
        GPIO.add_event_detect(pin_btn, GPIO.BOTH, callback=my_callback)
        socketio.run(app, host='0.0.0.0', port=8080, debug=True)
    finally:
        print('cleaning up')
        GPIO.cleanup()
