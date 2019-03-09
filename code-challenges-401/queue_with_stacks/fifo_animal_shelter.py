from stacks_and_queues import Stack
from linked_list import LinkedList

class AnimalShelter():
  """
    Summary of AnimalShelter class:  The purpose of this class is to implement a queue using two Stacks.  This utilizes a composition of the Stack class.

    Attributes:
    self._in_stack 
    self._out_stack
    self.top_in_stack
    self.top_out_stack

    Returns:
    An empty queue
    """   
    def __init__(self):
        self._in_stack = Stack()
        self._out_stack = Stack()
        self.top_in_stack = self._in_stack.top
        self.top_out_stack = self._out_stack.top

    def enqueue(self, animal):
        """
        Summary of enqueue method:  Adds input animal string to rear of queue, which is stop of stack
        
        Parameters:
        self (PsuedoQueue): which is the current PseudoQueue object
        animal (string): a string value 

        Returns:
        Nothing
        """
        self._in_stack.push(animal)
        self.top_in_stack = self._in_stack.top

        # print(str(self.front.value))

    def dequeue(self, pref):
        """
        Summary of dequeue method:  Removes a value from front of queue
        
        Parameters:
        self (PsuedoQueue): which is the current PseudoQueue object
        pref (string) : value to remove from queue

        Returns:
        Value removed from front of queue
        """
        if pref != 'dog' and pref != 'cat':
            return Null
        
        if self._out_stack.peek() == pref:
            return self._out_stack.pop()

        # if self._in_stack.peek():
        #     while self._in_stack.peek():
        #         self._out_stack.push(self._in_stack.peek())

        #     self.top_in_stack = self._out_stack.top.value
        #     return self._out_stack.pop()
        # else:
        #     return None

if __name__ == "__main__":
    animal_queue = AnimalShelter()
    animals = ['dog1', 'dog2', 'cat1']
    print(str(animals))
    for animal in range(len(animals)):
        animal_queue.enqueue(animal)
    
    animal_queue.dequeue()
    print('Front: ' + str(animal_queue.top_in_stack))