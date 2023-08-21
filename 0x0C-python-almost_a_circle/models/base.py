#!/usr/bin/python3
"""Defining a base model class."""
import json
import csv
import random
import turtle


class Base:
    """Representing the base model"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializing a new Base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converting a dictionary into a JSON string"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the deserialization of a JSON string"""
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Square":
                new_dummy = cls(1, 1)
            else:
                new_dummy = cls(1, 1)
            new_dummy.update(**dictionary)
            return new_dummy

    @classmethod
    def load_from_file(cls):
        """Loads a file"""
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves a list of rectangles or squares as a csv file"""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module."""
        s = turtle.Screen()
        t = turtle.Turtle()
        cl = ["red", "cyan", "brown", "yellow", "pink", "blue", "purple"]
        turtle.bgcolor("Teal")
        t.pensize(3)
        shapes = list_rectangles + list_squares
        for rec_sq in shapes:
            t.color(cl[random.randint(0, 4)])
            t.penup()
            t.setpos(rec_sq.x, rec.sq.y)
            t.pendown()
            t.fd(rec_sq.width)
            t.rt(90)
            t.fd(rec_sq.height)
            t.right(90)
            t.fd(rec_sq.width)
            t.rt(90)
            t.fd(rec_sq.height)
            t.rt(90)
        s.exitonclick()
