#!/usr/bin/python3
"""
   Prints a square depending on the size parameter
"""


def print_square(size):
    """
    Args:
        size: integer number

    Raises:
       TypeError: size must be an integer
       ValueError: size must be >= 0

    Returns:
       the square printed using #
    """
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for d in range(size):
        print("#" * size)
