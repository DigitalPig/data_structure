'''
Module to provide the Queue data structure
'''

class Queue():
    '''
    This is the class to define Queue data structure.
    Queue is data structure with FIFO type of data
    flow.

    Methods:
    --------------------
    Queue(): Initialize the queue
    enqueue(item): put one element into the queue
    dequeue(): Get the first item out from the queue
    isEmpty(): Return boolean if the queue empty or not
    size(): Return the size of the queue.
    '''

    def __init__(self):
        self._contents = []
        self._empty = True

    def enqueue(self, item):
        '''
        Enqueue an item into the queue

        Parameters:
        -----------
        item: T. Item to be in the queue.

        Return:
        -----------
        None
        '''
        self._contents.insert(0, item)
        if self._empty == True:
            self._empty = False

    def dequeue(self):
        '''
        Dequeue an element from the queue

        Parameters:
        -----------
        None.

        Return:
        -----------
        object at the top of queue.
        '''
        if self._empty:
            raise ValueError('Cannot dequeue an empty queue!')

        result = self._contents.pop()
        if len(self._contents) == 0:
            self._empty = True

        return result

    @property
    def isEmpty(self):
        '''
        Find out if the queue is empty or not

        Parameter:
        ----------
        None

        Return:
        ----------
        Boolean
        '''

        return self._empty

    def size(self):
        '''
        Get the size of the queue

        Parameters:
        ----------
        None

        Return:
        ----------
        Integer.
        '''

        return len(self._contents)

        
