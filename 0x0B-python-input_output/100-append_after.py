#!/usr/bin/python3
""" Function that inserts a line of text to a file, after each line
    containing a specific string """


def append_after(filename="", search_string="", new_string=""):
    """ append_after method:
        Args:
            filename:
            search_string:
            new_string:
        Returns:

    """
    with open(filename, mode='r+', encoding='utf-8') as f:
        for line in f:
            if search_string in line:
                return (f.write(new_string))
