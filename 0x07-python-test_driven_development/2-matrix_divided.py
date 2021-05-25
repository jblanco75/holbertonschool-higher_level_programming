#!/usr/bin/python3
"""Function: matrix_divided"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by
    a given number (div)"""

    if not matrix or type(matrix) != list:
        raise TypeError("matrix must be a matrix (list of lists) \
                         of integers/floats")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    new_matrix = []
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) \
                                  of integers/floats")
            new_matrix = [[round(i / div, 2) for i in row] for row in matrix]
    return new_matrix
