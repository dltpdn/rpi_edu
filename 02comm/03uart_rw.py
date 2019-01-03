import serial, threading

port = serial.Serial("/dev/serial0", baudrate=9600, timeout=3.0)

class ReadThread(threading.Thread):
    flag = True
    
    def run(self):
        while self.flag:
            line = self.readline()
            print("recv:" +line)
        print("read thread died.")
        
    
    def readline(self):
        line = ''
        while True:
            ch = port.read().decode()
            if ch =='\r' or ch=='\n' or ch == '':
                if len(line) > 0 :
                    return line
            else:
                line +=ch
    
try:
    if port.isOpen() :
        t = ReadThread()
        t.start()
        print('serial is ready.')
        while True:
            line = input(">")
            if line == 'exit':
                t.flag = False
                break
            print(line)
            port.write( (line + '\r\n').encode())
        print('bye')
finally:
    port.close()