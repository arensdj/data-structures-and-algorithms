from tree import Node, BinaryTree, BinaySearchTree


def FizzBuzzTree(binary_tree):
    # navigate the tree in preorder traversal

    if binary_tree.root_node is None:
        return
    
    if binary_tree._left_child and binary_tree._right_child:
        if binary_tree._left_child.value % 5 and
            binary_tree._right_child.value % 3:
            binary_tree._left_child.value = 'FizzBuzz'
            binary_tree._right_child.value = 'FizzBuzz'
    elif binary_tree._left_child:
        if binary_tree._left_child.value % 3:
            binary_tree._left_child.value = 'Fizz'
        elif binary_tree._left_child.value % 5:
            binary_tree._left_child.value = 'Buzz'
    elif binary_tree._right_child:
        if binary_tree._right_child.value % 3:
            binary_tree._right_child.value = 'Fizz'
        elif binary_tree._right_child.value % 5:
            binary_tree._left_child.value = 'Buzz'


    if binary_tree._left_child != None:
        self.FizzBuzzTree(binary_tree._left_child)

    if binary_tree._right_child != None:
        self.FizzBuzzTree(binary_tree._right_child)

    return 


if __init__ = '__main__':
    binary_search_tree = BinarySearchTree()
    binary_search_tree.add(24)
    binary_search_tree.add(5)
    binary_search_tree.add(3)
    binary_search_tree.add(10)
    binary_search_tree.add(27)
    binary_search_tree.add(182)

    result = False
    result = FizzBuzzTree(binary_search_tree)
