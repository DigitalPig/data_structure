'''
Test Tree module
'''

from ds.tree import Node, BinaryTree

def test_node_init():
    test = Node(1)

def test_node_init_w_left_right():
    test = Node(1)
    assert(test.value == 1)
    assert(test.left is None)
    assert(test.right is None)

def test_node_left_property_setter():
    test = Node(1)
    test.left = Node(2)
    assert(test.left == Node(2))

def test_node_equal():
    test1 = Node(1)
    test2 = Node(1)
    assert(test1 == test2)

def test_binary_tree_init():
    test = BinaryTree(Node(1))
    assert(isinstance(test, BinaryTree))

def test_binary_tree_with_root():
    test = BinaryTree(1)
    assert(test.root == Node(1))


def test_binary_tree_add_left():
    test = BinaryTree(1)
    test.add_left_node(3)
    assert(test.root.right is None)
    assert(test.root.left == Node(3))
    test.add_left_node(4)
    assert(test.root.right is None)
    assert(test.root.left == Node(3))
    assert(test.root.left.left == Node(4))
    assert(test.root.left.right is None)

def test_binary_tree_add_right():
    test = BinaryTree(1)
    test.add_right_node(3)
    assert(test.root.left is None)
    assert(test.root.right == Node(3))
    test.add_right_node(4)
    assert(test.root.left is None)
    assert(test.root.right == Node(3))
    assert(test.root.right.right == Node(4))
    assert(test.root.right.left is None)
