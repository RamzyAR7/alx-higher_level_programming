#!/usr/bin/python3
"""
this module for class BaseGeometry
"""


class BaseGeometry:
    """class BaseGeometry"""
    def area(self):
        """
        Public instance method: def area(self): that raises an Exception
        with the message area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method: def integer_validator(self, name, value):
        that validates value: you can assume name is always a string
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
