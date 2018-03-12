'''
Testing for module queue
'''

from ds import Queue

def test_Queue_init():
    test = Queue()
    assert(test)

def test_enqueue():
    test = Queue()
    test.enqueue(3)
    assert(test._contents == [3])

def test_dequeue():
    test = Queue()
    test.enqueue(3)
    test.enqueue(4)
    assert(test.dequeue() == 3)
    assert(test.dequeue() == 4)


def test_queue_isEmpty():
    test = Queue()
    assert(test.isEmpty == True)
    test.enqueue(3)
    assert(test.isEmpty == False)
    test.dequeue()
    assert(test.isEmpty == True)

def test_size():
    test = Queue()
    test.enqueue(3)
    assert(test.size() == 1)
    test.enqueue(34)
    assert(test.size() == 2)
    test.dequeue()
    assert(test.size() == 1)
