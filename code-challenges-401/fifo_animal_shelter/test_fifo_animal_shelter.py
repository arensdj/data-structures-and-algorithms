from fifo_animal_shelter import AnimalShelter

def test_animal_shelter_exists():
    """
    Test that class exists
    """
    assert AnimalShelter

def test_instantiation():
    """
    Test that class can be instatiated
    """
    assert AnimalShelter()

def test_enqueue_one_animal_string():
    """
    Test that a value can be enqueued (pushed on stack)
    """
    animal_queue = AnimalShelter()
    animal_queue.enqueue('dog')

    assert animal_queue.front_in_stack.value == 'dog'

def test_enqueue_multiple_animal_strings():
    """
    Test that multiple values can be enqueued (pushed on stack)
    """
    animal_queue = AnimalShelter()
    animal_queue.enqueue('dog')
    animal_queue.enqueue('dog')
    animal_queue.enqueue('cat')

    assert animal_queue.front_in_stack.value == 'cat'

def test_dequeue_one_value():
    """
    Test that one values can be dequeued (popped off stack)
    """    
    animal_queue = AnimalShelter()
    animal_queue.enqueue('dog')
    animal_queue.enqueue('dog')
    animal_queue.enqueue('cat')

    animal_queue.dequeue('cat')

    assert animal_queue.front_out_stack.value == 'dog'

    