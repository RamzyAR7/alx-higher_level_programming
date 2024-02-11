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
        
