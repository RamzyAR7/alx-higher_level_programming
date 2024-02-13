#!/usr/bin/python3
"""
this module for Base class
"""


import json
import csv


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries == "":
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a class to a file"""
        if list_objs is None or list_objs == "":
            list_objs = []
        with open(f"{cls.__name__}.json", "w", encoding="utf-8") as file:
            obj_list = [obj.to_dictionary() for obj in list_objs]
            file.write(cls.to_json_string(obj_list))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        from models.rectangle import Rectangle
        from models.square import Square

        if cls is Rectangle:
            obj = Rectangle(2, 2)
        elif cls is Square:
            obj = Square(4)
        else:
            obj = None
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """also you can use path from os"""
        try:
            with open(f"{cls.__name__}.json", "r", encoding="utf-8") as file:
                dicts = cls.from_json_string(file.read())
        except FileNotFoundError:
            return []
        else:
            return [cls.create(**dic) for dic in dicts]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Make a CVS class file represntation"""

        r_keys = ("id", "width", "height", "x", "y")
        s_keys = ("id", "size", "x", "y")
        class_name = cls.__name__
        list_dict = (
            [*map(lambda self: self.to_dictionary(), list_objs)]
            if list_objs else []
        )
        csv_list = []
        for inst_dict in list_dict:
            inst_list = []
            keys_list = inst_dict.keys()
            for key in s_keys if class_name == "Square" else r_keys:
                if key in keys_list:
                    inst_list.append(str(inst_dict[key]))
            if inst_list:
                csv_list.append(inst_list)

        with open(f"{class_name}.csv", "w") as f:
            if list_objs:
                if class_name == "Square":
                    f.write(",".join(s_keys) + "\n")
                elif class_name == "Rectangle":
                    f.write(",".join(r_keys) + "\n")
                for row in csv_list:
                    f.write(",".join(row) + "\n")
            else:
                f.write("[]")

    @classmethod
    def load_from_file_csv(cls):
        """Load a class from a CVS class file represntation"""
        class_name = cls.__name__
        try:
            with open(f"{class_name}.csv", "r") as f:
                inst_list = []
                for line in f:
                    if "id" in line:
                        continue
                    obj = cls(1) if class_name == "Square" else cls(1, 1)
                    obj.update(*map(int, line.split(",")))
                    inst_list.append(obj)
                return inst_list
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        import turtle
        import time
        from random import randrange
        turtle.Screen().colormode(255)
        for i in list_rectangles + list_squares:
            t = turtle.Turtle()
            t.color((randrange(255), randrange(255), randrange(255)))
            t.pensize(1)
            t.penup()
            t.pendown()
            t.setpos((i.x + t.pos()[0], i.y - t.pos()[1]))
            t.pensize(10)
            t.forward(i.width)
            t.left(90)
            t.forward(i.height)
            t.left(90)
            t.forward(i.width)
            t.left(90)
            t.forward(i.height)
            t.left(90)
            t.end_fill()

        time.sleep(5)
