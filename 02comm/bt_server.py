import bluetooth as bt
import os

if os.system("sudo hciconfig hci0 piscan"): # 0:OK, -1:Fail
    exit()

server = bt.BluetoothSocket( bt.RFCOMM )

server.bind(("", 3 ))
server.listen(1)
print("ready to connect...")
socket, address = server.accept()
print("client connected : ", address)

data = socket.recv(1024)
print(f"received :{data}")
socket.send(b'Good bye~')
print('sent data')
socket.close()
server.close()