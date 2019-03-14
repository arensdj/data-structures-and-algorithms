from tree import BinarySearchTree

def test_preorder_traversal():
    tree = BinarySearchTree()
    tree.add(25)
    tree.add(15)
    tree.add(35)
    tree.add(8)
    tree.add(19)
    tree.add(30)
    tree.add(45)

    expected = [25, 15, 8, 19, 35, 30, 45]

    result = []
    result = tree.get_pre_order_data() 

    assert result == expected

def test_breadth_order_traversal():
    tree = BinarySearchTree()
    tree.add(25)
    tree.add(15)
    tree.add(35)
    tree.add(8)
    tree.add(19)
    tree.add(30)
    tree.add(45)

    expected = [25, 15, 35, 8, 19, 30, 45]

    result = []
    # result = tree.binary_tree.breadth_first_traversal(None)
    result = tree.get_breadth_order_data()

    assert result == expected
