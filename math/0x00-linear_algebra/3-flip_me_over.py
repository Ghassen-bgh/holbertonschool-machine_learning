#!/usr/bin/env python3

def matrix_transpose(matrix):
    # Get the number of rows and columns in the matrix
    rows = len(matrix)
    columns = len(matrix[0])

    # Create a new matrix with dimensions swapped
    transpose_matrix = [[0 for _ in range(rows)] for _ in range(columns)]

    # Populate the transpose matrix with elements from the original matrix
    for i in range(rows):
        for j in range(columns):
            transpose_matrix[j][i] = matrix[i][j]

    return transpose_matrix
