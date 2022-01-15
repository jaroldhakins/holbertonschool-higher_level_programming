#!/usr/bin/python3
"""
    This Script find the peak in an unsortered list of integers
"""


def find_peak(list_of_integers):
    """This function find the peak in an unsortered list of integers"""
    if len(list_of_integers) == 0:
        return None
    else:
        list_of_integers.sort()
        return list_of_integers[-1]
