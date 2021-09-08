#!/usr/bin/python3
for i in range(ord('a'), ord('{')):
    if i == chr('q') or i == chr('e'):
        continue
    print("{:s}".format(chr(i)), end='')
