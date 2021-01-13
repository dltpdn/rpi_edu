import serial, threading

port = serial.Serial("/dev/serial0", baudrate=115200, timeout=3.0)

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
    if port.isOpen():
        print('serial writer is ready.')
    t = threading.Thread(target=read_serial)
    t.start()
    while running:
        line = input("1:On, 0:Off, 9:quit >")
        if line == '9':
            break
        port.write(line.encode())
finally:
    running = False
    port.close()