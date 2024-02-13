#!/usr/bin/python3
"""A module contain the Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initalization"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter method"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter method"""
        self.width = value
        self.height = value

    def __str__(self):
        """class string representation"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.size
        )

    def update(self, *args, **kwargs):
        """update class atrbutes"""
        keys = ("id", "size", "x", "y")
        for key, value in zip(keys, args):
            if key == "id" and not isinstance(value, int):
                continue
            setattr(self, key, value)
        if not args:
            for key, value in kwargs.items():
                if key == "id" and not isinstance(value, int):
                    continue
                setattr(self, key, value)

    def to_dictionary(self):
        """get dictionary copy of the class"""
        class_dict = {}
        keys = ("id", "size", "x", "y")
        for key in keys:
            class_dict[key] = getattr(self, key)
        return class_dict
