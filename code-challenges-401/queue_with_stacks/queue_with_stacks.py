from stacks_and_queues import Stack
from linked_lists import LinkedList

class PseudoQueue():
    def __init__(self):
        self._in_stack = Stack()
        self._out_stack = Stack()
        self.front = self._in_stack.top
        self.rear = self._in_stack.top

        """
        only 2 Stacks available for storage
        """
        def enqueue(self, val):
            """
            add to rear
            """
            # for item in range(len(input_list)):
            #     self._in_stack.push(item)
            self._in_stack.push(val)
            self.front = self._in_stack.top

        def dequeue(self):
            """
            remove from front
            """
            pass

def __init__ = "__main__":
    card_queue = PseudoQueue()
    card_list = ['1', '2', '3']
    for item in range(len(card_list)):
        card_queue.enqueue(item)
    
    print(str(card_queue))