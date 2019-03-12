from tree import BinarySearchTree

def test_exists():
    assert BinarySearchTree

def test_instance():
    tree = BinarySearchTree()
    assert tree

def test_insert_one():
    tree = BinarySearchTree()
    tree.add(15)
    assert tree.binary_tree.root_node.value == 15

def test_insert_another():
    tree = BinarySearchTree()
    tree.add(27)
    tree.add(18)
    tree.add(54)

    assert tree.binary_tree.root_node.value == 27
    assert tree.binary_tree.root_node._left_child.value == 18
    assert tree.binary_tree.root_node._right_child.value == 54

def test_insert_grandchild():
    tree = BinarySearchTree()
    tree.add(99)
    tree.add(128)
    tree.add(56)
    tree.add(70)

    assert tree.binary_tree.root_node._left_child._right_child.value == 70

def test_insert_grandchild():
    tree = BinarySearchTree()
    tree.add(99)
    tree.add(128)
    tree.add(56)
    tree.add(70)

    assert tree.contains(99)
    assert tree.contains(70)

def test_not_contains():
    tree = BinarySearchTree()
    tree.add(99)
    tree.add(128)
    tree.add(56)
    tree.add(70)

    assert not tree.contains(7)

def test_inorder_traversal():
    tree = BinarySearchTree()
    tree.add(99)
    tree.add(128)
    tree.add(56)
    # tree.add(70)

    expected = ['56','99','128']
    result = []
    result = tree.get_in_order_data() 

    assert result == expected


