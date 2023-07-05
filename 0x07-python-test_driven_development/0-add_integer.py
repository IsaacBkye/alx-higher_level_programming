#!/usr/bin/python3
'''
   0-add_integer is a function that adds two integers
'''
def add_integer(a, b=98):
    '''
    Sums two integers, a&b are either  int or float
    '''
    if type(a) is int or type(a) is float:
        if type(b) is int or type(b) is float:
            return int(a) + int(b)
        else:
            raise TypeError('b must be an integer')
    else:
        raise TypeError('a must be an integer')
