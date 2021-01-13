import sys
import bluetooth._bluetooth as bluez
import ble


dev_id = 0
try:
    sock = bluez.hci_open_dev(dev_id)
    print( "ble thread started")

except:
    print( "error accessing bluetooth device...")
    sys.exit(1)

ble.hci_le_set_scan_parameters(sock)
ble.hci_enable_le_scan(sock)

uuids = ["2f234454cf6d4a0fadf2f4911ba9ffa6", 
        "11111111222233334444555555555555",
         "000000ace8b4e0c27d20b611b611c774"]
#uuids = None
try:
    while True:
        returnedList = ble.parse_events(sock, 10)
        for beacon in returnedList:
            if uuids is None or beacon['UUID'] in uuids:
                txpow = beacon['TxPower']
                rssi = beacon['RSSI']
                print(beacon, f'Dist:{ble.calc_dist(txpow, rssi):.2f}m')
finally:
    ble.hci_disable_le_scan(sock)