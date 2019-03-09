from linked_list import LinkedList

class Node():
    """
    Summary of Node class:  Class definition of a node which is an individual item contained in a linked list. Each node contains the data for each item.

    Attributes:
    value (string): a string value
    _next: a property of Node class that will reference the next Node object in a linked list

    Returns:
    A new instance of a Node class.
    """
    def __init__(self, value):
        self.value = value
        self._next = None

class Queue():    # this is composition.  Not extending LinkedList but using its behavior
    """
    Summary of Queue class:  A queue is a data structure that consists of Nodes. Each Node references the next node in 
    the queue, but does not reference it’s previous.  This Queue class is a composition of the LinkedList class.  It 
    uses some of the LinkedList class methods.

    Attributes:
    self._list: a linked list
    self.front: a reference to the front of the queue
    self.rear: a reference to the rear of the queue

    Returns:
    An empty queue
    """
    # constructor
    def __init__(self):
        self._list = LinkedList()    # the '_' is a protected property
        self.front = None
        self.rear = None

    def dequeue(self):  
        """
        Summary of dequeue method:  removes a node from the front of the queue

        Attributes:
        self

        Returns:
        Nothing
        """
        try:
            self._list.remove_from_list_end()
            self.front = self._list.tail
            self.rear = self._list.head
        except:   # NullReferenceException:
            print('Queue is empty')

    def enqueue(self, value):
        """
        Summary of enqueue method: given an input string value adds a new node with that value to the rear of the queue.

        Attributes:
        self
        value (string): a string value

        Returns:
        Nothing
        """
        self._list.insert(value)    # insert a value at the rear of the queue
        self.front = self._list.tail
        self.rear = self._list.head

    def peek(self):
        """
        Summary of peek method:  returns the value of the node at the front of the queue

        Attributes:
        self

        Returns:
        The value of the node at the front of the queue.
        """
        try:
            return self._list.tail.value
        except: # NullReferenceException:
            print('Queue is empty')

class Stack():
    """
    Summary of Stack class:  A stack is a data structure that consists of Nodes. Each Node references the next node 
    in the stack, but does not reference it’s previous.  This Stack class is a composition of the LinkedList class.  
    It uses some of the LinkedList class methods.

    Attributes:
    self._list: an instance of a linked list
    self.top: initially assigned value of None.

    Returns:
    An empty stack
    """

    # constructor
    def __init__(self):
        self._list = LinkedList()
        self.top = None

    def peek(self):
        """
        Summary of peek method:  returns the value of the node on the top of the stack

        Attributes:
        self.head

        Returns:
        The value of the node on top of stack
        """
        try:
            self.top = self._list.head.value   
            return self.top 
        except: # NullReferenceException:
            print('Stack is empty')
        
    def pop(self):
        """
        Summary of pop method:  removes the node on top of the stack and returns that node's value

        Attributes:
        self

        Returns:
        The value of the node on stop of stack
        """
        try:
            value = self._list.remove_from_top()
            self.top = self._list.head
            return value
        except: # NullReferenceException:
            print('Stack is empty.')

    def push(self, value):
        """
        Summary of push method: given an input string value adds a new node with that value to the top of stack.

        Attributes:
        self
        value (string): a string value

        Returns:
        Nothing
        """
        self._list.insert(value)
        self.top = self._list.head

# if __name__ == "__main__":