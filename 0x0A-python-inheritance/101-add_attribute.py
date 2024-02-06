#!/usr/bin/python3
""" Module for the add_attribute function """


def add_attribute(obj, attribute, value):
    """ Adds a new attribute to an object if possible """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attribute, value)
