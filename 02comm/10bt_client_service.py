import bluetooth as bt

svc_name = "MyService"
print "finding service : %s" % svc_name
services=bt.find_service(name=svc_name,
                            uuid=bt.SERIAL_PORT_CLASS)
print "Found %d services" % len(services)
for i in range(len(services)):
   match=services[i]
   
   if(match["name"]=="MyService"):
      port=match["port"]
      name=match["name"]
      host=match["host"]
      print "Found service :", name, host, port

      socket=bt.BluetoothSocket( bt.RFCOMM )
      socket.connect((host, port))
      socket.send("Hello world 2")
      data = socket.recv(1024)
      print "recv :", data
      socket.close()

      break