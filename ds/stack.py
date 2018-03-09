'''
Class to implement stack data structure

Usage:

1. `Stack()` is to create a new stack object
2. `push(item)` is to push a new item into the stack
3. `pop()` is to remove the first item in the stack and return to user
4. `peek()` is to return the first item in the stack but do not remove the item
5. `isEmpty()` test if the stack is empty or not
6. `size()` returns the length of the stack

'''

class Stack():
    '''
    Stack class to hold elements for stack. Stack is a data structure basically holds stack
    object.

    Parameters:
    -----------
    None
    '''

    def __init__(self):
        '''
        Initialization of the class
        '''
        self._contents = [] # The implementation will be heavily relies on python list.
        self._empty = True

    def push(self, item):
        '''
        Push an item into the stack. The item would be sitting on top of the stack

        Parameters:
        -----------
        item: T. object to be pushed into the stack
        '''

        self._contents.append(item)
        if self._empty:
            self._empty = False

    def pop(self):
        '''
        Poping out item.

        Parameters:
        ----------------
        None

        Returns:
        ----------------
        Item at the top of stack
        '''

        if self._empty:
            raise TypeError('Cannot pop an empty stack')
        item = self._contents.pop()
        if len(self._contents) == 0:
            self._empty = True
        return item

    def peek(self):
        '''
        Peek at the top of the stack

        Parameters:
        ----------------
        None

        Returns:
        ________________
        Item at the top of stack
        '''
        if self._empty:
            return IndexError('Cannot peek at the empty stack')

        index = len(self._contents)
        return self._contents[index - 1]

    @property
    def isEmpty(self):
        '''
        Return if stack is empty of not
        '''
        return self._empty

    def size(self):
        '''
        Return the size of the stack.
        '''

        return len(self._contents)
