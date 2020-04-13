#!/usr/bin/python2

pt = 'aaaaaaaaaaaaaaaa'

import random
from Crypto.Cipher import AES
from os import urandom
from string import printable

random.seed(urandom(32))

#key1 = '0'*13 + ''.join([random.choice(printable) for _ in range(3)])
#key2 = ''.join([random.choice(printable) for _ in range(3)]) + '0'*13
key1, key2 = ('0000000000000j>Y', "['t0000000000000")

print(key1,key2)

cipher1 = AES.new(key=key1, mode=AES.MODE_ECB)
cipher2 = AES.new(key=key2, mode=AES.MODE_ECB)

print 'plaintext: ' + pt

print 'hex encoded plaintext: ' + pt.encode('hex')

c1 = cipher1.encrypt(pt.encode('hex'))
print 'intermediate ciphertext: ' + c1.encode('hex')

c2 = cipher2.encrypt(c1.encode('hex'))
print 'hex encoded Encrypted plaintext:\n' + c2.encode('hex')

p2 = cipher2.decrypt(c2)
print 'intermediate ciphertext: ' + p2

p1 = cipher1.decrypt(p2.decode('hex'))
print 'hex encoded Decrypted plaintext: ' + p1
print 'Decrypted plaintext: ' + p1.decode('hex')
