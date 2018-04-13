'''
Test Tree module
'''

from ds.tree import Node, BinaryTree, BinarySearchTree, TreeNode

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

def test_binary_search_tree_put():
    test = BinarySearchTree()
    test.put(2,'a')
    assert(test.root == TreeNode(2,'a'))
    test.put(1, 'b')
    assert(test.root.leftChild == TreeNode(1, 'b'))
    test.put(3, 'c')
    assert(test.root.rightChild == TreeNode(3, 'c'))
    test[4] = 'd'
    assert(test.root.rightChild.rightChild == TreeNode(4, 'd'))

def test_binary_search_tree_get():
    test = BinarySearchTree()
    test.put(2,'a')
    test.put(1, 'b')
    test.put(3, 'c')
    test[4] = 'd'
    assert(test[2] == 'a')
    assert(test[3] == 'c')

def test_binary_search_tree_contains():
    test = BinarySearchTree()
    test.put(2,'a')
    test.put(1, 'b')
    test.put(3, 'c')
    print(test[1])
    #test[4] = 'd'
    assert(2 in test)
    assert(not (7 in test))
    test2 = BinarySearchTree()
    assert(not (2 in test2))

def test_binary_search_tree_delete():
    test = BinarySearchTree()
    test.put(17, 'a')
    test.put(5, 'b')
    test.put(35, 'c')
    test.put(2,'d')
    test.put(11, 'e')
    test.put(9, 'k')
    test.put(16, 'j')
    test.put(8, 'l')
    test.put(29,'r')
    test.put(38, 't')
    test.delete(16)
    print(test)
    assert(test.get(16) is None)
    assert(test._get(test.root, 11).hasRightChild() is None)
    test.delete(35)
    print(test)
    assert(test.get(35) is None)
    assert(test.get(17).rightChild == test.get(29))
    assert(False == True)

