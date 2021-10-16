#!/usr/bin/python3
"""
this function appends a string
 at the end of a text file
"""


def append_write(filename="", text=""):
    """
    this function appends a string
    at the end of a text file
    """
    with open(filename, "a") as f:
        f.write(text)
    return len(text)
