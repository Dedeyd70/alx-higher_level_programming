#!/usr/bin/python3
""" defining a rectangle subclass square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ representing a square"""
    def __init__(self, size):
        """ Initializing a square"""
        try:
            super().__init__(size, size)
        except TypeError:
            raise TypeError("size must be an integer")
        except ValueError:
            raise ValueError("size must be greater than 0")
        self.__size = size

    def __str__(self):
        """returns string form of a square
        """
        return '[Square] {size}/{size}'.format(size=self.__size)
