#!/usr/bin/python3
""" Technical interview preparation:
    Create a function def pascal_triangle(n): that returns a list of lists
    of integers representing the Pascal’s triangle of n: """


def pascal_triangle(n):
    """ pascal_triangle method:
        Args:
            n (int)
        Returns:
            A list of lists of integers representing the Pascal’s triangle of n:
            or An empty list if n <= 0
    """
    if n <= 0:
        return ([])
    if n == 1:
        return [[1]]
