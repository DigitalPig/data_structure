'''
Linked list module

Note: this module is only for algorithm study purpose. Python's
implementation of linked list is really great and no need
to use this class here.
'''

class Item():
    '''
    This class provides the content of the linked list
    '''

    def __init__(self, obj):
        self._content = obj
        self._next_node = None
        self._prev_node = None

    def __str__(self):
        return self._content.__str__()

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, item):
        self._content = item

    @property
    def next_node(self):
        return self._next_node

    @next_node.setter
    def next_node(self, next_item):
        self._next_node = next_item

    @property
    def prev_node(self):
        return self._prev_node

    @prev_node.setter
    def prev_node(self, prev_item):
        self._prev_node = prev_item

class UnorderedList():
    '''
    This is the class for the unordered link list
    '''

    def __init__(self):
        '''
        Initialization of unordered linked list
        '''
        self.head = None
        self.tail = None

    def append(self, value):
        node = Item(value)
        if self.head is None:
            # Currently the empty list
            self.head = node
            self.tail = node
        else:
            p_node = self.tail
            self.tail.next_node = node
            self.tail = node
            self.tail.prev_node = p_node

    def search(self, value):
        '''
        Search for the content of the linked list
        '''
        found = False
        if self.head is None:
            raise ValueError('Unordered List is empty! Cannot search')
        current = self.head
        pos = 0
        while (not found) and (current is not None):
            if current.content == value:
                return pos
            else:
                current = current.next_node
                pos += 1

        # Not found after looping over the whole list
        return False

    def size(self):
        '''
        Return the size of the list
        '''
        if self.head == None:
            return 0
        else:
            current = self.head
            size = 0
            while current is not None:
                size += 1
                current = current.next_node
        return size

    def _index(self, pos):
        '''
        Return the position of content
        '''
        if self.head == None:
            raise ValueError("Cannot index element in an empty list!")

        if pos < 0:
            raise IndexError("Out of bound of index")
        if pos == 0:
            return self.head

        current = self.head
        while current is not None:
            if pos == 0:
                return current
            else:
                pos -= 1
                current = current.next_node

        raise IndexError("Out of bound error!")

    def index(self, pos):
        node = self._index(pos)
        return node.content

    def remove(self, pos):
        '''
        The most difficult function for unordered linked list
        '''
        if self.head is None:
            raise IndexError("Cannot remove element from an empty list")
        if pos == 0:
            current = self.head
            self.head = current.next_node
            del current
            if self.head is not None:
                self.head.prev_node = None
        else:
            try:
                node_to_remove = self._index(pos)
                node_to_remove.prev_node.next_node = node_to_remove.next_node
                if node_to_remove.next_node is None:
                    self.tail = node_to_remove.prev_node
                else:
                    node_to_remove.next_node.prev_node = node_to_remove.prev_node
                del node_to_remove
            except IndexError as e:
                raise e
