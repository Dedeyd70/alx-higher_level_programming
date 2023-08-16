#!/usr/bin/python3
"""Defining a file writing function"""


def write_file(filename="", text=""):
    """A function that writes to a text file"""
    with open(filename, mode="w") as fd:
        nbc = fd.write(text)
        return nbc
