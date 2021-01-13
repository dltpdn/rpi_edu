import bluetooth._bluetooth as bluez
import sys, time
import ble 

UUID = "000000ACE8B4E0C27D20B611B611C774"
MAJOR = 9 
MINOR = 7 
POWER = -59 

dev_id = 0
same_data = True #False
try:
    #ble.hci_config(dev_id, "up")
    #ble.hci_config(0, "leadv3")
    sock = bluez.hci_open_dev(dev_id)
except:
    print( "error accessing bluetooth device...")
    ble.hci_config(dev_id, "noleadv")
    sys.exit(1)

ble.hci_cmd_operate(sock, "start")
if same_data:
  ble.hci_cmd_format(sock, UUID, MAJOR, MINOR, POWER)
  ble.hci_cmd_setting(sock, 100) #100ms

try:
  print("BLE EMIT START")
  cnt1 = 0
  cnt2 = 100
  while True:
    if not same_data :
      ble.hci_cmd_format(sock, UUID, cnt1, cnt2, POWER)
      cnt1 = cnt1+1 if cnt1 < 100 else 0
      cnt2 = cnt2-1 if cnt1 > 1 else 100
      print(cnt1, cnt2)
    time.sleep(1)
finally:
  print("BLE EMIT STOP")
  ble.hci_cmd_operate(sock, "stop")
  #ble.hci_config(dev_id, "noleadv")
