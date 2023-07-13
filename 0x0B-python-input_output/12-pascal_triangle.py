#!/usr/bin/python3


"""Module for Pascal Traingle"""


def pascal_triangle(n):
    """Function for Pascal Triangle"""
    if n <= 0:
        return []

    myList = [[1]]
    for i in range(1, n):
        row = [1]
        for elem in range(1, i):
            row.append(myList[i - 1][elem - 1] + myList[i - 1][elem])
        row.append(1)
        myList.append(row)
    return myList
