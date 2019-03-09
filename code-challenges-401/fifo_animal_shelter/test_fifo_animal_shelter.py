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
    animal_queue.enqueue('dog1')

    assert animal_queue.front.value == 'dog1'

def test_enqueue_multiple_animal_strings():
    """
    Test that multiple values can be enqueued (pushed on stack)
    """
    animal_queue = AnimalShelter()
    animal_queue.enqueue('dog1')
    animal_queue.enqueue('dog2')
    animal_queue.enqueue('cat1')

    assert animal_queue.front.value == 'cat1'

def test_dequeue_one_value():
    """
    Test that one values can be dequeued (popped off stack)
    """    
    animal_queue = AnimalShelter()
    animal_queue.enqueue('dog1')
    animal_queue.enqueue('dog2')
    animal_queue.enqueue('cat1')

    assert animal_queue.front.value == 