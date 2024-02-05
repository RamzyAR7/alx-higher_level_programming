#!/usr/bin/python3
"""
this module for class BaseGeometry
"""


class BaseGeometry:
    """class BaseGeometry"""
    def area(self):
        """
        that raises an Exception
        with the message area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        that validates value: you can assume name is always a string
        """
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
