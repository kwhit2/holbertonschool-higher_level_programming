#!/usr/bin/python3
class Square:
    """ Square class
    """
    def __init__(self, size=0):
        """__init__ method initialization
        Args:
            size: integer
        Raises:
            TypeError: if the size is not an integer
            ValueError: if the size of the integers value is less than 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
