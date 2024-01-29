#!/usr/bin/python3
"""module for divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """ divides all elements of a matrix"""
    errormsg = "matrix must be a matrix (list of lists) of integers/floats"
    if not matrix:
        raise TypeError(errormsg)
    if not isinstance(matrix, list):
        raise TypeError(errormsg)
    for rows in matrix:
        if not isinstance(rows, list):
            raise TypeError(errormsg)
        for colums in rows:
            if not isinstance(colums, (int, float)):
                raise TypeError(errormsg)
    for rows in matrix:
        if len(rows) == 0:
            raise TypeError(errormsg)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not all(len(rows) == len(matrix[0]) for rows in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(colums / div, 2) for colums in rows] for rows in matrix]


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
