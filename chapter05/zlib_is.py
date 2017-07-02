#！/usr/bin/env/python3
#coding=utf-8

import zlib

s = b"hello word, 00000000000000000000000000000000"
print(type(s))
print(len(s))
c = zlib.compress(s)
print(len(c))
d = zlib.decompress(c)
print(d)