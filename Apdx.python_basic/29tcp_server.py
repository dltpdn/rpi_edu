
from socket import  *

server = socket(AF_INET, SOCK_STREAM)
server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server.bind(('', 1234))
server.listen(1)
print "server listening on 1234..."
conn, addr = server.accept()

conn.send('Welcome to python tcp server.')
while True:
    str = raw_input(">")
    if str == "exit":
        break
    conn.send(str+"\n")
    read = conn.recv(1024)
    print 'client:', read
    
conn.close()

