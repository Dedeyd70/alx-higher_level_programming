#!/usr/bin/python3
"""Defining a class Student."""


class Student:
    """ Class that is defining student instances """

    def __init__(self, first_name, last_name, age):
        """ initializing a new  student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ method retrieves a dict representation of student instance """
        if (type(attrs) == list and
                all(type(d) == str for d in attrs)):
            return {m: getattr(self, m) for m in attrs if hasattr(self, m)}
        return self.__dict__

    def reload_from_json(self, json):
        """ replacing attributes of the Student instance"""
        for key, value in json.items():
            setattr(self, key, value)
