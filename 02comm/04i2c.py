import smbus
bus = smbus.SMBus(1)

address = 0x04

while True:
    value = eval(input("0=Led Off, 1=Led On, 3=Get Count > "))
    if value < 2:
        bus.write_byte(address, value)
        print("Led ", value)
        continue
    else:
        number = bus.read_byte(address)
        print("Arduino LED Count", number)
