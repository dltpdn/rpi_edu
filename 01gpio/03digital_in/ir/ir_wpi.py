import wiringpi as wpi
PIN = 18

wpi.wiringPiSetupGpio()
wpi.pinMode(PIN, wpi.INPUT)

val = -1;
while True:
    read = wpi.digitalRead(PIN)
    if(read != val):
        val = read;
        print(val == 0 and "no IR" or "IR detected")