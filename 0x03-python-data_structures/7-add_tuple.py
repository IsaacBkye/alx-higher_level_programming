#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = createTuple(tuple_a)
    tuple_b = createTuple(tuple_b)
    return ((tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]))


def createTuple(tupl=()):
    length = len(tupl)
    if (length == 0):
        return ((0, 0))
    if (length == 1):
        tupl = list(tupl)
        tupl.append(0)
        tupl = tuple(tupl)
    return (tupl)
