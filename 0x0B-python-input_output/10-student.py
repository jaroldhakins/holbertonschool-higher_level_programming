#!/usr/bin/python3
"""Create a new class"""


class Student():
    """New class student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """descerialization"""
        the_dict = self.__dict__.copy()

        if type(attrs) == list:
            for key in self.__dict__.keys():
                if key not in attrs:
                    del the_dict[key]
        return the_dict
