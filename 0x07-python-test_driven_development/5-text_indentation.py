#!/usr/bin/python3
""" This module contains a function that prints a text with 2 new lines after
    each of these characters: ., ? and : """


def text_indentation(text):
    """ text_definition method
    Args: text:
        chars of following . ? :
    Raises:
        TypeError: text must be a string
    Returns: None
    """
    chars = ".?:"

    if type(text) is not str:
        raise TypeError("text must be a string")

    else:
        for c in text:
            print(c, end="")
            if c in chars:
                print()
                print()
