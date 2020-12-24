import wiringpi as wpi

PIN = 18
wpi.wiringPiSetupGpio()
wpi.pinMode(PIN, wpi.OUTPUT)
print(f'#{PIN} is set to OUTPUT.')
try:
    while True:
        val = input("1:on, 0:off > ")
        if val == '0':
            wpi.digitalWrite(PIN, wpi.LOW)
            print('On')
        elif val == '1':
            wpi.digitalWrite(PIN, wpi.HIGH)
            print('Off')
        else:
            break
finally:
    wpi.digitalWrite(PIN, wpi.LOW)
    wpi.pinMode(PIN, wpi.INPUT)
    print('cleanup and exit')

