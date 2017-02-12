
from socket import  *

socket = socket(AF_INET, SOCK_STREAM)
socket.connect( ('', 1234))

read = socket.recv(1024)
print 'server:', read

while True:
    str = raw_input(">")
    if str == "exit":
        break
    read = socket.recv(1024)
    print 'server:', read
    socket.send(str+"\n")
    
socket.close()



