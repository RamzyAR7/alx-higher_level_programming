#!/usr/bin/python3
"""
This module for class Rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class
    """
    def __init__(self, width, height):
        """init func"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """str func"""
        return f"[Rectangle] {self.__width} / {self.__height}"

    def area(self):
        """rectangle area"""
        return self.__width * self.__height
