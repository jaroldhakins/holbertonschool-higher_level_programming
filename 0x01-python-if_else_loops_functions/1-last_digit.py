#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num1 = 0
d = 0
str = "and is less than 6 and not 0"
if number < 0:
    num1 = number * -1
    d = num1 % 10
    d = d * -1
else:
    d = number % 10
if d == 0:
    print("last digit of {:d} is {:d} and is 0".format(number, d))
elif d > 5:
    print("last digit of {:d} is {:d} and is greater than 5".format(number, d))
elif d < 6 and d != 0:
    print("last digit of {:d} is {:d} {:s}".format(number, d, str))
