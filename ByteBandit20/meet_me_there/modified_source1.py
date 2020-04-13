#!/usr/bin/python

import sys
import random
from Crypto.Cipher import AES
from os import urandom
from string import printable

random.seed(urandom(32))

realflag = "fa364f11360cef2550bd9426948af22919f8bdf4903ee561ba3d9b9c7daba4e759268b5b5b4ea2589af3cf4abe6f9ae7e33c84e73a9c1630a25752ad2a984abfbbfaca24f7c0b4313e87e396f2bf5ae56ee99bb03c2ffdf67072e1dc98f9ef691db700d73f85f57ebd84f5c1711a28d1a50787d6e1b5e726bc50db5a3694f576"

def print16(text):
    for i in range(len(text)):
        if i%16==0 and i != 0:
            sys.stdout.write('  ')
        if i%64==0 and i !=0:
            print
        sys.stdout.write(text[i])
    print

#key1 = '0'*13 + ''.join([random.choice(printable) for _ in range(3)])
key1 = '303030303030303030303030300c0c0c'.decode('hex')
#key2 = ''.join([random.choice(printable) for _ in range(3)]) + '0'*13
key2 = '#<!0000000000000'
print((key1,key2))

cipher1 = AES.new(key=key1, mode=AES.MODE_ECB)
cipher2 = AES.new(key=key2, mode=AES.MODE_ECB)

print "\nGive me a string:"
pt = raw_input()

val = len(pt) % 16
if not val == 0:
    pt += '0'*(16 - val)

c1 = cipher1.encrypt(pt.encode('hex'))
print16(c1.encode('hex'))
c2 = cipher2.encrypt(c1.encode('hex'))
print 'Encrypted string:\n' 
print16(c2.encode('hex'))
print

with open("flag.txt") as f:
    flag = f.read().strip()

# length of flag is a multiple of 16
ct1 = cipher1.encrypt(flag.encode('hex'))
print16(ct1.encode('hex'))
ct2 = cipher2.encrypt(ct1.encode('hex'))
print '\nEncrypted Flag:\n' 
print16(ct2.encode('hex'))
print
