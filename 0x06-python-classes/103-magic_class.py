#!/usr/bin/python3
"""Module for MagicClass"""


import math


class MagicClass:
    """A class that replicates the provided Python bytecode"""
    def __init__(self, radius=0):
        """Initializer for MagicClass"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        else:
            self.__radius = radius

    def area(self):
        """Calculate the area of the circle"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculate the circumference of the circle"""
        return 2 * math.pi * self.__radius
