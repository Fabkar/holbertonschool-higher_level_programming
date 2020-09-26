#!/usr/bin/python3
"""
Function that divide each elements of a matix in an integer.


"""


def matrix_divided(matrix, div):
    """Divide each elements of a matrix in a number

    Args:
        matrix (int, float): [Elements of matrix must be an integer or float]
        div (int, float): [Divisor must be an integer or float]

    Raises:
        TypeError: [matrix elements different of int, float]
        TypeError: [different size of row]
        TypeError: [div must be a number ]
        ZeroDivisionError: [Can't divide by 0]

    Returns:
        [int, float]: [matrix divided]
    """
    n_matrix = []
    for i in matrix:
        for x in i:
            if type(x) not in [int, float]:
                raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
        if type(i) is not list:
            raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
        if len(i) != len(matrix[0]):
            raise TypeError("Each row of the \
matrix must have the same size")
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by Zero")
    n_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]
    return n_matrix
