#!/usr/bin/python3
"""Defining a function that reads content of a file"""


def read_file(filename=""):
    """Displaying contents of a file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
