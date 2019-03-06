from stacks_and_queues import Stack
from linked_list import LinkedList

class AnimalShelter():
    def __init__(self):
        self._in_stack = Stack()
        self.front = self._in_stack.top

    def enqueue(self, animal):
        """
        add to top
        """
        # for item in range(len(input_list)):
        #     self._in_stack.push(item)
        self._in_stack.push(animal)
        self.front = self._in_stack.top
        print(str(self.front.value))

    def dequeue(self, pref):
        """
        remove from top
        """
        temp = ''
        if pref != 'dog' and pref != 'cat':
            return Null
        
        if self._out_stack.peek():
            return self._out_stack.pop()

        # if self._in_stack.peek():
        #     while self._in_stack.peek():
        #         # temp = self._in_stack.pop()
        #         # self._out_stack.push(temp)
        #         self._out_stack.push(self._in_stack.pop())

        #     # temp._next = None
        #     self.front = self._in_stack.top
        #     print(str(self.front.value))
        #     print(str(temp.value))

        #     return self._out_stack.pop()
        # else:
        #     return None


if __name__ == "__main__":
    animal_queue = AnimalShelter()
    animals = ['dog1', 'dog2', 'cat1']
    print(str(animals))
    for animal in range(len(animals)):
        animal_queue.enqueue(animal)
    
    animal_queue = AnimalShelter()
    print('Front: ' + str(card_queue.front))