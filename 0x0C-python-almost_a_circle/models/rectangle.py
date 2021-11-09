#!/usr/bin/python3
"""New class, inherits from Base class"""


from models.base import Base


class Rectangle(Base):
    """initializing class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter to obtain width."""
        return self.__width

    @width.setter
    def width(self, value):
        """setter to modify width."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter to obtain height."""
        return self.__height

    @height.setter
    def height(self, value):
        """setter to modify height."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter to obtain x."""
        return self.__x

    @x.setter
    def x(self, value):
        """setter to modify x."""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter to obtain y."""
        return self.__y

    @y.setter
    def y(self, value):
        """setter to modify y."""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area of rectangle"""
        return self.__width * self.__height

    def display(self):
        """prints rectangle with this character #"""
        print("\n" * (self.__y), end="")
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                self.__y, self.__width, self.__height))

    def update(self, *args):
        key_list = ['id', '_Rectangle__width',  '_Rectangle__height',
                    '_Rectangle__x', '_Rectangle__y']
        for i, v in enumerate(args):
            self.__dict__[key_list[i]] = v
