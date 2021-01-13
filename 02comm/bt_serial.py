import serial, threading

port = serial.Serial("/dev/rfcomm0", baudrate=115200, timeout=3.0)

running = True
def read_serial():
    while running:
        try:
            ch = port.read().decode()
            if ch is not None and ch != '': # not timeout
                if ch == '\r':
                    ch = '\n'
                print(ch, end='')
        except:
            pass
    print("bye.")
    
try:
    if port.isOpen() :
        t = threading.Thread(target=read_serial)
        t.start()
        print('serial is ready.')
        while running:
            line = input(">")
            if line == 'exit':
                break
            port.write( (line + '\r\n').encode())
        print('closing...')
finally:
    running = False
    port.close()