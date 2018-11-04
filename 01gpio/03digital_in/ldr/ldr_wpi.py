import wiringpi as wpi
PIN = 18

wpi.wiringPiSetupGpio(); #wpi.setup('gpio');
wpi.pinMode(PIN, wpi.INPUT)


lastVal = -1
while True:
    val = wpi.digitalRead(PIN)
    if val != lastVal:
        print(val ==0 and 'dark' or 'light')
        lastVal = val
