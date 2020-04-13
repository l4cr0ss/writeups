#!/usr/bin/python

import random
from Crypto.Cipher import AES
from os import urandom
from string import printable

their_input = 'aaaaaaaaaaaaaaaa'
val = len(their_input) % 16
if not val == 0:
    their_input += '0'*(16 - val)
pt = their_input.encode('hex')
c0 = 'ef92fab38516aa95fdc53c2eb7e8fe1d5e12288fdc9d026e30469f38ca87c305ef92fab38516aa95fdc53c2eb7e8fe1d5e12288fdc9d026e30469f38ca87c305'.decode('hex')

random.seed(urandom(32))
keys = None
for i in range(0,0x10000000):
    key1 = '0'*13 + ''.join([random.choice(printable) for _ in range(3)])
    key2 = ''.join([random.choice(printable) for _ in range(3)]) + '0'*13

    cipher1 = AES.new(key=key1, mode=AES.MODE_ECB)
    cipher2 = AES.new(key=key2, mode=AES.MODE_ECB)
    
    c1 = cipher1.encrypt(pt)
    c2 = cipher2.encrypt(c1.encode('hex'))
    if c2 == c0:
        keys = (key1, key2)
        break
print(keys) if keys else "nada"


