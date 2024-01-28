#!/usr/bin/python3
"""module for divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix"""
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for colum in row:
            if not isinstance(colum, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(matrix[0]) != len(matrix[1]):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div is 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for row in matrix:
        new_matrix.append(list(map(lambda x: round(x / div, 2), row)))
    return new_matrix
