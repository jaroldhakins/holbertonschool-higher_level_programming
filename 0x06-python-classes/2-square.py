#!/usr/bin/python3
'''class Square'''


class Square:
    '''Square initialized with size'''
    pass

    def __init__(self, size=0):
        '''init with class square'''
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
