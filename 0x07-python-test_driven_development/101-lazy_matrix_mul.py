#!/usr/bin/python3
""" This module contains a function that
multiplies 2 matricies using numpy module """
import numpy


def lazy_matrix_mul(m_a, m_b):
    """ This function multiply 2 matricies using numpy module """
    return numpy.matmul(m_a, m_b)
