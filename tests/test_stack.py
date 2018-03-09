'''
Test Stack module
'''

from ds import Stack


def test_stack_push():
    test = Stack()
    test.push(1)
    test.push(2)
    assert(len(test._contents) == 2)
    assert(test._contents[0] == 1)

def test_stack_pop():
    test = Stack()
    test.push('a')
    test.push('b')
    assert (test.pop() == 'b')
    assert (len(test._contents) == 1)

def test_stack_peek():
    test = Stack()
    test.push(1)
    test.push(2)
    test.push(3)
    assert(test.peek() == 3)

def test_stack_isEmpty():
    test = Stack()
    assert(test.isEmpty == True)
    test.push(1)
    assert(test.isEmpty == False)
    test.pop()
    assert(test.isEmpty == True)
