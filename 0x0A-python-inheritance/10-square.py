#!/usr/bin/python3
'''
Importing BaseGeometry class
'''


Rectangle = __import__('9-rectangle').Rectangle


'''
Square Class
'''


class Square(Rectangle):
    '''Square class'''
    def __init__(self, size):
        self.__size = size
        super().__init__(self.__size, self.__size)
