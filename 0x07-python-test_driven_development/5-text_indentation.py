#!/usr/bin/python3
'''
   5-text_indentation adds new line after characters
'''
def text_indentation(text):
    '''Adds two new lines to string at character points
    '''
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    ind = text.replace('.', '.\n\n')
    ind = period.replace('?', '?\n\n')
    ind = period.replace(':', ':\n\n')
    ind1 = period.split('\n')
    for line in range(len(ind1)):
        print("{}".format(ind1[line].strip()),
              end=("" if (line == (len(ind1) - 1)) else '\n'))
