from  socket import *

sock = socket(AF_INET, SOCK_STREAM)
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sock.bind(('', 8080))
sock.listen(1)
print 'server listening on 8080...'
while True:
    conn, addr = sock.accept()
    req = ''
    while True:
        req += conn.recv(1024)
        if req.endswith('\r\n\r\n'):
            req_line = req.split('\r\n')[0]
            print req_line
            method, url, ver = req_line.split()
            print url
            break
    conn.send("HTTP/1.1 200 OK\nContent-Type:text/html\n\n<h1>Welocome to My server</h1>\n")
    conn.close()
sock.close()      
      