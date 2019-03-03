

class Queue():    # this is composition.  Not extending LinkedList ut using its behavior
            # my code (LinkedList needs to know the head)
    _list = LinkedList()    # the _ is protected

    def enqueue(self, value):
        _list.insert(value)    # at the beginning


    def dequeue(self):  # in LinkedList you would need a remove_from_list() method
      _list.remove_from_end()



class Stack():

    _list = LinkedList()

    def push(self, value):
      _list.insert(value):

    def pop():
      _list.

