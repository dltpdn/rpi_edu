import wiringpi as wpi

sw_pin = 18

wpi.wiringPiSetupGpio()
wpi.pinMode(sw_pin, wpi.INPUT)

while True:
    print wpi.digitalRead(sw_pin)