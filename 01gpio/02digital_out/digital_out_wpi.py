import wiringpi as wpi

pin = 18
wpi.wiringPiSetupGpio()
wpi.pinMode(pin, wpi.OUTPUT)
while True:
    val = input("1:on, 0:off > ")
    wpi.digitalWrite(pin, val)

