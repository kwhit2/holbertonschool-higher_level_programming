#!/usr/bin/python3
""" This module contains a class Rectangle """


class Rectangle:
    """ Rectangle class - represents a rectangle

    Attributes:
        __width: integer, width of rectangle
        __height: integer, height of rectangle
    """
    def __init__(self, width=0, height=0):
        """ __init method
        Args:
            width: integer
            height: integer
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ getter for __width
        Returns:
            width of rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ property setter 'width'
        Args:
            value: integer
        Raises:
            TypeError: if width is not an int
            ValueError: if width is < 0
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """ getter for __height
        Returns:
            height of rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ property setter 'height'
        Args:
            value: integer
        Raises:
            TypeError: if height is not an int
            ValueError: if height is < 0
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        """ area method
        Args:
            self: rectangle object
        Return:
            the current rectangle area
        """
        return self.__width * self.__height

    def perimeter(self):
        """ area method
        Args:
            self: rectangle object
        Return:
            the current rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (self.__width * 2) + (self.__height * 2)
