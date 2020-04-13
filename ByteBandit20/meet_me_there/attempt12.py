#!/usr/bin/python2

known_plaintext = 'aaaaaaaaaaaaaaaa'
known_ciphertext = 'ef92fab38516aa95fdc53c2eb7e8fe1d5e12288fdc9d026e30469f38ca87c305ef92fab38516aa95fdc53c2eb7e8fe1d5e12288fdc9d026e30469f38ca87c305'

import random
from Crypto.Cipher import AES
from os import urandom
from string import printable


#key1 = '0'*13 + ''.join([random.choice(printable) for _ in range(3)])
def keygen1():
    prefix = '0'*13
    for i in printable:
        for j in printable:
            for k in printable:
                yield prefix + ''.join([i,j,k])

all_key1 = list(keygen1())
print len(all_key1)

#f = open('plaintext_encrypted_with_all_key1_possibilities.txt','w')
#for key in keygen1():
#    cipher = AES.new(key=key, mode=AES.MODE_ECB)
#    ciphertext = cipher.encrypt(known_plaintext.encode('hex')).encode('hex')
#    f.write(ciphertext + ciphertext + '\n')
#f.close()


def keygen2():
    keys = []
    suffix = '0'*13
    for i in printable:
        for j in printable:
            for k in printable:
                yield ''.join([i,j,k]) + suffix

all_key2 = list(keygen2())
print len(all_key2)

#f = open('ciphertext_decrypted_with_all_key2_possibilities.txt','w')
#for key in keygen2():
#    cipher = AES.new(key=key, mode=AES.MODE_ECB)
#    decrypted_text = cipher.decrypt(known_ciphertext.decode('hex')).encode('hex')
#    f.write(decrypted_text + '\n')
#f.close()

with open('plaintext_encrypted_with_all_key1_possibilities.txt','r') as f:
    left_half = set([line.strip() for line in f.readlines()])

with open('ciphertext_decrypted_with_all_key2_possibilities.txt','r') as f:
    right_half = set([line.strip() for line in f.readlines()])

print left_half & right_half


