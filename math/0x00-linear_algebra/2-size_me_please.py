#!/usr/bin/env python3
"""matrix shape calculation"""


def matrix_shape(matrix):
    '''matrix shape'''
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape
