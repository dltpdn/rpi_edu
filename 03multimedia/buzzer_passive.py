import wiringpi  
from time import sleep  
PIN_BUZ = 18

wiringpi.wiringPiSetupGpio()  
  
try:
    wiringpi.softToneCreate(PIN_BUZ)
    while True:
        wiringpi.softToneWrite(PIN_BUZ, 392)
        sleep(0.5)
        wiringpi.softToneWrite(PIN_BUZ, 523)
        sleep(0.5)
finally:
    wiringpi.pinMode(PIN_BUZ, 0)
