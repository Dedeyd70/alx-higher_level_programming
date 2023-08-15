#!/usr/bin/python3
"""Defining a base class for geometry"""


class BaseGeometry:
    """Representing the base geometry."""

    def area(self):
        """Raising an exception"""
        raise Exception("area() is not implemented")
