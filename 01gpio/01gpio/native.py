import ctypes

native = ctypes.CDLL('./native.so')
native.hello()
ret = native.add(2, 3)
print('ret:', ret)