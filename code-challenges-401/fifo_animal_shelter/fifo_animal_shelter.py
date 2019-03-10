from stacks_and_queues import Stack

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
        self._in_stack.push(animal)
        self.front_in_stack = self._in_stack.top
        print('Front of in stack: ' + str(self.front_in_stack.value))

    def dequeue(self, pref):
        """
        remove from top
        """
        if pref != 'dog' and pref != 'cat':
            return Null
        
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


if __name__ == "__main__":
    animal_queue = AnimalShelter()
    # animal_queue.enqueue('dog')
    # animal_queue.enqueue('dog')
    # animal_queue.enqueue('cat')

    # print(str(animals))
    animals = ['dog', 'dog', 'cat']
    for animal in range(len(animals)):
        animal_queue.enqueue(animals[animal])

    result = animal_queue.dequeue('cat')
    print(str(result))

    result = animal_queue.dequeue('dog')
    print(str(result))

