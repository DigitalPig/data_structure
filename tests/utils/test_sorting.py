'''
Test sorting functions
'''

from utils import bubble_sort, selection_sort, insert_sort, merge_sort, quick_sort
import random
import pytest

@pytest.fixture
def test_array():
    return [random.randrange(1,100) for i in range(5)]

def test_bubble_sort(test_array):
    assert(bubble_sort(test_array) == sorted(test_array))

def test_selection_sort(test_array):
    assert(selection_sort(test_array) == sorted(test_array))

def test_insert_sort(test_array):
    assert(insert_sort(test_array) == sorted(test_array))

def test_merge_sort(test_array):
    assert(merge_sort(test_array) == sorted(test_array))

def test_quick_sort(test_array):
    assert(quick_sort(test_array) == sorted(test_array))

def test_quick_sort():
    assert(quick_sort([72, 34]) == sorted([72, 34]))
