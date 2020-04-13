#!/usr/bin/python2

import pdb
import random
from Crypto.Cipher import AES
from os import urandom
from string import printable

pt = 'aaaaaaaaaaaaaaaa'
pt = pt.encode('hex')
ct = 'ef92fab38516aa95fdc53c2eb7e8fe1d5e12288fdc9d026e30469f38ca87c305ef92fab38516aa95fdc53c2eb7e8fe1d5e12288fdc9d026e30469f38ca87c305'
ct = ct.decode('hex')

#key2 = ''.join([random.choice(printable) for _ in range(3)]) + '0'*13
def keygen2():
    keys = []
    suffix = '0'*13
    for i in printable:
        for j in printable:
            for k in printable:
                yield ''.join([i,j,k]) + suffix


#key1 = '0'*13 + ''.join([random.choice(printable) for _ in range(3)])
def keygen1():
    prefix = '0'*13
    for i in printable:
        for j in printable:
            for k in printable:
                yield prefix + ''.join([i,j,k])

ans = 'c91dcfc4e250ee0c013fe3e6faa0d76fc91dcfc4e250ee0c013fe3e6faa0d76f'

all_cipher1 = []
all_cipher1_keys = []
for key1 in keygen1():
    cipher1 = AES.new(key=key1,mode=AES.MODE_ECB)
    all_cipher1.append(cipher1.encrypt(pt).encode('hex'))
    all_cipher1_keys.append(key1.encode('hex'))

pdb.set_trace()

all_cipher2 = []
all_cipher2_keys = []
for key2 in keygen2():
    cipher2 = AES.new(key=key2,mode=AES.MODE_ECB)
    all_cipher2.append(cipher2.decrypt(ct))
    all_cipher2_keys.append(key2.encode('hex'))

text = (set(all_cipher1) & set(all_cipher2)).pop()
pdb.set_trace()

print text

key1 = all_cipher1_keys[all_cipher1.index(text)]
key2 = all_cipher2_keys[all_cipher2.index(text)]
print (key1,key2)
cipher1 = AES.new(key=key1,mode=AES.MODE_ECB)
cipher2 = AES.new(key=key2,mode=AES.MODE_ECB)

flag = "fa364f11360cef2550bd9426948af22919f8bdf4903ee561ba3d9b9c7daba4e759268b5b5b4ea2589af3cf4abe6f9ae7e33c84e73a9c1630a25752ad2a984abfbbfaca24f7c0b4313e87e396f2bf5ae56ee99bb03c2ffdf67072e1dc98f9ef691db700d73f85f57ebd84f5c1711a28d1a50787d6e1b5e726bc50db5a3694f576"

p2 = cipher2.decrypt(flag)
p1 = cipher1.decrypt(p2)
print 'hex encoded Decrypted plaintext: ' + p1.encode('hex')

