import serial

port = serial.Serial("/dev/serial0", baudrate=9600, timeout=3.0)


def readline():
    line = ''
    while True:
        ch = port.read().decode()
        if ch =='\n' or ch == '\r' or ch == '':
            if len(line) > 0 :
                return line
        else:
            line +=ch
    
try:
    if port.isOpen() :
        print('serial is ready.')
        while True:
            print("recv:" + readline()) 
finally:
    port.close()