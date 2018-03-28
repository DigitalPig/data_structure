'''
Test sorting functions
'''

from utils import bubble_sort, selection_sort, insert_sort
import random
import pytest

@pytest.fixture
def test_array():
    return [random.randrange(1,100) for i in range(100)]

def test_bubble_sort(test_array):
    assert(bubble_sort(test_array) == sorted(test_array))

def test_selection_sort(test_array):
    assert(selection_sort(test_array) == sorted(test_array))

def test_insert_sort(test_array):
    assert(insert_sort(test_array) == sorted(test_array))
