import wiringpi as wpi
pin = 18

wpi.wiringPiSetupGpio()
wpi.pinMode(pin, wpi.INPUT)

val = -1;
while True:
    read = wpi.digitalRead(pin)
    if(read != val):
        val = read;
        print val == 0 and "no IR" or "IR detected"