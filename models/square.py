#!/usr/bin/python3
"""
this module for Square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[{self.__class__.__name__}] \
({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """update if you use args"""
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                match key:
                    case "id":
                        self.id = value
                    case "size":
                        self.size = value
                    case "x":
                        self.x = value
                    case "y":
                        self.y = value

    def to_dictionary(self):
        return {"id": self.id, "size": self.size,
                "x": self.x, "y": self.y}
