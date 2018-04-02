'''
This is the tree module
'''

class Node():
    def __init__(self, value, left=None, right=None):
        '''
        Initialize the node with left and right children
        '''
        self._left = left
        self._right = right
        self._value = value

    def __str__(self):
        '''
        Represent the string of the content
        '''
        return 'value: {0}, left: {1} -- right : {2}'.format(self._value.__str__(),
                                                             self.left.__str__(),
                                                             self.right.__str__())

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, content):
        self._left = content

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, content):
        self._right = content

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, obj):
        self._value = obj

    def __eq__(self, other):
       return self._value == other._value


class BinaryTree():
    def __init__(self, obj):
        self._root = Node(obj)
        self.level = 0

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, obj):
        self._root = Node(obj)

    def add_left_node(self, obj):
        '''
        Adding to the left node of the root
        '''

        start_node = self._root

        while start_node.left is not None:
            start_node = start_node.left

        start_node.left = Node(obj)

    def add_right_node(self, obj):
        '''
        Adding to the right node of the root
        '''
        start_node = self._root
        while start_node.right is not None:
            start_node = start_node.right

        start_node.right = Node(obj)
