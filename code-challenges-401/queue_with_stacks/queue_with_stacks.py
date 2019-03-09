from stacks_and_queues import Stack
from linked_list import LinkedList

class PseudoQueue():
    """
    Summary of PseudoQueue class:  The purpose of this class is to implement a queue using two Stacks.  This utilizes a composition of the Stack class.

    Attributes:
    self._in_stack 
    self._out_stack
    self.top_in_stack
    self.top_out_stack

    Returns:
    An empty queue
    """   

    # Constructor
    def __init__(self):
        """
        Summary of constructor:  initializes two stacks

        Attributes:
        elf._in_stack : used to push values
        self._out_stack : used to push values popped from self._in_stack

        Returns:
        An empty queue      
        """
        self._in_stack = Stack()
        self._out_stack = Stack()
        self.top_in_stack = self._in_stack.top
        self.top_out_stack = self._out_stack.top

    def enqueue(self, val):
        """
        Summary of enqueue method:  Adds input val to rear of queue
        
        Parameters:
        self (PsuedoQueue): which is the current PseudoQueue object
        val (string): a string value 

        Returns:
        Nothing
        """
        self._in_stack.push(val)
        self.top_in_stack = self._in_stack.top
        # print('Enqueue: ' + str(self.top_in_stack.value))
        # print(str(self._in_stack._list.print()))

    def dequeue(self):
        """
        remove from front
        """
        """
        Summary of dequeue method:  Removes a value from front of queue
        
        Parameters:
        self (PsuedoQueue): which is the current PseudoQueue object

        Returns:
        Value removed from front of queue
        """
        if self._out_stack.peek():
            self.top_out_stack = self._out_stack.top
            return self._out_stack.pop()

        # print('Before dequeue: ')
        # print(str(self._in_stack._list.print()))

        if self._in_stack.peek():
            while self._in_stack.peek():
                self._out_stack.push(self._in_stack.pop())


            self.top_out_stack = self._out_stack.top.value
            # print('Top of out stack: ')
            # print(str(self._out_stack.top))

            return self._out_stack.pop()
        else:
            return None


# if __name__ == "__main__":
#     card_queue = PseudoQueue()
#     card_list = ['1', '2', '3']
#     print(str(card_list))
#     for item in range(len(card_list)):
#         card_queue.enqueue(card_list[item])
    
#     print('Top: ' + str(card_queue.top_in_stack.value))
#     result = card_queue.dequeue()
#     print('Result: ' + str(result))
#     print('Top: ' + str(card_queue.top_in_stack.value))
#     print('Top: ' + str(card_queue.top_out_stack.value))