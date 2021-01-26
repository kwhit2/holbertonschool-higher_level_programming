#!/usr/bin/python3
""" This module contains a class Square that is inherited from Rectangle """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class inherited from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ __init__ method:
            Args:
                self:
                size: size of a side of the square (integer)
                x: position on x axis
                y: position on y axis
                id: Assume id is an integer. Do not need to test the type of...
                ...it(id). Default value of id is set to None
            Returns:
                None
        """
        super().__init__(size, size, x, y, id)
        # Pass in the init method from Rectangle but pass in size, size...
        # ...instead of width & height

    def __str__(self):
        """ __str__ method: returns string representation of square """
        return ("[Square] ({}) {:d}/{:d} - {:d}".format
                (self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """ getter for size
            Args: self
            Returns: width/size
        """
        return (self.width)

    @size.setter
    def size(self, value):
        """ property setter for size:
            Args:
                self:
                value = value
            Raises:
                TyperError: if size is not an integer
                ValueError: is size is < 0
            Returns:
                None
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ update method: assigns attributes to: id, size, x, y
            Args:
                self:
                *args: variable number of arguments
                **kwargs: variable number of keyword arguments
            Returns: None
        """
        if len(args):
            for a, b in enumerate(args):
                if a == 0:
                    self.id = b
                if a == 1:
                    self.size = b
                if a == 2:
                    self.x = b
                if a == 3:
                    self.y = b
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """ to_dictionary method:
            Args: self:
            Returns: the dictionary representation of a Square
        """
        empty_dict = {}  # create empty dictionary
        empty_dict["id"] = self.id  # set key 'id' = to value of 'id' attribute
        empty_dict["size"] = self.size
        empty_dict["x"] = self.x
        empty_dict["y"] = self.y

        return (empty_dict)
