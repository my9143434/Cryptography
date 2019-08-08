import base64
import binascii
import struct
from base64 import b64encode
from os import urandom

binstr = urandom(16)
print(binstr)

binstr = b64encode(binstr).decode('utf-8')
print(binstr)
print(type(binstr))
'''
binstr= base64.b64encode(binstr)
print(binstr)
'''
'''
encoded = b64encode(binstr).decode()
# encoded = binascii.b2a_base64(binstr)
print(encoded)
# print(binascii.a2b_base64(encoded))

encoded = b64encode(encoded).encode()
print(encoded)
'''
'''
ba=bytearray(binstr)
print (list(ba))

print (binascii.b2a_hex(binstr))
print (struct.unpack("21B",binstr))
'''