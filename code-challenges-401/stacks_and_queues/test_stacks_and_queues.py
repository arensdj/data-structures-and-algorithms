from stacks_and_queues import Stack, Queue
"""
Test module for stacks_and_queues class
"""
def test_stack_push_one_node():
    """
    Can successfully push onto a stack
    """
    plate_stack = Stack()
    plate_stack.push('plate_1')

    assert plate_stack.top.value == 'plate_1'

def test_stack_push_multiple_nodes():
    """
    Can successfully push multiple nodes onto a stack
    """
    plate_stack = Stack()

    plate_stack.push('plate_1')
    plate_stack.push('plate_2')
    plate_stack.push('plate_3')

    assert plate_stack.top.value == 'plate_3'

def test_stack_pop():
    """
    Can successfully pop off the stack
    """
    plate_stack = Stack()
    plate_stack.push('plate_1')
    plate_stack.push('plate_2')
    plate_stack.push('plate_3')
    plate_stack.pop()

    assert plate_stack.top.value == 'plate_2'

def test_stack_multiple_pops():
    """
    Can successfully empty a stack after multiple pops.
    """
    plate_stack = Stack()
    plate_stack.push('plate_1')
    plate_stack.push('plate_2')
    plate_stack.push('plate_3')
    plate_stack.pop()
    plate_stack.pop()
    plate_stack.pop()

    assert plate_stack.top == None

def test_stack_peek():
    """
    Can successfully peek the next item on the stack.
    """
    plate_stack = Stack()
    plate_stack.push('plate_1')
    plate_stack.push('plate_2')
    plate_stack.push('plate_3')  
    
    assert plate_stack.peek() == 'plate_3'

def test_stack_instatiation():
    """
    Can successfully instantiate an empty stack
    """
    assert Stack()

def test_queue_enqueue_one_node():
    """
    Can successfully enqueue onto a queue
    """
    grocery_checkout_queue = Queue()
    grocery_checkout_queue.enqueue('Adam')

    assert grocery_checkout_queue.front.value == 'Adam'
    assert grocery_checkout_queue.rear.value == 'Adam'

def test_queue_enqueue_multiple_nodes():
    """
    Can successfully enqueue multiple items into a queue
    """
    grocery_checkout_queue = Queue()
    grocery_checkout_queue.enqueue('Adam')
    grocery_checkout_queue.enqueue('Sue')
    grocery_checkout_queue.enqueue('Michael')

    assert grocery_checkout_queue.front.value == 'Adam'
    assert grocery_checkout_queue.rear.value == 'Michael'

def test_queue_peek():
    """
    Can successfully peek into a queue, seeing the expected value
    """
    grocery_checkout_queue = Queue()
    grocery_checkout_queue.enqueue('Adam')
    grocery_checkout_queue.enqueue('Sue')

    assert grocery_checkout_queue.peek() == 'Adam'

def test_dequeue_one_node():
    """
    Can successfully dequeue off of a queue the expected value
    """
    grocery_checkout_queue = Queue()
    grocery_checkout_queue.enqueue('Adam')
    grocery_checkout_queue.enqueue('Sue')
    grocery_checkout_queue.enqueue('Michael')

    grocery_checkout_queue.dequeue()
    assert grocery_checkout_queue.front.value == 'Sue'

def test_queue_multiple_dequeue():
    """
    Can successfully empty a queue after multiple dequeues
    """
    grocery_checkout_queue = Queue()
    grocery_checkout_queue.enqueue('Adam')
    grocery_checkout_queue.enqueue('Sue')
    grocery_checkout_queue.enqueue('Michael')

    grocery_checkout_queue.dequeue()
    grocery_checkout_queue.dequeue()
    grocery_checkout_queue.dequeue()
   
    assert grocery_checkout_queue.peek() == None

def test_queue_instatiation():
    """
    Can successfully instantiate an empty queue
    """
    assert Queue()