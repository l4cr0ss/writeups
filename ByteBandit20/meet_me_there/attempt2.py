#!/usr/bin/python

import random
from Crypto.Cipher import AES
from os import urandom
from string import printable

c1 = 'ef92fab38516aa95fdc53c2eb7e8fe1d5e12288fdc9d026e30469f38ca87c305ef92fab38516aa95fdc53c2eb7e8fe1d5e12288fdc9d026e30469f38ca87c305'.decode("hex")
pt = 'aaaaaaaaaaaaaaaa'
val = len(pt) % 16
if not val == 0:
    pt += '0'*(16 - val)
pt = pt.encode('hex')

random.seed(urandom(32))

key = None
keys = []
for i in range (0,0x1000000):
    key1 = '0'*13 + ''.join([random.choice(printable) for _ in range(3)])
    cipher1 = AES.new(key=key1, mode=AES.MODE_ECB)
    ct1 = cipher1.encrypt(pt);
    if ct1 == c1:
        key = key1
        break
print(key if key else "nuthin")

