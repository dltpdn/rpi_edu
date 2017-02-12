from flask import Flask, request, redirect
import RPi.GPIO as GPIO
import Adafruit_DHT, json, time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

GPIO.setmode(GPIO.BCM)
sensor = Adafruit_DHT.DHT11
pin_dht11 = 24

@app.route('/')
def main():
    return redirect('/static/dht11.html')

@app.route('/monitor')
def monitoring():
    try:
        print '/monitor'
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin_dht11)
        obj = {'humi' : humidity, 'temp' : temperature}
        return json.dumps(obj)
    except Exception as e:
        print 'err', e


if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0')
    finally:
        print 'cleaning up'
        GPIO.cleanup()