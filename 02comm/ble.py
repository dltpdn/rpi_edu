# This code based on https://github.com/switchdoclabs/iBeacon-Scanner-
DEBUG = False

import os
import sys
import struct
import subprocess
import re
from time import sleep

import bluetooth._bluetooth as bluez

LE_META_EVENT = 0x3e
LE_PUBLIC_ADDRESS=0x00
LE_RANDOM_ADDRESS=0x01
LE_SET_SCAN_PARAMETERS_CP_SIZE=7

LE_ROLE_MASTER = 0x00
LE_ROLE_SLAVE = 0x01

EVT_LE_CONN_COMPLETE=0x01
EVT_LE_ADVERTISING_REPORT=0x02
EVT_LE_CONN_UPDATE_COMPLETE=0x03
EVT_LE_READ_REMOTE_USED_FEATURES_COMPLETE=0x04

ADV_IND=0x00
ADV_DIRECT_IND=0x01
ADV_SCAN_IND=0x02
ADV_NONCONN_IND=0x03
ADV_SCAN_RSP=0x04

OGF = 0x08
OCF_LE_SET_SCAN_PARAMETERS=0x000B
OCF_LE_SET_SCAN_ENABLE=0x000C
OCF_LE_CREATE_CONN=0x000D

OCF_LE_ADVT_DATA = 0x0008 #LE Set Advertising Data
OCF_LE_ADVT_PARAM = 0x0006 # LE Set Advertising Parameters
OCF_LE_ADVT_ENABLE = 0x000A #LE Set Advertise Enable
EOF = 0x00 #(0).to_bytes(1, byteorder='big')
param_start = 0x01
param_stop = 0x00

IBEACONPROFIX = [0x1E, 0x02, 0x01, 0x1A, 0x1A, 0xFF, 0x4C, 0x00, 0x02, 0x15]

def hci_config(dev_id, param):
  result = subprocess.check_output("sudo hciconfig " + "hci%d"%dev_id + " " + param, shell=True)

def str2byte(str):
    return bytes([int(e, 16) for e in str.split()])

def hci_cmd_format(sock, uuid, major, minor, txpower):
    uuid_bytes = bytes(list(map(lambda d: int(d, 16), re.findall('..',uuid))))
    cmd_pkt = bytes(IBEACONPROFIX) + uuid_bytes + \
                 major.to_bytes(2, byteorder='big') + minor.to_bytes(2, byteorder='big') + \
                 txpower.to_bytes(1, byteorder='big', signed=True) + bytes(EOF)
    bluez.hci_send_cmd(sock, OGF, OCF_LE_ADVT_DATA, cmd_pkt)


def hci_cmd_setting(sock, interval):
    intervalHEX = '{:04X}'.format(int(interval/0.625)) # 0.625ms is granularity
    minInterval = intervalHEX[2:] + " " + intervalHEX[:2] + " "
    maxInterval = intervalHEX[2:] + " " + intervalHEX[:2] + " "
    cmd_pkt = str2byte(maxInterval) + str2byte(maxInterval) + \
                 bytes([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x07, 0x00])
    bluez.hci_send_cmd(sock, OGF, OCF_LE_ADVT_PARAM, cmd_pkt)
    
def hci_cmd_operate(sock, param):
    if param =="start" :
        cmd_pkt = bytes([param_start])
    elif param == "stop" :
        cmd_pkt = bytes([param_stop])
    bluez.hci_send_cmd(sock, OGF, OCF_LE_ADVT_ENABLE, cmd_pkt)


def returnnumberpacket(pkt):
    myInteger = 0
    multiple = 256
    for c in pkt:
        myInteger +=  c * multiple
        multiple = 1
    return myInteger 

def returnstringpacket(pkt):
    myString = ""
    for c in pkt:
        myString +=  "%02x" %c
    return myString 

def printpacket(pkt):
    for c in pkt:
        sys.stdout.write("%02x " % c)

def get_packed_bdaddr(bdaddr_string):
    packable_addr = []
    addr = bdaddr_string.split(':')
    addr.reverse()
    for b in addr: 
        packable_addr.append(int(b, 16))
    return struct.pack("<BBBBBB", *packable_addr)

def packed_bdaddr_to_string(bdaddr_packed):
    return ':'.join('%02x'%i for i in struct.unpack("<BBBBBB", bdaddr_packed[::-1]))

def hci_enable_le_scan(sock):
    hci_toggle_le_scan(sock, 0x01)

def hci_disable_le_scan(sock):
    hci_toggle_le_scan(sock, 0x00)

def hci_toggle_le_scan(sock, enable):
    cmd_pkt = struct.pack("<BB", enable, 0x00)
    bluez.hci_send_cmd(sock, OGF, OCF_LE_SET_SCAN_ENABLE, cmd_pkt)


def hci_le_set_scan_parameters(sock):
    old_filter = sock.getsockopt( bluez.SOL_HCI, bluez.HCI_FILTER, 14)
    SCAN_RANDOM = 0x01
    OWN_TYPE = SCAN_RANDOM
    SCAN_TYPE = 0x01

    
def parse_events(sock, loop_count=100):
    old_filter = sock.getsockopt( bluez.SOL_HCI, bluez.HCI_FILTER, 14)

    flt = bluez.hci_filter_new()
    bluez.hci_filter_all_events(flt)
    bluez.hci_filter_set_ptype(flt, bluez.HCI_EVENT_PKT)
    sock.setsockopt( bluez.SOL_HCI, bluez.HCI_FILTER, flt )
    done = False
    results = []
    myFullList = []
    for i in range(0, loop_count):
        pkt = sock.recv(255)
        ptype, event, plen = struct.unpack("BBB", pkt[:3])
        #print "--------------" 
        if event == bluez.EVT_INQUIRY_RESULT_WITH_RSSI:
            i =0
        elif event == bluez.EVT_NUM_COMP_PKTS:
            i =0 
        elif event == bluez.EVT_DISCONN_COMPLETE:
            i =0 
        elif event == LE_META_EVENT:
            subevent = pkt[3] 
            pkt = pkt[4:]
            if subevent == EVT_LE_CONN_COMPLETE:
                le_handle_connection_complete(pkt)
            elif subevent == EVT_LE_ADVERTISING_REPORT:
                num_reports = pkt[0]
                report_pkt_offset = 0
                for i in range(0, num_reports):
                    item = {"UUID":returnstringpacket(pkt[report_pkt_offset -22: report_pkt_offset - 6]) ,
                            "MAC": packed_bdaddr_to_string(pkt[report_pkt_offset + 3:report_pkt_offset + 9]),
                            "MAJOR":"%i" % returnnumberpacket(pkt[report_pkt_offset -6: report_pkt_offset - 4]),
                            "MINOR":returnnumberpacket(pkt[report_pkt_offset -4: report_pkt_offset - 2]),
                            "TxPower": int.from_bytes(bytes([pkt[report_pkt_offset -2]]), byteorder='big', signed=True),
                            "RSSI": int.from_bytes(bytes([pkt[report_pkt_offset -1]]), byteorder='big', signed=True)}
                    myFullList.append(item)
                done = True
    sock.setsockopt( bluez.SOL_HCI, bluez.HCI_FILTER, old_filter )
    return myFullList

def calc_dist(txpower, rssi, n=2):
    dist = 10 ** ((txpower-rssi)/(10*n))
    return dist

def calc_dist2(txpower, rssi):
    ratio = rssi*1.0/txpower
    if ratio < 1.0:
        return ratio**10
    else:
        return (0.89976) * (ratio**7.7095) + 0.111