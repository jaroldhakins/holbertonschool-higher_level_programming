#!/usr/bin/python3
"""
This function reads a text file
"""


def read_file(filename=""):
    """This function
    reads a text file
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
