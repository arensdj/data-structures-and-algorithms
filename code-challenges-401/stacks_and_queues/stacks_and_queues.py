from linked_list import LinkedList

class Node():
    def __init__(self, value):
        self.value = value
        self._next = None

class Queue():    # this is composition.  Not extending LinkedList ut using its behavior

    # constructor
    def __init__(self):
        self._list = LinkedList()    # the _ is protected
        self.front = None
        self.rear = None

    def enqueue(self, value):
        self._list.insert(value)    # at the beginning
        self.front = self._list.tail
        self.rear = self._list.head

    def peek(self):
        try:
            return self._list.tail.value
        except: # NullReferenceException:
            print('Queue is empty')

    def dequeue(self):  # in LinkedList you would need a remove_from_list_end() method
        try:
            self._list.remove_from_list_end()
            self.front = self._list.tail
            self.rear = self._list.head
        except:   # NullReferenceException:
            print('Queue is empty')

class Stack():
    """
    Summary of Stack class:  A stack is a data structure that consists of Nodes. Each Node references the next node in the stack, but does not reference it’s previous.  This Stack class is a composition of the LinkedList class.  It uses some of the LinkedList class methods.

    Attributes:
    _list: a linked list
    top: Initially assigned value of None.

    Returns:
    An empty stack
    """

    # constructor
    def __init__(self):
        self._list = LinkedList()
        self.top = None

    def peek(self):
        """
        Summary of peek method:  initializes an empty linked list

        Attributes:
        self.head

        Returns:
        An empty of a linked list
        """
        try:
            self.top = self._list.head.value   
            return self.top 
        except NullReferenceException:
            print('Stack is empty')
        
    def pop(self):
        try:
            self._list.remove_from_top()
            self.top = self._list.head
        except NullReferenceException:
            print('Stack is empty.')

    def push(self, value):
        self._list.insert(value)
        self.top = self._list.head

# if __name__ == "__main__":