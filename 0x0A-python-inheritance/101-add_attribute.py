#!/usr/bin/python3
'''
adds a new attribute
if it's possible
'''


def add_attribute(*args):
    """init class
    """
    if "main" in str(type(args[0])):
        setattr(args[0], args[1], args[2])
    else:
        raise TypeError("can't add new attribute")
