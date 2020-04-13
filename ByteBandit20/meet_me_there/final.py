#!/usr/bin/python2
import random
from Crypto.Cipher import AES
from os import urandom
from string import printable

# known plaintext
kpt = 'aaaaaaaaaaaaaaaa'
kpt = kpt.encode('hex')

# known ciphertext
kct = 'ef92fab38516aa95fdc53c2eb7e8fe1d5e12288fdc9d026e30469f38ca87c305\
ef92fab38516aa95fdc53c2eb7e8fe1d5e12288fdc9d026e30469f38ca87c305'
kct = kct.decode('hex')

# encrypted flag
flag = 'fa364f11360cef2550bd9426948af22919f8bdf4903ee561ba3d9b9c7daba4e7\
59268b5b5b4ea2589af3cf4abe6f9ae7e33c84e73a9c1630a25752ad2a984abf\
bbfaca24f7c0b4313e87e396f2bf5ae56ee99bb03c2ffdf67072e1dc98f9ef69\
1db700d73f85f57ebd84f5c1711a28d1a50787d6e1b5e726bc50db5a3694f576' 

def keygen(n=1):
    pad = '0'*13
    template = pad + "{}" if n == 1 else "{}" + pad 
    for i in printable:
        for j in printable:
            for k in printable:
                yield template.format(''.join([i,j,k]))

L1, L2 = ({},{})
ks1, ks2 = (keygen(1),keygen(2))
for k1,k2 in zip(ks1,ks2):
    L1[AES.new(key=k1, mode=AES.MODE_ECB).encrypt(kpt).encode('hex')] = k1.encode('hex')
    L2[AES.new(key=k2, mode=AES.MODE_ECB).decrypt(kct)] = k2.encode('hex')

ict = (L1.viewkeys() & L2.viewkeys()).pop()
k1, k2 = L1[ict].decode('hex'), L2[ict].decode('hex')
c1 = AES.new(key=k1, mode=AES.MODE_ECB)
c2 = AES.new(key=k2, mode=AES.MODE_ECB)
p2 = c2.decrypt(flag.decode('hex'))
p1 = c1.decrypt(p2.decode('hex'))
print p1.decode('hex')
