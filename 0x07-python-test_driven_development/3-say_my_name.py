#!/usr/bin/python3
'''
   3-say_my_name prints names
'''
def say_my_name(first_name, last_name=""):
    '''
    Takes two strings and prints them
    '''
Emsg = 'first_name must be a string'
Emsg1 = 'last_name must be a string'
Fname = 'My name is '


def say_my_name(first_name, last_name=""):
    if not isinstance(first_name, str):
        raise TypeError(Emsg)
    if not isinstance(last_name, str):
        raise TypeError(Emsg1)
    else:
        print('My name is {} {}'.format(first_name, last_name))
