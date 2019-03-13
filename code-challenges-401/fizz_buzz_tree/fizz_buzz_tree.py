from tree import BinarySearchTree


def FizzBuzzTree(current_node, bst):
    # navigate the tree in preorder traversal
    
    fizz_buzz_tree = BinarySearchTree()

    if current_node is None:
        current_node = bst.binary_tree.root_node
    
    current_node.value = set_fizz_buzz(current_node.value)

    if current_node._left_child != None:
        FizzBuzzTree(current_node._left_child, bst)

    if current_node._right_child != None:
        FizzBuzzTree(current_node._right_child, bst)

    fizz_buzz_tree = bst
    return fizz_buzz_tree

def set_fizz_buzz(node_value):
    if node_value % 5 == 0 and node_value % 3 == 0:
        return 'FizzBuzz'
    elif node_value % 3 == 0:
        return 'Fizz'
    elif node_value % 5 == 0:
        return 'Buzz'
    else:
        return node_value

if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.add(30)
    bst.add(5)
    bst.add(3)

    new_bst = FizzBuzzTree(None, bst)
