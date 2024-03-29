#!/usr/bin/python3
"""this module for Base class"""
import json
import turtle


class Base:
    """base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initalization"""

        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Make a JSON class file represntation"""

        if list_objs is not None:
            list_objs = [o.to_dictionary() for o in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """Make a list of JSON class file represntation"""

        if json_string:
            return json.loads(json_string)
        else:
            return []

    @classmethod
    def create(cls, **dictionary):
        """Create instanse from a dictionary"""
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
        """Create instanse from a json file"""
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
        cursor = turtle.Turtle()
        cursor.color("blue", "red")
        cursor.penup()
        cursor.left(180)
        cursor.forward(50)
        cursor.pendown()
        for rect in list_rectangles:
            width = rect.width
            height = rect.height
            cursor.begin_fill()
            cursor.forward(width)
            cursor.right(90)
            cursor.forward(height)
            cursor.right(90)
            cursor.forward(width)
            cursor.right(90)
            cursor.forward(height)
            cursor.penup()
            cursor.right(180)
            cursor.forward(height + 10)
            cursor.left(90)
            cursor.pendown()
            cursor.end_fill()

        cursor.penup()
        cursor.goto(0, 0)
        cursor.left(180)
        cursor.forward(50)
        cursor.pendown()

        for square in list_squares:
            size = square.size
            cursor.begin_fill()
            for i in range(3):
                cursor.forward(size)
                cursor.left(90)
            cursor.forward(size)
            cursor.penup()
            cursor.right(180)
            cursor.forward(size + 10)
            cursor.right(90)
            cursor.pendown()
            cursor.end_fill()
        cursor.penup()
        cursor.goto(0, 0)
        cursor.left(90)
        turtle.done()
