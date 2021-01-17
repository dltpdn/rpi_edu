from flask import *
import RPi.GPIO as GPIO
import Adafruit_DHT, json, time

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
sensor = Adafruit_DHT.DHT11
pin_dht11 = 24

@app.route('/')
def main():
    #return app.send_static_file('dht11.html')
    return app.send_static_file('dht11_gauge.html')

@app.route('/monitor')
def monitoring():
    try:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin_dht11)
        obj = {'humi' : humidity, 'temp' : temperature}
        return Response(json.dumps(obj), content_type='application/json')
    except Exception as e:
        print('err', e)


if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=8080, debug=True)
    finally:
        GPIO.cleanup()
        print('cleaning up')