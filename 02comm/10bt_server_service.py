import bluetooth as bt

server = bt.BluetoothSocket( bt.RFCOMM )

server.bind(("", bt.PORT_ANY ))
server.listen(1)

bt.advertise_service(server, "MyService",
                     service_classes=[bt.SERIAL_PORT_CLASS],
                     profiles=[bt.SERIAL_PORT_PROFILE])

print "ready to connect..."
socket, address = server.accept()
print "client connected : ", address

data = socket.recv(1024)
print "received :%s" % data
socket.send('Good bye~')
print 'sent data'
socket.close()
server.close()