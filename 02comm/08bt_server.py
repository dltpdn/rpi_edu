import bluetooth as bt

server = bt.BluetoothSocket( bt.RFCOMM )

server.bind(("", 3 ))
server.listen(1)


print "ready to connect..."
socket, address = server.accept()
print "client connected : ", address

data = socket.recv(1024)
print "received :%s" % data
socket.send('Good bye~')
print 'sent data'
socket.close()
server.close()