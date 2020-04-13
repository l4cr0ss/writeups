#!/usr/bin/python2

import sys
from os import path
import random
from Crypto.Cipher import AES
from os import urandom
from string import printable

key1 = '0'*13 + ''.join([random.choice(printable) for _ in range(3)])
key2 = ''.join([random.choice(printable) for _ in range(3)]) + '0'*13

known_pt = "aaaaaaaaaaaaaaaa"
known_ct = 'ef92fab38516aa95fdc53c2eb7e8fe1d5e12288fdc9d026e30469f38ca87c305ef92fab38516aa95fdc53c2eb7e8fe1d5e12288fdc9d026e30469f38ca87c305'

def keygen1():
    prefix = '0'*13
    for i in printable:
        for j in printable:
            for k in printable:
                yield prefix + ''.join([i,j,k])

def keygen2():
    keys = []
    suffix = '0'*13
    for i in printable:
        for j in printable:
            for k in printable:
                yield ''.join([i,j,k]) + suffix

def load_pts():
    candidates = {}
    with open('encrypted_pts','rb') as f:
        lines = f.readlines()
        for line in lines:
            key,val = line.rstrip().split(',')
            candidates[key] = val
    return candidates

# encrypt known_pt with every possible key, yielding the intermediate value,
# building a table of k-v pairs where:
    # k = the result of encrypting the plaintext using a candidate key
    # v = the candidate key used to encrypt the plaintext
# save the table to disk

key1_cts = {}
if not path.exists('encrypted_pts'):
    with open('encrypted_pts','wb') as f:
        for key1 in keygen1():
            c1 = AES.new(key=key1, mode=AES.MODE_ECB)
            ct = c1.encrypt(known_pt.encode('hex')).encode('hex')
            f.write(ct + ',' + key1.encode('hex') + '\n')
    load_pts()
else:
    key1_cts = load_pts()

print "phase 1 complete (" + str(len(key1_cts)) + "cts)"

# decrypt known_ct with every possible key, yield the intermediate value,
# building a table of k-v pairs where:
    # k = the result of decrypting the ciphertext using a candidate key
    # v = the candidate key used to decrypt the ciphertext

key2_pts = {}
if not path.exists('decrypted_cts'):
    with open('decrypted_cts','wb') as f:
        for key2 in keygen2():
            c2 = AES.new(key=key2, mode=AES.MODE_ECB)
            pt = c2.decrypt(known_ct).encode('hex')
            key2_pts[pt] = key2.encode('hex')
            f.write(pt[:64] + ',' + key2.encode('hex') + '\n')
else:
    with open('decrypted_cts','rb') as f:
        lines = f.readlines()
        for line in lines:
            key,val = line.rstrip().split(',')
            key2_pts[key] = val

print "phase 2 complete (" + str(len(key2_pts)) + "pts)"

# find the intersection of the sets
print key1_cts.viewkeys() & key2_pts.viewkeys()



