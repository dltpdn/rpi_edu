import bluetooth as bt

socket = bt.BluetoothSocket( bt.RFCOMM )
print("scanning...")
scan_list = bt.discover_devices(lookup_names = True)
print(f"found {len(scan_list)} devices")
for i, (addr, name) in enumerate(scan_list):
    print(f"{i}: {addr} ({name})")
    
if len(scan_list) > 0 :
    idx = eval(input("device number you want to connect:"))
    address = scan_list[idx][0]
    socket.connect((address, 3)) 
    print ("connected.")
    socket.send(b"Hello Bluetooth World.")
    print ("sent data")
    recv = socket.recv(1024)
    print(f"recv data : {recv.decode()}")
    socket.close()