#!/usr/bin/python3
"""Defining a rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Reprsenting a square."""

    def __init__(self, size):
        """Intializing a new square.
        Args:
            size (int): Size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
