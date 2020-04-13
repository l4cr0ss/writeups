#!/usr/bin/python

import sys
import random
from Crypto.Cipher import AES
from os import urandom
from string import printable

# find the first key
pt = 'aaaaaaaaaaaaaaaa'
print pt
val = len(pt) % 16
if not val == 0:
    pt += '0'*(16 - val)
print pt
ciphertext = 'ef92fab38516aa95fdc53c2eb7e8fe1d5e12288fdc9d026e30469f38ca87c305ef92fab38516aa95fdc53c2eb7e8fe1d5e12288fdc9d026e30469f38ca87c305'.decode('hex')
key1 = None
pt = pt.encode('hex')

for i in printable:
    for j in printable:
        for k in printable:
            key1 = '0'*13 + ''.join([i,j,k])
            c1 = AES.new(key=key1, mode=AES.MODE_ECB)
            c2 = AES.new(key='0000000000000000', mode=AES.MODE_ECB)
            ct1 = c1.encrypt(pt)
            ct2 = c2.encrypt(ct1.encode('hex'))
            if ct2 == ciphertext:
                break
print key1.encode('hex') if key1 else "nada"
