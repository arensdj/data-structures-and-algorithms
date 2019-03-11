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
        self.value = value
        self._left_child = None
        self._right_child = None

class BinaryTree():

    def __init__(self):
        self.root_node = None
        self.sort_list = []

    def pre_order(self, current_node):
        """
        Summary of pre_order method: returns an array of the value following the pre order which is node, left, right.

        Parameters:
        self (): which is the current linked list object

        Returns:
        An array that is ordered via pre order.
        """
        # tmp_array = []

        if current_node is None:
            # return tmp_array
            current_node = self.root_node
            self.pre_order(current_node)
            return
        else:
            self.sort_list.append(current_node.value)

            self.pre_order(current_node._left_child)

            self.pre_order(current_node._right_child)

            return

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

class BinarySearchTree():

    def __init__(self):
        """
        Summary of constructor:  initializes binary tree with a root node

        Attributes:
        self.head

        Returns:
        An empty binary tree
        """
        self.binary_tree = BinaryTree()

    def add(self, current_node, new_node):
        if current_node == None:
            if self.binary_tree.root_node == None:
                self.binary_tree.root_node = new_node
            else:
                self.add(self.binary_tree.root_node, new_node)

            return
        else:
            # while not added_node:
            if new_node.value < current_node.value:
                if current_node._left_child == None:
                    current_node._left_child = new_node
                    return
                else:
                    self.add(current_node, new_node)
            else:
                if current_node._right_child == None:
                    current_node._right_child = new_node
                    return
                else:
                    self.add(current_node, new_node)


    def contains(self, value):
        pass

    def get_pre_order_data(self):
        return self.binary_tree.pre_order(None)



if __name__ == "__main__":
    # binary_tree = BinaryTree()
    binary_search_tree = BinarySearchTree()

    new_node = Node(5)
    binary_search_tree.add(None, new_node)

    new_node = Node(3)
    binary_search_tree.add(None, new_node)

    new_node = Node(10)
    binary_search_tree.add(None, new_node)

    array_pre_order = []
    array_pre_order = binary_search_tree.get_pre_order_data()




