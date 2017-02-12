import wiringpi
import time

pin = 18
wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(pin, wiringpi.OUTPUT)

for i in range(0,5):
    wiringpi.digitalWrite(pin, True)
    print 'pin %s ON'%pin
    time.sleep(1)
    wiringpi.digitalWrite(pin, False)
    print 'pin %s Off'%pin
    time.sleep(1)



    