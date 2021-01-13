import bluetooth as bt

print("scanning...")
scan_list = bt.discover_devices(lookup_names = True)
print(f"found {len(scan_list)} devices")

for i, (addr, name) in enumerate(scan_list):
    print(f"{i}: {addr} - {name}")