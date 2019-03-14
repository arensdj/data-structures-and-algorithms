from tree import BinarySearchTree


def FizzBuzzTree(current_node, bst):
    """
    Summary of FizzBuzzTree function: given a binary search tree argument determines
    whether or not the value of each node is divisible by 3, 5 or both 3 and 5.
    Changes the node value to 'FizzBuzz' if value is divisible by 3 and 5.
    Changes the node value to 'Fizz' if the value is divisible by 3.
    Changes the node value to 'Buzz' if the value is divisible by 5.

    Parameters:
    current_node : value is None
    bst (BinarySearchTree): the current binary search tree

    Returns:
    A binary search tree with the new values.
    """
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
    """
    Summary of set_fizz_buzz function: Evaluates the value of node_value and
    returns either
      'FizzBuzz' if value is divisible by 3 and 5.
      'Fizz' if the value is divisible by 3.
      'Buzz' if the value is divisible by 5.

    Parameters:
    node_value (Node) : the current node

    Returns:
    Either 'FizzBuzz', 'Fizz' or 'Buzz'
    """
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
    bst.add(33)

    new_bst = FizzBuzzTree(None, bst)