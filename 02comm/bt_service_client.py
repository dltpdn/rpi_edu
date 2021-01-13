import bluetooth as bt

svc_name = "MyService"
print("finding service : %s" % svc_name)
uuid ='c2575952-d199-4bc0-8bd4-1aa48930a8fa'
services=bt.find_service(svc_name, uuid=uuid)
print(f"Found len(services) services")
for match in services:
   print(match)
   if(match["name"]=="MyService"):
      port=match["port"]
      name=match["name"]
      host=match["host"]
      print("Found service :", name, host, port)
      socket=bt.BluetoothSocket( bt.RFCOMM )
      socket.connect((host, port))
      socket.send(b"Hello world 2")
      data = socket.recv(1024)
      print("recv :", data)
      socket.close()

      break