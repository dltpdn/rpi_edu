import wiringpi as wpi
pin = 18

wpi.wiringPiSetupGpio()
wpi.pinMode(pin, wpi.INPUT)

while True:
    read = wpi.digitalRead(pin)
    if(read):
        print "touched"