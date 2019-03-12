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

    def pre_order(self, node):
        """
        Summary of pre_order method: returns an array of the value following the pre order which is node, left, right.

        Parameters:
        self (): which is the current linked list object

        Returns:
        An array that is ordered via pre order.
        """
        self.sort_list.append(node)

        if node._left_child != None:
            self.pre_order(node._left_child)

        if node._right_child != None:
            self.pre_order(node._right_child)

        return self.sort_list


    def in_order(self, node):
        """
        Summary of in_order method: returns an array of the value following the in order which is left, node, right

        Parameters:
        self (): which is the current binary tree

        Returns:
        An array that is ordered via in order.
        """

        if node._left_child != None:
            self.in_order(node._left_child)

        self.sort_list.append(node)

        if node._right_child != None:
            self.in_order(node._right_child)

        return self.sort_list


    def post_order(self, node):
        """
        Summary of post_order method: returns an array of the value following the in order which is left, right, node

        Parameters:
        self (): which is the current binary

        Returns:
        An array that is ordered via post order.
        """
        if node._left_child != None:
            self.post_order(node._left_child)

        if node._right_child != None:
            self.post_order(node._right_child)

        self.sort_list.append(node)

        return self.sort_list

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

    # def add(self, current_node, new_value):
    def add(self, new_value):
        new_node = Node(new_value)

        if self.binary_tree.root_node == None:
            self.binary_tree.root_node = new_node
        else:
            self._addNode(self.binary_tree.root_node, new_node)

        # return

        # if current_node == None:
            # if self.binary_tree.root_node == None:
            #     self.binary_tree.root_node = new_node
            # else:
            #     self.add(self.binary_tree.root_node, new_node)

            # return
        # else:
            # while not added_node:
        
    def _addNode(self, parent_node, new_node):

        if not parent_node:
            return

        if new_node.value < parent_node.value:
        # if new_node.value < current_node.value:
            # if current_node._left_child == None:
            if parent_node._left_child == None:
                # current_node._left_child = new_node
                parent_node._left_child = new_node
                # return
            else:
                self._addNode(parent_node._left_child, new_node)
                # self.add(current_node, new_node)
        else:
            if parent_node._right_child == None:
                parent_node._right_child = new_node
                # return
            else:
                self.add(parent_node._right_child, new_node)

    def contains(self, value):
        pass

    def get_pre_order_data(self):
        self.binary_tree.sort_list = []
        return self.binary_tree.pre_order(self.binary_tree.root_node)

    def get_post_order_data(self):
        self.binary_tree.sort_list = []
        return self.binary_tree.post_order(self.binary_tree.root_node)

    def get_in_order_data(self):
        self.binary_tree.sort_list = []
        return self.binary_tree.in_order(self.binary_tree.root_node)

if __name__ == "__main__":
    binary_search_tree = BinarySearchTree()

    binary_search_tree.add(5)

    binary_search_tree.add(3)

    binary_search_tree.add(10)

    array_pre_order = []
    array_pre_order = binary_search_tree.get_pre_order_data()

    array_post_order = []
    array_post_order = binary_search_tree.get_post_order_data()

    array_in_order = []
    array_in_order = binary_search_tree.get_in_order_data()


    print((array_pre_order))
