import bluetooth as bt

socket = bt.BluetoothSocket( bt.RFCOMM )
address = "B8:27:EB:AD:74:74" #You should change this to your target address
#address = "B8:27:EB:14:18:CC"
socket.connect((address, 3)) 
print "connected."
socket.send("Hello Bluetooth World.")
print "sent data"
recv = socket.recv(1024)
print "recv data : %s" % recv

socket.close()