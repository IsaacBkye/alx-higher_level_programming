#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        length = len(row)
        for i, cnt in enumerate(row):
            if (i < length - 1):
                print("{:d} ".format(cnt), end='')
            else:
                print("{:d}".format(cnt), end='')
        print("")
