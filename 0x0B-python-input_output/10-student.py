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

    def to_json(self, attrs=None):
        """ return dict of all attribute as key & value"""
        js_dict = {}
        for key, value in self.__dict__.items():
            if not isinstance(attrs, list) or key in attrs:
                js_dict[key] = value
        return js_dict
