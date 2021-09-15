#!/usr/bin/python3
def multiple_returns(sentence):
    lon = len(sentence)
    if lon > 0:
        first_char = sentence[0]
    else:
        first_char = "None"
    mul_ret = lon, first_char
    return mul_ret
