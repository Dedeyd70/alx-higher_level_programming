#!/usr/bin/python3
"""Defining a string to JSON function"""
import json


def to_json_string(my_obj):
    """A function that prints the JSON representation of an object"""
    return (json.dumps(my_obj))
