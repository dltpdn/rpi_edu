from flask import Flask, request, redirect
import RPi.GPIO as GPIO
from flask_socketio import SocketIO, send
import Adafruit_DHT, json, time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app,async_mode='threading')

pin_led = 18
pin_btn = 23
pin_dht11 = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_led, GPIO.OUT)
GPIO.setup(pin_btn, GPIO.IN)
sensor = Adafruit_DHT.DHT11

@app.route('/')
def main():
    return redirect('/static/web_iot.html')


@app.route('/operate/<cmd>')
def op(cmd):
    val = request.values['val']   
    if cmd == "led":
        val = request.values['val']   
        print '/operate/', cmd, val 
        if val == 'on':
            GPIO.output(pin_led, True)
            print pin_led, 'on'
        elif val == 'off':
            GPIO.output(pin_led, False)
        return 'OK'


@app.route('/monitor')
def monitoring():
    try:
        print '/monitor'
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin_dht11)
        obj = {'humi' : humidity, 'temp' : temperature}
        print obj
        return json.dumps(obj)
    except Exception as e:
        print 'err', e


@socketio.on('connect')
def connect():
    send({'data': 'welcome'})
    
def my_callback(channel):
    print 'Edge detected on channel %s state %s'% (channel, GPIO.input(channel)) 
    val =GPIO.input(channel)
    if val == 1:
        socketio.send( {'data': '1' })
    else:
        socketio.send({'data': '0'})
    print 'btn pressed', 0

if __name__ == '__main__':
    try:
        GPIO.add_event_detect(pin_btn, GPIO.BOTH, callback=my_callback)
        socketio.run(app, host='0.0.0.0')
    finally:
        print 'cleaning up'
        GPIO.cleanup()
