#!/usr/bin/python3
"""this module for pascal_triangle function"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle with n rows.
    """
    triangle = []

    for i in range(n):
        row = [1] * (i + 1)
        if i >= 2:
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle
