#!/usr/bin/python3
'''This new class inherits from Rectangle
'''

from models.rectangle import Rectangle


class Square(Rectangle):
    """New class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter that retrieves size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter that sets the value of size"""
        self.width = value
        self.height = value

    def __str__(self):
        """Method that returns the square string representation"""
        return f"[Square] ({self.id}) {self.x}/{self.y} " \
               f"- {self.width}"
