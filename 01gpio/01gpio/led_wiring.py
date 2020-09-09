import wiringpi as wpi
import time

PIN_LED = 18
wpi.wiringPiSetupGpio()
wpi.pinMode(PIN_LED, wpi.OUTPUT)

for i in range(5):
    wpi.digitalWrite(PIN_LED, True)
    print( 'pin %s ON'%PIN_LED)
    time.sleep(1)
    wpi.digitalWrite(PIN_LED, False)
    print( 'pin %s Off'%PIN_LED)
    time.sleep(1)
wpi.digitalWrite(PIN_LED, False)
wpi.pinMode(PIN_LED, wpi.INPUT)



    