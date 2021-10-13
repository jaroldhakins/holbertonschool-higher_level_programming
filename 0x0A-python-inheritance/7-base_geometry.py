#!/usr/bin/python3
'''
BaseGeometry class
'''


class BaseGeometry():
    """
    This class has two methods:
    area() and integer_validator
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.name = name
        self.value = value

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(self.name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))
