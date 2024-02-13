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
    def size(self, size):
        """Setter method"""
        self.width = size
        self.height = size

    def __str__(self):
        '''Returns string info about this square.'''
        return f"[Square] ({self.id}) \
{self.x}/{self.y} - {self.size}"

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
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        return {"id": self.id, "size": self.size,
                "x": self.x, "y": self.y}
