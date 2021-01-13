import wiringpi as wpi, threading

fd = wpi.serialOpen("/dev/serial0", 115200)
running = True

def read_serial():
    while running:
        try:
            if wpi.serialDataAvail(fd) != -1 :
                ch = wpi.serialGetchar(fd)
                if ch== -1 :
                    continue
                ch = chr(ch)
                if ch == '\r':
                    ch = '\n'
                print(ch, end='')
        except:
            pass
    print("bye.")
    
try:
    t = threading.Thread(target=read_serial)
    t.start()
    print('serial is ready.')
    while True:
        line = input(">")
        if line == 'exit':
            break
        wpi.serialPrintf(fd,  (line + '\r\n'))
    print('closing.')
finally:
    running = False
    wpi.serialClose(fd)