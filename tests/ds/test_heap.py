'''Module to test heap functionality'''


from ds.heap import BinaryHeap

def test_binary_heap_init():
    test = BinaryHeap()
    assert(isinstance(test, BinaryHeap))
    assert(test.content[0] == 0)
    assert(test.size == 0)


def test_binary_heap_percolate():
    test = BinaryHeap()
    test.content = [0, 5, 9, 11, 14, 18, 19, 21, 33, 17, 27]
    test.currentSize = 10
    test.insert(7)
    assert(test.content[2] == 7)


def test_binary_heap_delmin():
    test = BinaryHeap()
    test.content = [0, 5, 9, 11, 14, 18, 19, 21, 33, 17, 27]
    test.currentSize = 10
    result = test.delMin()
    assert(result == 5)
    test2 = BinaryHeap()
    test2.content = [0, 9, 14, 11, 17, 18, 19, 21, 33, 27]
    assert(test == test2)
