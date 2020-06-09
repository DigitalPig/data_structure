'''
Piority Queue Implementation
'''

import heapq
from itertools import count
from typing import List

class PriorityQueue():
    '''
    Priority Queue implementation using the min heap definition
    '''

    def __init__(self, each_size=2):
        self.counter = count()
        self.contents = []
        self.each_size = each_size

    def add(self, element):
        '''
        adding an element to the queue
        '''
        if len(element) != self.each_size:
            raise ValueError(f"elements needs to have length of {self.each_size} but now has {len(element)}.")
        # The first sub component is the value needed for sort
        value = element[0]
        counts = next(self.counter)
        new_element = [value, counts] + element[1:]
        heapq.heappush(self.contents, new_element)

    def pop(self):
        curr_min = heapq.heappop(self.contents)
        curr_min.pop(1) # Getting rid of the counter
        return curr_min

    def __iter__(self):
        for v in self.contents:
            real_v = v[0:1] + v[2:]
            yield real_v

    def update(self, key, value):
        idx = None
        for i, v in enumerate(self.contents):
            if v[-1] == key:
                idx = i
                break
        if idx:
            obj = self.contents.pop(i)
            obj[0] = value
            heapq.heappush(self.contents, obj)
        else:
            raise KeyError(f"Content {key} is not in the priority queue.")


