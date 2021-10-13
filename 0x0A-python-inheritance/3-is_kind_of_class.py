#!/usr/bin/python3
'''
returns True if the object is an instance
'''


def is_kind_of_class(obj, a_class):
    """
    This Function returns True
    if the object is an instance
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
