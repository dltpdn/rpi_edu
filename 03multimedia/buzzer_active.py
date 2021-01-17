import wiringpi as wpi

PIN_BZR = 18
PIN_BTN = 23

wpi.wiringPiSetupGpio()
wpi.pinMode(PIN_BZR, wpi.OUTPUT)
wpi.pinMode(PIN_BTN, wpi.INPUT)
wpi.pullUpDnControl(PIN_BTN, wpi.PUD_UP)

try:
    while True:
        val = wpi.digitalRead(PIN_BTN)
        wpi.digitalWrite(PIN_BZR, not val)
finally:
    wpi.pinMode(PIN_BZR, wpi.INPUT)