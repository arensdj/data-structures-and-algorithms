from stacks_and_queues import Stack
from linked_list import LinkedList

class AnimalShelter():
    def __init__(self):
        self._in_stack = Stack()
        self.front = self._in_stack.top
        # self.rear = self._in_stack.top

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
        print(str(self.front.value))

    def dequeue(self):
        """
        remove from front
        """
        temp = ''
        if self._out_stack.peek():
            return self._out_stack.pop()

        if self._in_stack.peek():
            while self._in_stack.peek():
                # temp = self._in_stack.pop()
                # self._out_stack.push(temp)
                self._out_stack.push(self._in_stack.pop())

            # temp._next = None
            self.front = self._in_stack.top
            print(str(self.front.value))
            print(str(temp.value))

            return self._out_stack.pop()
        else:
            return None


if __name__ == "__main__":
    card_queue = PseudoQueue()
    card_list = ['1', '2', '3']
    print(str(card_list))
    for item in range(len(card_list)):
        card_queue.enqueue(item)
    
    print('Front: ' + str(card_queue.front))
    # print('Rear: ' + str(card_queue.rear))