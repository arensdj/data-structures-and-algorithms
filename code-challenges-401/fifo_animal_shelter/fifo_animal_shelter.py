from stacks_and_queues import Stack

class AnimalShelter():
    """
    Summary of AnimalShelter class:  The purpose of this class is to implement a queue using two Stacks. This utilizes a composition of the Stack class.  The class will manage information on dogs and cats using a first-in, first-out approach.

    Attributes:
    self._in_stack : a stack that contains input string values of an animal
    self._out_stack : a stack that contains string values of an animal that are popped off the in stack
    self.top_in_stack : a string value of the top node of the stack containing input values
    self.top_out_stack : a string value of the top node of the stack containing values popped off the in stack
    """
    def __init__(self):
        self._in_stack = Stack()
        self._out_stack = Stack()
        self.front_in_stack = self._in_stack.top
        self.front_out_stack = self._out_stack.top

    def enqueue(self, animal):
        """
        Summary of enqueue method:  Adds input value of an animal (dog or cat) to rear of queue

        Parameters:
        self (AnimalShelter instance): which is the current AnimalShelter object
        animal (string): a string value

        Returns:
        Nothing
        """
        self._in_stack.push(animal)
        self.front_in_stack = self._in_stack.top
        # print('Front of in stack: ' + str(self.front_in_stack.value))

    def dequeue(self, pref):
        """
        Summary of dequeue method:  Removes a value from front of queue

        Parameters:
        self (AnimalShelter): which is the current AnimalShelter object
        pref (string) : a string value of an animal either a dog or cat

        Returns:
        Value removed from front of queue
        """
        if pref != 'dog' and pref != 'cat':
            return None

        if self._in_stack.peek():
            # pop everything on in_stack and push on out_stack
            while self._in_stack.peek():
                self._out_stack.push(self._in_stack.pop())

        # search for node that contains the pref value
        while True:
            if self._out_stack.top.value == pref:
                return self._out_stack.pop()
            else:
                self._in_stack.push(self._out_stack.pop())


# if __name__ == "__main__":
#     animal_queue = AnimalShelter()
#
#     # print(str(animals))
#     animals = ['dog', 'dog', 'cat']
#     for animal in range(len(animals)):
#         animal_queue.enqueue(animals[animal])
#
#     result = animal_queue.dequeue('cat')
#     print(str(result))
#
#     result = animal_queue.dequeue('dog')
#     print(str(result))

