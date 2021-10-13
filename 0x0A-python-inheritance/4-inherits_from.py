#!/usr/bin/python3
'''
is inheritance
'''


def inherits_from(obj, a_class):
    '''
    obj: an object
    a_class: a class
    '''
    return type(obj) != a_class and isinstance(obj, a_class)
