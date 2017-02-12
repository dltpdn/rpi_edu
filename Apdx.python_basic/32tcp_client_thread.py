
from socket import  *
import threading

running = True
def recv():
    while running:
        read = socket.recv(1024)
        print 'client:', read

try:
    socket = socket(AF_INET, SOCK_STREAM)
    socket.connect(('', 1234))
    th = threading.Thread(target=recv)
    th.start()
    socket.send('Hi! This is a client.')
    
    while running:
        str = raw_input(">")
        if str == "exit":
            break
        socket.send(str+"\n")
        
    socket.close()
finally:
    running = False
