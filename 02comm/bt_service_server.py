# run with sudo
import bluetooth as bt
import os

if os.system("sudo hciconfig hci0 piscan"): # 0:OK, -1:Fail
    exit()
server = bt.BluetoothSocket( bt.RFCOMM )

server.bind(("", bt.PORT_ANY ))
server.listen(1)
service_name = "MyService"
uuid = "c2575952-d199-4bc0-8bd4-1aa48930a8fa"
bt.advertise_service(server, service_name, service_id=uuid,
                     service_classes=[uuid, bt.SERIAL_PORT_CLASS],
                     profiles=[bt.SERIAL_PORT_PROFILE])

print("ready to connect...")
socket, address = server.accept()
print("client connected : ", address)

data = socket.recv(1024)
print("received :%s" % data)
socket.send(b'Good bye~')
print('sent data')
socket.close()
server.close()