#!/usr/bin/python3
'''Square area'''


class Square:
    '''initialized with __init__'''
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    '''return area of square'''
    def area(self):
        return self.__size * self.__size
