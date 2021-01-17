from flask import *
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
GPIO.setup(pin_btn, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
sensor = Adafruit_DHT.DHT11

@app.route('/')
def main():
    return redirect('/static/web_iot.html')


@app.route('/led/<cmd>')
def op(cmd):
    if cmd == "on":
        GPIO.output(pin_led, True)
        return 'Led On'
    elif cmd == 'off':
        GPIO.output(pin_led, False)
        return 'Led Off'


@app.route('/monitor')
def monitoring():
    try:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin_dht11)
        obj = {'humi' : humidity, 'temp' : temperature}
        return Response(json.dumps(obj), content_type='application/json')
    except Exception as e:
        print('err', e)


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
        socketio.run(app, host='0.0.0.0', port=8080)
    finally:
        print('cleaning up')
        GPIO.cleanup()
