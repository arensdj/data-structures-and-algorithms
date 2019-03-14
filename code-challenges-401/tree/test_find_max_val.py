from tree import BinarySearchTree

def test_max_value_large_sample():
    bst = BinarySearchTree()
    bst.add(2)
    bst.add(7)
    bst.add(5)
    bst.add(2)
    bst.add(6)
    bst.add(9)
    bst.add(5)
    bst.add(11)
    bst.add(4)

    expected = 11
    result = bst.binary_tree.find_maximum_value()
    assert result == expected

def test_max_value_small_sample():
    bst = BinarySearchTree()
    bst.add(2)
    bst.add(7)
    bst.add(5)

    expected = 7
    result = bst.binary_tree.find_maximum_value()
    assert result == expected

def test_max_value_one():
    bst = BinarySearchTree()
    bst.add(2)

    expected = 2
    result = bst.binary_tree.find_maximum_value()
    assert result == expected

def test_max_value_empty_tree():
    bst = BinarySearchTree()

    expected = None
    result = bst.binary_tree.find_maximum_value()
    assert result == expected