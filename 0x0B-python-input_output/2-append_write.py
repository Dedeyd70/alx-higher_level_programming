#!/usr/bin/python3
"""Defining a function that appends a string to the end of a text file."""


def append_write(filename="", text=""):
    """Returns the number of charcaters added."""
    with open(filename, mode="a") as fd:
        d = fd.write(text)
        return d
