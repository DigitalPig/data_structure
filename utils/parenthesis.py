'''
This module is to use the stack method to check for parethesis balance.
'''

from ds import Stack

def check_balance(string):
    '''
    Check to see if we have balanced parethesis.

    Parameters:
    -----------
    string: str. The string contains the text with parenthesis that needs to be check balanced.

    Return:
    Boolean. Tell if parenthesis is matched or not
    '''

    parethesis = Stack()
    for s in string.strip():
        if s == '(':
            parethesis.push(s)
        elif s == ')':
            try:
                parethesis.pop()
            except TypeError:
                return False
    if parethesis.size() != 0:
        return False

    return True
