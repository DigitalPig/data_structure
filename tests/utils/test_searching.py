from utils import binary_search

def test_search_for_in_list():
    test = [1, 2, 3, 4]
    assert(binary_search(test, 4) == True)

def test_search_not_in_list():
    test = [1, 2, 3, 4]
    assert(binary_search(test, 5) == False)

def test_search_middle_point():
    test = [1, 2, 3, 4, 5]
    assert(binary_search(test, 3) == True)
