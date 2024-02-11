#!/usr/bin/python3
"""
this module for Base class
"""


import json


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
        with open(f"{cls.__name__}.json", "w") as file:
            obj_list = [obj.to_dictionary() for obj in list_objs]
            file.write(cls.to_json_string(obj_list))

    @staticmethod
    def from_json_string(json_string):
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        from models.rectangle import Rectangle
        from models.square import Square

        if cls is Rectangle:
            obj = Rectangle(1, 1)
        elif cls is Square:
            obj = Square(1)
        else:
            obj = None
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        from os import path

        if not path.isfile(f"{cls.__name__}.json"):
            return []
        with open(f"{cls.__name__}.json", "r") as file:
            return [cls.create(**l) for l in cls.from_json_string(file.read())]
