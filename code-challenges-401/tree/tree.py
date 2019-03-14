from stacks_and_queues import Queue

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
    """
    Summary of BinaryTree class:  Class definition of a binary tree data structure in which each node has at most two child nodes which are referred to as the left child and the right child.

    Attributes:
    self.root_node : the top node in a binary tree
    self.sort_list : an array that will contain the traversal order of binary tree

    Returns:
    An instance of a binary tree
    """
    def __init__(self):
        self.root_node = None
        self.sort_list = []

    def breadth_first_traversal(self, current_node):
        """
        Summary of breadth_first_traversal method: returns an array of the value following the pre order which is node, left, right.

        Parameters:
        self (): which is the current binary tree object
        current_node : an input that has value of None
         
        Returns:
        An string that contains values of binary tree in breadth first order.
        """
        queue = Queue()

        if self.root_node is None:
            return output

        queue.enqueue(self.root_node)
        
        while queue.peek():
            current_node = queue.dequeue()

            if current_node._left_child:
                queue.enqueue(current_node._left_child)

            if current_node._right_child:
                queue.enqueue(current_node._right_child)

            self.sort_list.append(current_node.value)
        
        # print(str(self.sort_list))
        return self.sort_list

    def pre_order(self, node):
        """
        Summary of pre_order method: returns an array of node values following the pre order which is node, left, right.  This is done recursively.

        Parameters:
        self (): which is the current binary tree object
        node : the root node

        Returns:
        An array containing node values ordered via pre order.
        """
        self.sort_list.append(node.value)

        if node._left_child is not None:
            self.pre_order(node._left_child)

        if node._right_child is not None:
            self.pre_order(node._right_child)

        return self.sort_list

    def in_order(self, node):
        """
        Summary of in_order method: returns an array of node values following the in order which is left, node, right.  This is done recursively.

        Parameters:
        self (): which is the current binary tree
        node : the root node

        Returns:
        An array containing node values ordered via in order.
        """

        if node._left_child is not None:
            self.in_order(node._left_child)

        self.sort_list.append(node.value)

        if node._right_child is not None:
            self.in_order(node._right_child)

        return self.sort_list

    def post_order(self, node):
        """
        Summary of post_order method: returns an array of node value following the in order which is left, right, node.  This is done recursively.

        Parameters:
        self (): which is the current binary
        node : the root node

        Returns:
        An array containing node values ordered via post order.
        """
        if node._left_child is not None:
            self.post_order(node._left_child)

        if node._right_child is not None:
            self.post_order(node._right_child)

        self.sort_list.append(node.value)

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

    def add(self, new_value):
        """
        Summary of add method: adds a new node value in the correct location in the binary search tree.

        Parameters:
        self () : which is the current binary tree
        new_value : string value to add

        Returns:
        """
        new_node = Node(new_value)

        if self.binary_tree.root_node is None:
            self.binary_tree.root_node = new_node
        else:
            self._addNode(self.binary_tree.root_node, new_node)

    def _addNode(self, parent_node, new_node):
        """
        Summary of _addNode method: adds a new node value in the correct location in the binary search tree.

        Parameters:
        self () : which is the current binary tree
        parent_node : the root node
        new_value : string value to add

        Returns:
        An array that is ordered via post order.
        """
        if not parent_node:
            return

        if new_node.value < parent_node.value:
            if parent_node._left_child is None:
                parent_node._left_child = new_node
            else:
                self._addNode(parent_node._left_child, new_node)
        else:
            if parent_node._right_child is None:
                parent_node._right_child = new_node
            else:
                self._addNode(parent_node._right_child, new_node)

    def contains(self, value, parent_node=None):
        """
        Summary of contains method:  accepts a value and returns a boolean indicating whether or not the value is in the tree at least once.

        Parameters:
        self (): which is the current binary

        Returns:
        A boolean value
        """
        if parent_node is None:
            parent_node = self.binary_tree.root_node
        
        if parent_node.value == value:
            return True

        if value > parent_node.value and parent_node._right_child.value:
            return self.contains(value, parent_node._right_child)

        if parent_node._left_child:
            return self.contains(value, parent_node._left_child)

        return False

    def get_breadth_order_data(self):
        """
        Summary of get_in_order_data method: returns an array of the value following the in order which is left, right, node

        Parameters:
        self (): which is the current binary

        Returns:
        An array that is ordered via post order.
        """
        self.binary_tree.sort_list = []
        return self.binary_tree.breadth_first_traversal(None)
        # return self.binary_tree.breadth_first_traversal(self.binary_tree.root_node, None)


    def get_pre_order_data(self):
        """
        Summary of get_pre_order_data method: returns an array of the value following the in order which is left, right, node

        Parameters:
        self (): which is the current binary

        Returns:
        An array that is ordered via post order.
        """
        self.binary_tree.sort_list = []
        return self.binary_tree.pre_order(self.binary_tree.root_node)

    def get_post_order_data(self):
        """
        Summary of get_post_order_data method: returns an array of the value following the in order which is left, right, node

        Parameters:
        self (): which is the current binary

        Returns:
        An array that is ordered via post order.
        """
        self.binary_tree.sort_list = []
        return self.binary_tree.post_order(self.binary_tree.root_node)

    def get_in_order_data(self):
        """
        Summary of get_in_order_data method: returns an array of the value following the in order which is left, right, node

        Parameters:
        self (): which is the current binary

        Returns:
        An array that is ordered via post order.
        """
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
