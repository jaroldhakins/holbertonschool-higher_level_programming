#!/usr/bin/python3
for i in range(ord('a'), ord('{')):
    if chr(i) == 'e' or chr(i) == 'q':
        continue
    print("{:s}".format(chr(i)), end='')