'''
Test of parethesis matching
'''
from utils import check_balance

def test_empty_string():
    string = " "
    assert(check_balance(string) == True)

def test_matched_string():
    string = " (((1 df dfdr)))"
    assert(check_balance(string) == True)

def test_unmatched_string():
    string = "(((sdfsdfsd sdfds))"
    assert(check_balance(string) == False)

def test_multiple_line_string():
    string = """
    ((
    sdfd
      sdf ))

    """
    assert(check_balance(string) == True)
