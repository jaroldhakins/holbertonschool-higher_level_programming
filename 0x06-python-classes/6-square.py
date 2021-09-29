#!/usr/bin/python3
'''create class Square'''


class Square:
    '''initialized with init method'''

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    def position(self):
        return self.__position

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @position.setter
    def position(self, position):
        if type(position != tuple):
            raise TypeError("position must be a tuple of 2 positive integer")
