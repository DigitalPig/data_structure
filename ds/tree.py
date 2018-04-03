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


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, obj):
        '''
        Put an object into the BinarySearchTree
        '''
        if self.root is None:
            self.root = TreeNode(key, obj)
        else:
            self._put(self.root, key, obj)
        self.size += 1

    def _put(self, node, key, obj):
        left = node.hasLeftChild()
        right = node.hasRightChild()
        if key <= node.key:
            if left is None:
                node.leftChild = TreeNode(key, obj)
            else:
                self._put(node.hasLeftChild(), key, obj)
        else:
            if right is None:
                node.rightChild = TreeNode(key, obj)
            else:
                self._put(node.hasRightChild(), key, obj)

    def __setitem__(self, key, obj):
        self.put(key, obj)


class TreeNode:
    def __init__(self,key,val,left=None,right=None,
                                       parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

    def __eq__(self, other):
        return (self.key == other.key) and (self.payload == other.payload)
