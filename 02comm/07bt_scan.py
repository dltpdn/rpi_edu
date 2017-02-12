import bluetooth as bt

print "scanning..."

scan_list = bt.discover_devices(lookup_names = True)

print "found %d devices" % len(scan_list)

for addr, name in scan_list:
    print "%s (%s)" % (addr, name)