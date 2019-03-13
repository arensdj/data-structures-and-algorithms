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
    Summary of BinaryTree class:  Class definition of a node which is an individual item. Each node contains the data for each item.

    Attributes:
    value (string) : a string value
    _left_node : a property of Node class that will reference the next Node object to the left of the root node.
    _right_node : a property of Node class that will reference the next Node object to the right of the root node.

    Returns:
    A new instance of a Node class.
    """
    def __init__(self):
        self.root_node = None
        self.sort_list = []

    def breadth_first_traversal(self, binary_tree):
        """
        Summary of breadth_first_traversal method: returns an array of the value following the pre order which is node, left, right.

        Parameters:
        self (): which is the current binary tree object
         

        Returns:
        An string that contains values of binary tree in breadth first order.
        """
        queue = Queue()
        output = ''

        if binary_tree.root_node is None:
            return output

        queue.enqueue(binary_tree.root_node)
        temp = Node()
        current = Node()

        while queue.peek():
            current = queue.dequeue()

            if current._left_child:
                queue.enqueue(current._left_child)

            if current._right_child:
                queue.enqueue(current._right_child)

            temp = queue.dequeue()

            output += temp.value

        return output



    def pre_order(self, node):
        """
        Summary of pre_order method: returns an array of the value following the pre order which is node, left, right.

        Parameters:
        self (): which is the current binary tree object
        node 

        Returns:
        An array that is ordered via pre order.
        """
        self.sort_list.append(node.value)

        if node._left_child is not None:
            self.pre_order(node._left_child)

        if node._right_child is not None:
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

        if node._left_child is not None:
            self.in_order(node._left_child)

        self.sort_list.append(node.value)

        if node._right_child is not None:
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
        Summary of add method: returns an array of the value following the in order which is left, right, node

        Parameters:
        self (): which is the current binary

        Returns:
        An array that is ordered via post order.
        """
        new_node = Node(new_value)

        if self.binary_tree.root_node is None:
            self.binary_tree.root_node = new_node
        else:
            self._addNode(self.binary_tree.root_node, new_node)

    def _addNode(self, parent_node, new_node):
        """
        Summary of _addNode method: returns an array of the value following the pre order which is left, right, node

        Parameters:
        self (): which is the current binary

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
        Summary of contains method: 

        Parameters:
        self (): which is the current binary

        Returns:
        An array that is ordered via post order.
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
