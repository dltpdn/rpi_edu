import smbus
bus = smbus.SMBus(1)

address = 0x04

def writeNumber(value):
    bus.write_byte(address, value)

def readNumber():
    number = bus.read_byte(address)
    return number

while True:
    var = input("0=Led Off, 1=Led On, 3=Get Count > ")
    if var < 2:
        writeNumber(var)
        print "Led ", var
        continue
    else:
        number = readNumber()
        print "Arduino LED Count", number
