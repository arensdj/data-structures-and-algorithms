from tree import BinarySearchTree
from fizz_buzz_tree import FizzBuzzTree


  
# def test_exists():
#     assert BinarySearchTree
#
# def test_instance():
#     tree = BinarySearchTree()
#     assert tree
#
# def test_insert_one():
#     tree = BinarySearchTree()
#     tree.add(15)
#     assert tree.binary_tree.root_node.value == 15

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
    bst.add(3)

    tree = FizzBuzzTree(None, bst)

    assert tree.binary_tree.root_node.value == 'FizzBuzz'
    assert tree.binary_tree.root_node._right_child.value == 'Buzz'
    assert tree.binary_tree.root_node._left_child.value == 'Fizz'