import bluetooth as bt

socket = bt.BluetoothSocket( bt.RFCOMM )
print("scanning...")
scan_list = bt.discover_devices(lookup_names = True)
print(("found %d devices" % len(scan_list)))
for i, (addr, name) in enumerate(scan_list):
    print(( "%d: %s (%s)" % (i,addr, name)))
    
if len(scan_list) > 0 :
    idx = eval(input("device number you want to connect:"))
    address = scan_list[idx][0]
    #address = "B8:27:EB:14:18:CC"
    socket.connect((address, 3)) 
    print ("connected.")
    socket.send(b"Hello Bluetooth World.")
    print ("sent data")
    recv = socket.recv(1024)
    print(("recv data : %s" % recv.decode()))
    
    socket.close()