#!/usr/bin/python3
"""A module contain the Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a Rectangle instance."""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Retrieves the width attribute."""

        return self.__width

    @property
    def height(self):
        """Retrieves the height attribute."""

        return self.__height

    @property
    def x(self):
        """Retrieves the x attribute."""

        return self.__x

    @property
    def y(self):
        """Retrieves the y attribute."""

        return self.__y

    @width.setter
    def width(self, value):
        """Sets the width attribute."""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Sets the height attribute."""

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Sets the x attribute."""

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Sets the y attribute."""

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
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
