#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num1 = 0
ld = 0
if number < 0:
    num1 = number * -1
    ld = num1 % 10
    ld = ld * -1
else:
    ld = number % 10
print("Last digit of {:d} is ".format(number), end="")
if ld == 0:
    print("{:d} and is 0".format(ld))
elif ld > 5:
    print("{:d} and is greater than 5".format(ld))
elif ld < 6 and ld != 0:
    print("{:d} and is less than 6 and not 0".format(ld))
