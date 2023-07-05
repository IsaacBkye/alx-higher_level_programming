#!/usr/bin/python3
'''
    2-matrix_divided.py divides all elements of a matrix
'''


def matrix_divided(matrix, div):
    '''
    Function to divide a matrix by variable div
    '''
    listError = 'Matrix has to be a matrix (list of lists) of integers/floats'
    
    if type(matrix) is not list:
        raise TypeError(listError)

    for rows in matrix:
        if type(rows) is not list:
            raise TypeError(listError)

    for row in matrix:
        if len(matrix[0]) != len(row):
            raise TypeError('Each row of the matrix must have the same size')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    for rows in matrix:
        for items in rows:
            if not isinstance(items, (int, float)):
                raise TypeError(listError)

    Mnew = []
    for rows in matrix:
        if not isinstance(div, (int, float)):
            raise TypeError('div must be a number')
        else:
            Mnew.append([round((items / div), 2) for items in rows])
    return Mnew
