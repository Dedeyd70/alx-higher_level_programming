#!/usr/bin/python3
"""Deining a class MyInt."""


class MyInt(int):
    """ class that inverts == and != operators."""

    def __eq__(self, value):
        """ inverts =="""
        return self.real != value

    def __ne__(self, value):
        """inverts !="""
        return self.real == value
