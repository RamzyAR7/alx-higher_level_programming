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
        if attrs is None or not attrs:
            return self.__dict__
        if isinstance(attrs, list):
            js_dict = {}
            for x in attrs:
                if hasattr(self, x):
                    js_dict[x] = getattr(self, x)
        return js_dict
