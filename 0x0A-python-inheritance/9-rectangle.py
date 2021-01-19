#!/usr/bin/python3
""" This module contains a class Rectangle that inherits from
    BaseGeometry. It contains instantiation with 'width' and
    'height' """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class """
    def __init__(self, width, height):
        """ init method:
            Args:
                self
                width (int)
                height (int)
            Returns:
                None
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ area method:
            Args:
                width (int)
                height (int)
            Returns:
                Area as int: width * height
        """
        return (self.__width * self.__height)
# Also gives correct output: return ("{}".format(self.__width * self.__height))

    def __str__(self):
        """ __str__ method:
            Args:
                width (int)
                height (int)
            Returns:
                Area of Rectangle
        """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
