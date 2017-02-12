import serial

port = serial.Serial("/dev/ttyS0", baudrate=115200, timeout=3.0)


def readline():
    line = ''
    while True:
        ch = port.read()
        line +=ch
        if ch =='\n' or ch == '':
            if len(line) > 0 :
                return line
    
try:
    if port.isOpen() :
        print 'serial is ready.'
        while True:
            print "recv:" + readline() 
finally:
    port.close()