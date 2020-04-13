#!/usr/bin/python2

import sys
import random
from Crypto.Cipher import AES
from os import urandom
from string import printable

answer = ''

encrypted_string = 'ef92fab38516aa95fdc53c2eb7e8fe1d5e12288fdc9d026e30469f38ca87c305ef92fab38516aa95fdc53c2eb7e8fe1d5e12288fdc9d026e30469f38ca87c305'

def key1():
    keys = []
    suffix = '0'*13
    for i in printable:
        for j in printable:
            for k in printable:
                yield ''.join([i,j,k]) + suffix

def key2():
    prefix = '0'*13
    for i in printable:
        for j in printable:
            for k in printable:
                yield prefix + ''.join([i,j,k])

def solve(flag,key1,key2):
    cipher1 = AES.new(key=key1, mode=AES.MODE_ECB)
    cipher2 = AES.new(key=key2, mode=AES.MODE_ECB)
    c1 = cipher1.encrypt(flag.encode('hex'))
    c2 = cipher2.encrypt(c1.encode('hex'))
    return flag

def print16(text):
    for i in range(len(text)):
        if i%16==0 and i != 0:
            sys.stdout.write('  ')
        if i%64==0 and i !=0 :
            print
        sys.stdout.write(text[i])
    print

def string_bytes():
    string = 'ef92fab38516aa95fdc53c2eb7e8fe1d5e12288fdc9d026e30469f38ca87c305ef92fab38516aa95fdc53c2eb7e8fe1d5e12288fdc9d026e30469f38ca87c305'
    for i in range(0,len(string),2):
        yield string[i:i+2]

def flag_bytes():
    flag = 'fa364f11360cef2550bd9426948af22919f8bdf4903ee561ba3d9b9c7daba4e759268b5b5b4ea2589af3cf4abe6f9ae7e33c84e73a9c1630a25752ad2a984abfbbfaca24f7c0b4313e87e396f2bf5ae56ee99bb03c2ffdf67072e1dc98f9ef691db700d73f85f57ebd84f5c1711a28d1a50787d6e1b5e726bc50db5a3694f576'
    for i in range(0,len(flag),2):
        yield flag[i:i+2]

fb = flag_bytes()
sb = string_bytes()

candidates = {}

tested = 0
message = 'aaaaaaaaaaaaaaaa'

k1=list(key1())
k2=list(key2())
print len(k1),len(k2)
for key1 in k1:
    for key2 in k2:
        if solve(message,key1,key2)[:64] == encrypted_string[:64]:
            print((key1,key2))
            break

