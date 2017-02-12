import serial, threading

port = serial.Serial("/dev/ttyS0", baudrate=115200, timeout=3.0)

class ReadThread(threading.Thread):
    flag = True
    
    def run(self):
        while self.flag:
            line = self.readline()
            if len(line) > 0 :
                print "recv:" +line
        print "read thread died."
        
    
    def readline(self):
        line = ''
        while True:
            ch = port.read()
            line +=ch
            if ch =='\r' or ch == '':
                return line
    
try:
    if port.isOpen() :
        t = ReadThread()
        t.start()
        print 'serial is ready.'
        while True:
            line = raw_input(">")
            if line == 'exit':
                t.flag = False
                break
            print line
            port.write(line + '\r\n')
        print 'bye'
finally:
    port.close()