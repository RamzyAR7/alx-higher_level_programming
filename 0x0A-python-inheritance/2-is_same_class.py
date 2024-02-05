#!/usr/bin/python3
""" Module that contains a function 
that returns True if the object is exactly"""


def is_same_class(obj, a_class):
    """ Function that returns True if the object is 
    exactly an instance of the specified class"""

    return type(obj) == a_class
