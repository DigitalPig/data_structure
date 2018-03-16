'''
Test module for linked list
'''

from ds import UnorderedList
import pytest

def test_initialization():
    test = UnorderedList()

def test_add_to_blank_list():
    test = UnorderedList()
    test.append(1)
    assert(test.size() == 1)
    assert(test.index(0) == 1)

def test_search_list():
    test = UnorderedList()
    test.append(1)
    test.append(2)
    assert(test.search(1) == 0)
    assert(test.search(2) == 1)
    assert(test.search(3) == False)

def test_empth_list_search():
    test = UnorderedList()
    with pytest.raises(Exception):
        test.search(1)

def test_size_list():
    test = UnorderedList()
    test.append(1)
    assert(test.size() == 1)

def test_list_index():
    test = UnorderedList()
    test.append(1)
    test.append(2)
    test.append(3)
    assert(test.index(2) == 3)
    with pytest.raises(IndexError):
        test.index(-1)
        test.index(5)

def test_list_remove():
    test = UnorderedList()
    test.append(1)
    test.remove(0)
    assert(test.size() == 0)
    test.append(1)
    test.append(2)
    test.remove(1)
    assert(test.index(0) == 1)
