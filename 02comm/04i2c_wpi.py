import wiringpi as wpi

address = 0x04
fd = wpi.wiringPiI2CSetup(address)
while True:
    value = eval(input("0=Led Off, 1=Led On, 3=Get Count > "))
    if value < 2:
        wpi.wiringPiI2CWrite(fd, value)
        print("Led ", value)
        continue
    else:
        number = wpi.wiringPiI2CRead(fd)
        print("Arduino LED Count", number)
