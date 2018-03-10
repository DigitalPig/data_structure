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
    par_dict = {')': '(', '}':'{', ']':'['}
    for s in string.strip():
        if s in par_dict.values():
            parethesis.push(s)
        elif s in par_dict.keys():
            try:
                t = parethesis.pop()
                if t != par_dict[s]:
                    return False
            except TypeError:
                return False
    if parethesis.size() != 0:
        return False

    return True
