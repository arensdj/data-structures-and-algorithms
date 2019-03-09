from queue_with_stacks import PseudoQueue

def test_pseudo_queue_exists():
    assert PseudoQueue

def test_instantiation():
    assert PseudoQueue()

def test_enqueue_one_value():
    card_queue = PseudoQueue()
    card_queue.enqueue('1')

    assert card_queue.top_in_stack.value == '1'


def test_enqueue_two_values():
    card_queue = PseudoQueue()
    card_queue.enqueue('1')
    card_queue.enqueue('2')

    assert card_queue.top_in_stack.value == '2'

def test_dequeue_one_value():
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

def test_dequeue_two_values():
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