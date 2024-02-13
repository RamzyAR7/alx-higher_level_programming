#!/usr/bin/python3
"""A module contain the Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initalization"""
        super().__init__(id)
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif type(height) is not int:
            raise TypeError(f"height must be an integer")
        elif type(x) is not int:
            raise TypeError("x must be an integer")
        elif type(y) is not int:
            raise TypeError("y must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        elif height <= 0:
            raise ValueError("height must be > 0")
        elif x < 0:
            raise ValueError("x must be >= 0")
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Getter method"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter method"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter method"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter method"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter method"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return the rectangle area"""
        return self.__width * self.__height

    def display(self):
        """print the rectangle"""
        print("\n" * self.__y, end="")
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """class string representation"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.__x, self.__y, self.__width, self.__height
        )

    def update(self, *args, **kwargs):
        """update class atrbutes"""
        keys = ("id", "width", "height", "x", "y")
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
        keys = ("id", "width", "height", "x", "y")
        for key in keys:
            class_dict[key] = getattr(self, key)
        return class_dict
