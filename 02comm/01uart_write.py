import serial

port = serial.Serial("/dev/serial0", baudrate=9600, timeout=3.0)
try:
    if port.isOpen():
        print('serial writer is ready.')
    
    while True:
        line = input(">")
        print( line)
        port.write( (line + '\r\n').encode())
finally:
    port.close()