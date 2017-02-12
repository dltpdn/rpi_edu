from flask import Flask, request, redirect
import RPi.GPIO as GPIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

GPIO.setmode(GPIO.BCM)
pin_led = 18

GPIO.setup(pin_led, GPIO.OUT)

@app.route('/')
def main():
    return redirect('/static/led.html')


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

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0')
    finally:
        print 'cleaning up'
        GPIO.cleanup()
