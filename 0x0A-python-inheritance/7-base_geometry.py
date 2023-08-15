#!/usr/bin/python3
"""Defining a base class for geometry"""


class BaseGeometry:
    """Representing the base geometry."""

    def area(self):
        """Raising an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validating a value.
            Args:
                name(str): Name of the parameter.
                value(int): The value.
            Raises:
                TypeError: where value is not an integer.
                ValueError: if is value <= 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
