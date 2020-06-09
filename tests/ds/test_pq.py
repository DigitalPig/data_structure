'''
Test the priority queue
'''

from ds.pq import PriorityQueue

def test_basic_operations():
    p = PriorityQueue()
    p.add([1, 't'])
    p.add([2, 'a'])
    p.add([0, 'm'])
    assert [1, 't'] in p
    smallest = p.pop()
    assert smallest == [0, 'm']

def test_make_sure_duplicate_items_dont_compare():
    p = PriorityQueue()
    p.add([1, 'c'])
    p.add([1, 'a'])
    p.add([1, 'b'])
    smallest = p.pop()
    assert smallest == [1, 'c']


def test_update():
    p = PriorityQueue()
    p.add([2, 'b'])
    p.add([1, 'c'])
    p.add([3, 'a'])
    p.update('a', 0)
    assert p.pop() == [0, 'a']
