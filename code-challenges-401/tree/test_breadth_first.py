from tree import BinarySearchTree


def test_preorder_traversal():
    tree = BinarySearchTree()
    tree.add(2)
    tree.add(7)
    tree.add(5)
    tree.add(2)
    tree.add(6)
    tree.add(9)
    tree.add(5)
    tree.add(11)
    tree.add(14)

    expected = [2, 7, 5, 2, 6, 5, 9, 11, 14]
    #  = [2, 7, 2, 6, 5, 11, 5, 9, 4]
    result = []
    result = tree.get_pre_order_data() 

    assert result == expected


def test_in_order():
    tree = BinarySearchTree()
    tree.add(2)
    tree.add(7)
    tree.add(5)
    tree.add(2)
    tree.add(6)
    tree.add(9)
    tree.add(5)
    tree.add(11)
    tree.add(14)

    expected = [2, 2, 5, 5, 6, 7, 9, 11, 14]
    result = []
    result = tree.get_in_order_data() 

    assert result == expected

def test_post_order():
    tree = BinarySearchTree()
    tree.add(2)
    tree.add(7)
    tree.add(5)
    tree.add(2)
    tree.add(6)
    tree.add(9)
    tree.add(5)
    tree.add(11)
    tree.add(14)

    expected = [2, 5, 6, 5, 14, 11, 9, 7, 2]

    result = []
    result = tree.get_post_order_data() 

    assert result == expected