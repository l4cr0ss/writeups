#!/usr/bin/python

import sys
import random
from Crypto.Cipher import AES
from os import urandom
from string import printable

def print16(text):
    for i in range(len(text)):
        if i%16==0 and i != 0:
            sys.stdout.write('  ')
        if i%64==0 and i !=0 :
            print
        sys.stdout.write(text[i])
    print

with open("flag.txt") as f:
    flag = f.read().strip()

#keys = ['00000000000004Ph', '0ep0000000000000']
keys = ['0000000000000313', '1140000000000000']

block = 'aaaaaaaaaaaaaaaa'

print keys[0].encode('hex')
print keys[1].encode('hex')
c1 = AES.new(key=keys[0], mode=AES.MODE_ECB)
c2 = AES.new(key=keys[1], mode=AES.MODE_ECB)

ct1 = c1.encrypt(block.encode('hex'))
ct2 = c2.encrypt(ct1.encode('hex'))

print16(ct1.encode('hex'))
print
print16(ct2.encode('hex'))

