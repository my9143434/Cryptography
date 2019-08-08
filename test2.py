from base64 import b64encode
from os import urandom
import base64

random_bytes = urandom(16)

print(random_bytes)
print("random bytes type: ", type(random_bytes))
print("random type length:", len(random_bytes))


# token = base64ToString(random_bytes)
# token = b64encode(random_bytes).decode('utf-8')
# token = bytes.decode(random_bytes)

token = b64encode(random_bytes).decode('utf-8')
print("decoded key", token)
print("decode token type (turn to string type): ", type(token))

# encoded = str.encode(token)

'''
encoded = base64.encodebytes(token)

# encoded = base64.b64encode(token.encode('utf-8'))
print("encoded key: ", encoded)
print("encoded type: ", type(encoded))
print("encoded length: ", len(encoded))
'''
# encoded = b64encode(token)
# token = token.encode('utf-8')
# print(encoded)
'''
token = b64encode(token).encode('utf-8')
print(token)
print(type(token))
'''


