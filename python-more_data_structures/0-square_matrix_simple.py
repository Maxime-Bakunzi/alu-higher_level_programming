#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """computes the square value of all integers
    of a matrix.

    Args:

    Returns:
        a new matrix is returned
    """
    new_matrix = [[col ** 2 for col in row] for row in matrix]
    return new_matrix
