#!/usr/bin/python3
'''
BaseGeometry class
'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


'''
Rectangle class
'''


class Rectangle(BaseGeometry):
    """
    Rectangle class
    """
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
