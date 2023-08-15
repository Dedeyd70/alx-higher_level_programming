#!/usr/bin/python3
""" contains the MyList class """


class MyList(list):
    """A subclass of list"""
    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))
