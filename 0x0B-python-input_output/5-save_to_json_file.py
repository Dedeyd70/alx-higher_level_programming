#!/usr/bin/python3
"""A function that writes an object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using JSON representation"""
    with open(filename, mode="w") as fd:
        json.dump(my_obj, fd)
