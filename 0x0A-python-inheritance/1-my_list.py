#!/usr/bin/python3
""" class MyList that inherits from list """


class MyList(list):
    """ class that inherits from list """
    def print_sorted(self):
        """ print_sorted method:
            Args:
                self: list to print
            Returns:
                None
        """
        print(sorted(self))
