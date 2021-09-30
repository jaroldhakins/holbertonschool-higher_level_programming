#!/usr/bin/python3
'''create a new Rectangle class
'''


class Rectangle:
    '''initialize the class
    '''
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        '''init'''

        Rectangle.number_of_instances += 1
        self.__width = width
        self.__height = height

    @property
    def width(self):
        '''method: set_width
        getter
        '''
        if (not isinstance(self.__width, int)) or isinstance(self.__width,
                                                             bool):
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")
        return self.__width

    @width.setter
    def width(self, width):
        '''method set_width
        '''
        if not isinstance(self.__width, int) or isinstance(self.__width, bool):
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        '''method: set_height
        getter
        '''
        if (not isinstance(self.__height, int)) or isinstance(self.__height,
                                                              bool):
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise ValueError("height must be >= 0")
        return self.__height

    @height.setter
    def height(self, height):
        '''setter
        '''
        if not isinstance(self.__height, int) or isinstance(self.__height,
                                                            bool):
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        '''return the Rectangle area
        '''
        return self.__width * self.__height

    def perimeter(self):
        '''return the Rectangle perimeter
        '''
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__height * self.__width))

    def __str__(self):
        '''method: __str__
        return nice string rectangle
        '''
        string = ""
        x = self.__height - 1
        if self.__height == 0 or self.__width == 0:
            return ""
        for i in range(self.__height):
            for j in range(self.__width):
                string += "#"
            if i < x:
                string += "\n"
        return string

    def __repr__(self):
        '''method: __repr__ create new object
        '''
        string = "Rectangle(" + str(self.__width) + ","
        string += str(self.__height) + ")"
        return string

    def __del__(self):
        '''delete a instance
        '''
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
