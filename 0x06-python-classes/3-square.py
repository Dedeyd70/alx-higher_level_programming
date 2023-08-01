#!/usr/bin/python3
"""Naming class square"""


class Square:
    """defines a square"""
    def __init__(self, size=0):
        """initialize square

        Args:
            size (int): size of the square

        Attributes:

            __size (int): size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """returns the current square area"""
        result = self.__size * self.__size
        return result
