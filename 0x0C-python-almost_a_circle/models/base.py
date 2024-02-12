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
        with open(f"{cls.__name__}.json", "w", encoding="utf-8") as file:
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
        from models.rectangle import Rectangle
        from models.square import Square

        if cls is Rectangle:
            list_objs = [[obj.id, obj.width, obj.height, obj.x, obj.y]
                            for obj in list_objs]
        elif cls is Square:
            list_objs = [[o.id, o.size, o.x, o.y]
                            for o in list_objs]
        with open(f"{cls.__name__}.csv", 'w', newline='',
                  encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        from models.rectangle import Rectangle
        from models.square import Square
        rt = []
        with open(f"{cls.__name__}.csv", 'r', newline='',
                  encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                row = [int(r) for r in row]
                if cls is Rectangle:
                    d = {"id": row[0], "width": row[1], "height": row[2],
                         "x": row[3], "y": row[4]}
                else:
                    d = {"id": row[0], "size": row[1],
                         "x": row[2], "y": row[3]}
                rt.append(cls.create(**d))
        return rt

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
