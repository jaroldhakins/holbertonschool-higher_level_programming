#!/usr/bin/python3
'''
Inherits from Rectangle
'''


Rectangle = __import__('9-rectangle').Rectangle


'''
Square class
'''


class Square(Rectangle):
    '''square class'''
    def __init__(self, size):
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        return ("[Square]" + str(self.__size) + "/" + str(self.__size))
