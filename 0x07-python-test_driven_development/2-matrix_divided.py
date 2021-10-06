#!/usr/bin/python3
'''
divide
all elements
in one matrix
'''


def matrix_divided(matrix, div):
    """
    divide a matrix
    """
    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    j = None
    for arr in matrix:
        size = len(arr)
        if j is not None:
            if j != size:
                raise TypeError(
                    "Each row of the matrix must have the same size")
        if type(arr) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        j = 0
        for i in arr:
            if type(i) is not int and type(i) is not float:
                raise TypeError(
                    "matrix must be a matrix (list of lists) of"
                    "integers/floats")
            j += 1
        if type(div) is not int and type(div) is not float:
            raise TypeError("div must be a number")
        if div == 0:
            raise ZeroDivisionError("division by zero")
    return [[round(i / div, 2) for i in arr] for arr in matrix]
