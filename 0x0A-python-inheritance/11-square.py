#!/usr/bin/python3
"""
this module for class Square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class
    """
    def __init__(self, size):
        """init func"""
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """Square area"""
        return self.__size*self.__size

    def __str__(self):
        """str func"""
        return f"[Square] {self.__size}/{self.__size}"
