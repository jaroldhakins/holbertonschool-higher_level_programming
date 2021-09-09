#!/usr/bin/python3
i = 122
while i >= 97:
    sup = 0
    if i % 2 != 0:
        i = i - 32
        sup = 1
    print("{:s}".format(chr(i)), end="")
    if sup == 1:
        i = i + 32
    i = i - 1
