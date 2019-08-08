from binascii import unhexlify
s = 'f0cbf260e0ca8ec2431089fb393a1c29513aaaa5847d13e8be84760968e64dc6'
print(s)
print(type(s))

t = unhexlify(s)
print(type(t))
print(t)