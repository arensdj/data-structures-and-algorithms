from queue_with_stacks import PseudoQueue

def test_pseudo_queue_exists():
    """
    Test that class exists
    """
    assert PseudoQueue

def test_instantiation():
    """
    Test that class can be instatiated
    """
    assert PseudoQueue()

def test_enqueue_one_value():
    """
    Test that a value can be enqueued (pushed on stack)
    """
    card_queue = PseudoQueue()
    card_queue.enqueue('1')

    assert card_queue.top_in_stack.value == '1'

def test_enqueue_two_values():
    """
    Test that two values can be enqueued (pushed on stack)
    """ 
    card_queue = PseudoQueue()
    card_queue.enqueue('1')
    card_queue.enqueue('2')

    assert card_queue.top_in_stack.value == '2'

def test_dequeue_one_value():
    """
    Test that one value can be dequeued (popped off stack)
    """ 
    card_queue = PseudoQueue()
    card_queue.enqueue('1')
    card_queue.enqueue('2')
    card_queue.enqueue('3')
    card_queue.enqueue('4')

    assert card_queue.top_in_stack.value == '4'

    result = card_queue.dequeue()
    assert result == '1'

def test_dequeue_two_values():
    """
    Test that two values can be dequeued (popped off stack)
    """ 
    card_queue = PseudoQueue()
    card_queue.enqueue('1')
    card_queue.enqueue('2')
    card_queue.enqueue('3')
    card_queue.enqueue('4')

    assert card_queue.top_in_stack.value == '4'

    result = card_queue.dequeue()
    assert result == '1'
    
    result = card_queue.dequeue()
    assert result == '2'