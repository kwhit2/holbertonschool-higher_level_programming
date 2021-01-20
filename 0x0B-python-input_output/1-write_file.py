#!/usr/bin/python3
""" Function that writes a string to a text file (UTF8) and returns
    the number of characters written: """


def write_file(filename="", text=""):
    """ write_file method:
        Args:
            filename = name of file(string)
            text = text content of file
        Returns:
            contents written to file
    """
    with open(filename, mode='w', encoding='utf-8') as f:
            return f.write(text)
