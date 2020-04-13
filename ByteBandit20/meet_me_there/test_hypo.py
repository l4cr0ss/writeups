
keys = ('00000000000004Ph', '0ep0000000000000')
key1 = keys[0].decode('hex')
key2 = keys[1].decode('hex')
print((key1^key2).encode('hex'))
