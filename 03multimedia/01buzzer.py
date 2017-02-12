import wiringpi  
from time import sleep  
pin = 18

wiringpi.wiringPiSetupGpio()  
  
try:
    wiringpi.softToneCreate(pin)
    while True:
        wiringpi.softToneWrite(pin, 392)
        sleep(0.5)
        wiringpi.softToneWrite(pin, 523)
        sleep(0.5)
finally:
    wiringpi.pinMode(pin, 0)
