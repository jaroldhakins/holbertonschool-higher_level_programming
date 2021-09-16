#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
        cop_matrix = []
        for i in matrix:
                cop_matrix.append(list(map(lambda i: i**2, i)))
        return cop_matrix
