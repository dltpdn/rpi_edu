import wiringpi as wpi
pin = 18

wpi.wiringPiSetupGpio(); #wpi.setup('gpio');
wpi.pinMode(pin, wpi.INPUT)


lastVal = -1
while True:
    val = wpi.digitalRead(pin)
    if val != lastVal:
        print val ==0 and 'dark' or 'light'
        lastVal = val
