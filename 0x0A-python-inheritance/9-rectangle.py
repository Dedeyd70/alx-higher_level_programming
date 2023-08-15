#!/usr/bin/python3
"""Defining a class rectangle that inherits BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """representing a rectangle using BaseGeometry"""
    def __init__(self, width, height):
        """initializing a new rectangle."""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returning the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        string = "[" + str(self.__class__.__name__) + "]"
        string += str(self.__width) + "/" + str(self.__height)
        return string
