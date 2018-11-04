import wiringpi as wpi

PIN_LED = 18
wpi.wiringPiSetupGpio()
wpi.pinMode(PIN_LED, wpi.OUTPUT)
while True:
    val = eval(input("1:on, 0:off > "))
    wpi.digitalWrite(PIN_LED, val)

