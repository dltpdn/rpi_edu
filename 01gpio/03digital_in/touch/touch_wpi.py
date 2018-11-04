import wiringpi as wpi
PIN = 18

wpi.wiringPiSetupGpio()
wpi.pinMode(PIN, wpi.INPUT)

while True:
    read = wpi.digitalRead(PIN)
    if(read):
        print("touched")