#!/usr/bin/python3
""" This module contains a class Rectangle that is inherited from Base """


from models.base import Base


class Rectangle(Base):
    """ Rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ __init__ method:
            Args:
                self:
                width: width of rectangle (integer)
                height: height of rectangle (integer)
                x: space
                y: newline
                id: Assume id is an integer. Do not need to test the type of...
                ...it(id). Default value of id is set to None
            Returns:
                None
        """
        super().__init__(id)  # get the base init method & add below to it
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ getter for __width
        Returns:
            width of rectangle
        """
        return (self.__width)

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
        elif value <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = value

    @property
    def height(self):
        """ getter for __height
        Returns:
            height of rectangle
        """
        return (self.__height)

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
        elif value <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = value

    @property
    def x(self):
        """ getter for __x
        Returns:
            x
        """
        return (self.__x)

    @x.setter
    def x(self, value):
        """ property setter 'x'
        Args:
            value: integer
        Raises:
            TypeError: if x is not an int
            ValueError: if x is < 0
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = value

    @property
    def y(self):
        """ getter for __y
        Returns:
            y
        """
        return (self.__y)

    @y.setter
    def y(self, value):
        """ property setter 'y'
        Args:
            value: integer
        Raises:
            TypeError: if y is not an int
            ValueError: if y is < 0
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = value

    def area(self):
        """ area method:
            Args:
                width (integer)
                height (integer)
            Returns:
                Area as int: width * height
        """
        return (self.__width * self.__height)

    def display(self):
        """ display method:
        Args:
            self: rectangle object
        Returns:
            rectangle printed with #
        Prints:
            y = newline ('\n')
            x = space (blank space ' ')
            width = '#'
            height = '#'
        """
        print("\n" * self.__y, end="")
        for a in range(self.__height):
            print(" " * self.__x, end="")
            for b in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """ __str__ method:
            Args: self
            Returns:
                [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """ update method: assigns an argument to each attribute &
                assigns a key/value argument to attributes:
                id, width, height, x, y
            Args:
                self:
                *args: variable number of arguments
                **kwargs: variable number of keyword arguments
            Returns: None
        """
        if len(args):  # if args: gave same output. Up to checker
            for a, b in enumerate(args):
                if a == 0:
                    self.id = b
                if a == 1:
                    self.width = b
                if a == 2:
                    self.height = b
                if a == 3:
                    self.x = b
                if a == 4:
                    self.y = b
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """ to_dictionary method:
            Args: self:
            Returns: the dictionary representation of a Rectangle
        """
        empty_dict = {}  # create empty dictionary
        empty_dict["id"] = self.id  # set key 'id' = value of 'id' attribute
        empty_dict["width"] = self.width
        empty_dict["height"] = self.height
        empty_dict["x"] = self.x
        empty_dict["y"] = self.y

        return (empty_dict)
