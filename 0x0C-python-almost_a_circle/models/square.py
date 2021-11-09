#!/usr/bin/python3
'''This new class inherits from Rectangle
'''

from models.rectangle import Rectangle


class Square(Rectangle):
    """New class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializing Square"""
        super().__init__(size, size, x, y, id)
