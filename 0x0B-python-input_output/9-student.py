#!/usr/bin/python3
"""
this module for Student class
"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Instantiation """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ return dict of all attribute as key & value"""
        return self.__dict__
