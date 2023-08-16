#!/usr/bin/python3
"""Defining a Student class"""


class Student:
    """This represents a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """This gets the dictionary presentation of Student."""
        return self.__dict__
