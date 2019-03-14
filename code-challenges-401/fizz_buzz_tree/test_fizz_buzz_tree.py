from tree import BinarySearchTree
from fizz_buzz_tree import FizzBuzzTree

def test_insert_another():
    tree = BinarySearchTree()
    tree.add(27)
    tree.add(18)
    tree.add(54)

    assert tree.binary_tree.root_node.value == 27
    assert tree.binary_tree.root_node._left_child.value == 18
    assert tree.binary_tree.root_node._right_child.value == 54

def test_fizz_buzz():
    bst = BinarySearchTree()
    bst.add(30)
    bst.add(5)
    bst.add(33)

    tree = FizzBuzzTree(None, bst)
    current_node = tree.binary_tree.root_node

    assert tree.binary_tree.root_node.value == 'FizzBuzz'
    assert tree.binary_tree.root_node._right_child.value == 'Fizz'
    assert tree.binary_tree.root_node._left_child.value == 'Buzz'

def test_fizz_buzz():
    bst = BinarySearchTree()
    bst.add(30)
    bst.add(2)
    bst.add(20)
    bst.add(33)

    tree = FizzBuzzTree(None, bst)
    current_node = tree.binary_tree.root_node

    assert tree.binary_tree.root_node.value == 'FizzBuzz'
    assert tree.binary_tree.root_node._left_child.value == 2
    assert tree.binary_tree.root_node._left_child._right_child.value == 'Buzz'
    assert tree.binary_tree.root_node._right_child.value == 'Fizz'
