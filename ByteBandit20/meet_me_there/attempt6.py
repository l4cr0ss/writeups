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

string = 'ef92fab38516aa95fdc53c2eb7e8fe1d5e12288fdc9d026e30469f38ca87c305ef92fab38516aa95fdc53c2eb7e8fe1d5e12288fdc9d026e30469f38ca87c305'
flag = 'fa364f11360cef2550bd9426948af22919f8bdf4903ee561ba3d9b9c7daba4e759268b5b5b4ea2589af3cf4abe6f9ae7e33c84e73a9c1630a25752ad2a984abfbbfaca24f7c0b4313e87e396f2bf5ae56ee99bb03c2ffdf67072e1dc98f9ef691db700d73f85f57ebd84f5c1711a28d1a50787d6e1b5e726bc50db5a3694f576'
key1 = None
key2 = None
pt = pt.encode('hex')

for i in printable:
    for j in printable:
        for k in printable:
            key1 = '0'*13 + ''.join([i,j,k])
            key2 = '303030303030303030303030300c0c0c'.decode('hex')
            c1 = AES.new(key=key1, mode=AES.MODE_ECB)
            c2 = AES.new(key=key2, mode=AES.MODE_ECB)
            ct1 = c1.encrypt(pt)
            ct2 = c2.encrypt(ct1.encode('hex'))
            if ct2 == string:
                break
print (key1,key2) if key1 else "nada"
