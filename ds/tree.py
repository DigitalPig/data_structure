'''
This is the tree module
'''
import math
from ds.queue import Queue

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


class BinarySearchTree():

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
                node.leftChild.parent = node
            else:
                self._put(node.hasLeftChild(), key, obj)
        else:
            if right is None:
                node.rightChild = TreeNode(key, obj)
                node.rightChild.parent = node
            else:
                self._put(node.hasRightChild(), key, obj)

    def __setitem__(self, key, obj):
        self.put(key, obj)

    def get(self, key):
        '''
        Search for an item in a BinarySearchTree
        '''
        if self.root is None:
            return None
        elif self.root.key == key:
            return self.root.payload
        else:
            if self._get(self.root, key) is None:
                return None
            else:
                return self._get(self.root, key).payload

    def _get(self, node, key):
        '''
        Recursively look for item
        '''
        if node is None:
            return None
        if node.key == key:
            return node
        left = node.leftChild
        right = node.rightChild
        if (left is None) and (right is None):
            if node.key != key:
                return None
            else:
                return node
        elif key < node.key:
            return self._get(node.leftChild, key)
        else:
            return self._get(node.rightChild, key)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self.root is None:
            return False
        elif self.root.key == key:
            return True
        else:
            return self._get(self.root, key) is not None

    def __str__(self):
        '''
        Print the whole tree out
        This function still needs extensive work to make it work
        '''

        def calc_offset(node):
            if node.hasLeftChild() is not None:
                return node.str_length // 2 + calc_offset(node.hasLeftChild())
            else:
                return 1

        def offset_print(node, offset):
            if node is None:
                return ''
            else:
                string = offset_print(node.hasRightChild(), offset + node.str_length) + '\n' + \
                         ''.join([' '] * offset) + node.__str__() + '\n' + \
                         offset_print(node.hasLeftChild(), offset + node.str_length)
                return string

        if self.root is None:
            return ''
        else:
            offset = calc_offset(self.root)
            return offset_print(self.root, offset)

    def delete(self, key):
        '''
        Delete the key from the Binary Search Tree
        '''

        def find_max(node):
            '''
            Helper function to find the successor for a node that is being
            deleted.
            '''
            if node.hasRightChild() is not None:
                return find_max(node.hasRightChild())
            else:
                return node

        def isolate_node(node):
            '''
            Helper function to isolate out the node
            '''
            if node.isLeaf():
                if node.isLeftChild():
                    node.parent.leftChild = None
                else:
                    node.parent.rightChild = None
            elif node.hasLeftChild():
                if node.isLeftChild():
                    node.parent.leftChild = node.hasLeftChild()
                else:
                    node.parent.rightChild = node.hasLeftChild()
                node.hasLeftChild().parent = node.parent
            else:
                if node.isLeftChild():
                    node.parent.leftChild = node.hasRightChild()
                else:
                    node.parent.rightChild = node.hasRightChild()
                node.hasRightChild().parent = node.parent


        if self.root is None:
            raise IndexError('Cannot delete item from an empty BST!')
        if self.get(key) is None:
            raise IndexError('BST does not contain key {0}'.format(key))

        currentNode = self._get(self.root, key)
        if currentNode.isLeaf():
            if currentNode.isLeftChild():
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        elif (currentNode.hasLeftChild() and (currentNode.hasRightChild() is None) or
              currentNode.hasRightChild() and (currentNode.hasLeftChild() is None)):
            if currentNode.hasLeftChild():
                new_current = currentNode.hasLeftChild()
            else:
                new_current = currentNode.hasRightChild()
            if currentNode.isLeftChild:
                currentNode.parent.leftChild = new_current
                new_current.parent = currentNode.parent
            elif currentNode.isRightChild:
                currentNode.parent.rightChild = new_current
                new_current.parent = currentNode.parent
            else:
                currentNode.replaceNodeData(new_current.key, new_current.payload,
                                            new_current.hasLeftChild(), new_current.hasRightChild())
        else:
            # Now we are dealing with both children cases
            successor = find_max(currentNode.hasLeftChild())
            isolate_node(successor)
            currentNode.replaceNodeData(successor.key, successor.payload, currentNode.hasLeftChild(), currentNode.hasRightChild())

class TreeNode:
    def __init__(self,key,val,left=None,right=None,
                                       parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
        self.str_length = len(str(self.key) + ':' + str(self.payload)) + 2

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

    def __str__(self):
        '''
        Representation of TreeNode
        '''

        total_length = self.str_length
        node_str = '[{key}:{value}]'.format(key=self.key, value=self.payload)
        # node_str = \
        # '''+{{top:-^{length}}}+
        # |   [{{key}}:{{value}}]   |
        # +{{bottom:-^{length}}}+'''.format(length=total_length).format(top='-', bottom='-',key=self.key, value=self.payload)
        return node_str
