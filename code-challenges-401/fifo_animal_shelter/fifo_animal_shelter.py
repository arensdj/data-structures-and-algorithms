from stacks_and_queues import Stack
from linked_list import LinkedList

class AnimalShelter():
    def __init__(self):
        self._in_stack = Stack()
        self._out_stack = Stack()
        self.front_in_stack = self._in_stack.top
        self.front_out_stack = self._out_stack.top

    def enqueue(self, animal):
        """
        add to top
        """
        # for item in range(len(input_list)):
        #     self._in_stack.push(item)
        self._in_stack.push(animal)
        self.front_in_stack = self._in_stack.top
        print('Front of in stack: ' + str(self.front.value))

    def dequeue(self, pref):
        """
        remove from top
        """
        if pref != 'dog' and pref != 'cat':
            return Null
        
        if self._out_stack.peek():
            return self._out_stack.pop()

        if self._in_stack.peek():
            while self._in_stack.peek():
                self._out_stack.push(self._in_stack.pop())

            self.front_out_stack = self._in_stack.top
            print('Front out stack: ' + str(self.front_out_stack))
            # print(str(temp.value))

            return self._out_stack.pop()
        else:
            return None


if __name__ == "__main__":
    animal_queue = AnimalShelter()
    animals = ['dog1', 'dog2', 'cat1']
    print(str(animals))
    for animal in range(len(animals)):
        animal_queue.enqueue(animal)
    
    animal_queue.dequeue()
    print('Front: ' + str(animal_queue.front))