from flask import Flask, request, redirect
import RPi.GPIO as GPIO

PIN_LED = 18
app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_LED, GPIO.OUT)

@app.route('/')
def main():
    #return app.send_static_file('led_form.html')
    return app.send_static_file('led_ajax.html')


@app.route('/led/<cmd>')
def op(cmd):
    if cmd == "on":
        GPIO.output(PIN_LED, True)
        print("led on") 
        return "LED On"
    elif cmd == 'off':
        GPIO.output(PIN_LED, False)
        return 'LED Off'

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=8080, debug=True)
    finally:
        print('cleaning up')
        GPIO.cleanup()
