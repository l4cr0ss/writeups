#!/usr/bin/python

import random
from Crypto.Cipher import AES
from os import urandom
from string import printable

random.seed(urandom(32))

their_input = 'aaaaaaaaaaaaaaaa'
val = len(their_input) % 16
if not val == 0:
    their_input += '0'*(16 - val)
pt = their_input.encode('hex')

key1 = '0'*13 + ''.join([random.choice(printable) for _ in range(3)])
key2 = ''.join([random.choice(printable) for _ in range(3)]) + '0'*13

cipher1 = AES.new(key=key1, mode=AES.MODE_ECB)
cipher2 = AES.new(key=key2, mode=AES.MODE_ECB)

enc_flag = 'fa364f11360cef2550bd9426948af22919f8bdf4903ee561ba3d9b9c7daba4e759268b5b5b4ea2589af3cf4abe6f9ae7e33c84e73a9c1630a25752ad2a984abfbbfaca24f7c0b4313e87e396f2bf5ae56ee99bb03c2ffdf67072e1dc98f9ef691db700d73f85f57ebd84f5c1711a28d1a50787d6e1b5e726bc50db5a3694f576'.decode('hex')
