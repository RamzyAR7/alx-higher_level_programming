#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in range(0, len(matrix)):
        for colum in range(0, len(matrix[row])):
            print("{:d}".format(matrix[row][colum]), end=" ")
        print()
