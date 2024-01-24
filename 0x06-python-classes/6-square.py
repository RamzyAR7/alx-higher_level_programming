#!/usr/bin/python3
"""This module defines for a class Square"""


class Square:
    """This class is a Tamplate for a square"""
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int) or not isinstance(position, tuple):
            raise TypeError("""size must be an integer,
                            position must be a tuple of two integers""")
        elif size < 0 or position[0] < 0 or position[1] < 0:
            raise ValueError("size and position must be >= 0")
        else:
            self.__size = size
            self.__position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of two integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise ValueError("elements of position must be >= 0")
        else:
            self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                for _ in range(self.__position[0]):
                    print(" ",  end="")
                print("#" * (self.__size))
