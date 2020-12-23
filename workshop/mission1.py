'''
Created on Oct 21, 2016

@author: rainer
Mission example for Samsung Eletronics Raspberry-Pi Education
 
'''

import RPi.GPIO as GPIO 
import time
import pygame
import picamera

PIR_PIN = 18
SERVO_PIN  = 25
trig_pin = 24
echo_pin = 23 
    
sound_file = "sample.mp3"
camera_distance = 5

status = { "PIR": -1, "SND": False, "PHT": False, 'MODE':0}
#mode  0:init, 1:motion, 2: scanning, 3:taking photo
def main():
    global status
    delay = 3
    print('Mission-1 started.(delay time: %d)' %delay)
    for x in range(delay, 0, -1):
        time.sleep(1)
        print('Waiting.. ', x)
    try:    
        setup()
        while True:
            if status['MODE'] == 0:
                if check_pir(status): 
                    status['MODE'] = 1
                    if not(status['SND']):
                        play_sound(status)
                    scan_sonic(status)
                else: 
                    if status['MODE'] !=0 :
                        status['MODE'] =0
                        if status['SND']:
                            stop_sound(status)
    finally:
        GPIO.cleanup()

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIR_PIN, GPIO.IN)
    GPIO.setup(SERVO_PIN, GPIO.OUT)
    GPIO.setup(trig_pin, GPIO.OUT)
    GPIO.setup(echo_pin, GPIO.IN)


def get_distance():
    distance = 0
    puls = 0
    start_time = 0   
    GPIO.output(trig_pin, False)
    #print "waiting for sensor to settle."
    time.sleep(0.2)
    #time.sleep(2)
    GPIO.output(trig_pin, True)
    #time.sleep(20.0/1000.0)
    time.sleep(0.00001)
    GPIO.output(trig_pin, False)
    while GPIO.input(echo_pin) == 0:
        start_time = time.time()
    while GPIO.input(echo_pin) == 1:
        end_time = time.time()
    travel_time = end_time - start_time;
    #print travel_time
   # distance = travel_time / 58
    distance = travel_time * 17150
    distance = round(distance, 2)
    print('Distance:%dcm' %distance)
    return distance
    
def scan_sonic(status):
    status['MODE'] = 2
    p = GPIO.PWM(SERVO_PIN,100)
    degree = 15;
    gap = 0.55 #1degree : 0.1111
    direction = True;
    p.start(degree)
    with picamera.PiCamera() as camera:
        camera.start_preview()
        while True:
            if direction == True:
                if degree < 25:
                    degree += gap
                else :
                    degree = 25 - gap
                    direction = False
            else:
                if degree > 5:
                    degree -= gap
                else:
                    degree = 5 + gap
                    direction = True
            p.ChangeDutyCycle(degree)
            if get_distance() <= camera_distance:
                if status['SND']:
                   stop_sound(status)
                now_str = time.strftime("%Y%m%d-%H%M%S")
                camera.capture('./photo%s.jpg' %now_str)
                time.sleep(5)  #show the photo that was taken just before
                status['MODE'] = 0
                break

            if status['MODE'] !=2 :
                break;
            #time.sleep(0.5)
        camera.stop_preview()
        p.stop()
def take_photo(status):
    with picamera.PiCamera() as camera:
        camera.start_preview()
        now_str = time.strftime("%Y%m%d-%H%M%S")
        camera.capture('./photo%s.jpg' %now_str)
        status['MODE'] = 3
        time.sleep(5)
        #camera.stop_preview()


def check_pir(status):
    read = GPIO.input(PIR_PIN)
    if status['PIR'] != read: 
        status['PIR'] = read
        if status['PIR']== 0:
            print(time.strftime("%Y%m%d-%H%M%S"), "No intruder")
        elif status['PIR'] == 1:
            print(time.strftime("%Y%m%d-%H%M%S"), "Intruder dectected")
    return status['PIR']      


def play_sound(status):
    pygame.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()
    status['SND'] = True

def stop_sound(staus):
    pygame.mixer.music.pause()
    status['SND'] = False

  
if __name__ == '__main__':
    main()
    pass