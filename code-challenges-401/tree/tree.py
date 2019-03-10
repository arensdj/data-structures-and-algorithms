class Node():
    """
    Summary of Node class:  Class definition of a node which is an individual item. Each node contains the data for each item.

    Attributes:
    value (string) : a string value
    _left_node : a property of Node class that will reference the next Node object to the left of the root node.
    _right_node : a property of Node class that will reference the next Node object to the right of the root node.

    Returns:
    A new instance of a Node class.
    """
    def __init__(self, value):
        self._value = value
        self._left_node = None
        self._right_node = None

class BinaryTree():
        def __init__(self, new_value):
        """
        Summary of constructor:  initializes binary tree with a root node

        Attributes:
        self.head

        Returns:
        An empty binary tree
        """
        root_node = Node(new_value)

    def pre_order(self):
        """
        Summary of pre_order method: returns an array of the value following the pre order which is node, left, right.

        Parameters:
        self (): which is the current linked list object

        Returns:
        An array that is ordered via pre order.
        """
        pass

    def in_order(self):
        """
        Summary of in_order method: returns an array of the value following the in order which is left, node, right

        Parameters:
        self (): which is the current binary tree

        Returns:
        An array that is ordered via in order.
        """
        pass

    def post_order(self):   
        """
        Summary of post_order method: returns an array of the value following the in order which is left, right, node

        Parameters:
        self (): which is the current binary

        Returns:
        An array that is ordered via post order.
        """
        pass



class BinarySearchTree(BinaryTree):

    def add(self, new_value):
        node = Node(new_value)

        if node._value < root_node._value:
            root_node._left_node = node
        else:
            root_node._right_node = node


    def contains(self, value):
        pass
