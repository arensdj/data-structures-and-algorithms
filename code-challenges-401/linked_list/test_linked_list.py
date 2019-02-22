from linked_list import LinkedList

"""
# Can successfully instantiate an empty linked list
# Can properly insert into the linked list
# The head property will properly point to the first node in the linked list
# Can properly  insert multiple nodes into the linked list
# Will return true when finding a value within the linked list that exists
# Will return false when searching for a value in the linked list that does not exist
# Can properly return a collection of all the values that exist in the linked list
"""

def test_exists():
    """
    """
    assert LinkedList

def test_instantiation():
    """
    Can successfully instantiate an empty linked list
    """
    assert LinkedList()


def test_insert():
    """
    Can properly insert into the linked list
    """
    flowers = LinkedList()
    flowers.insert('zinnia')

    expected = 'zinnia'
    actual = flowers.head.value

    assert expected == actual

def test_head_points_to_first_node():
    """
    The head property will properly point to the first node in the linked list
    """
    flowers = LinkedList()
    flowers.insert('lavender')

    expected = 'lavender'
    actual = flowers.head.value

    assert expected == actual


def test_multiple_insert():
    """
    Can properly insert multiple nodes into the linked list
    """
    flowers = LinkedList()
    flowers.insert('zinnia')
    flowers.insert('lavender')
    flowers.insert('rose')
    
    assert flowers.head.value == 'zinnia'
    assert flowers.head._next.value == 'lavender'
    assert flowers.head._next._next.value == 'rose'

def test_includes():
    """
    Will return true when finding a value within the linked list that exists
    """
    flowers = LinkedList()
    flowers.insert('zinnia')
    flowers.insert('lavender')
    flowers.insert('rose')

    assert flowers.includes('rose')

def test_not_includes():
    """
    Will return false when finding a value that doesn't exist in the linked list
    """
    flowers = LinkedList()
    flowers.insert('zinnia')
    flowers.insert('lavender')
    flowers.insert('rose')

    assert not flowers.includes('daisy')    

def test_print_list():
    """
    Can properly return a collection of all the values that exist in the linked list
    """
    flowers = LinkedList()
    flowers.insert('tulip')
    flowers.insert('daffodile')
    flowers.insert('crocus')

    assert flowers.print() == 'tulip,daffodile,crocus,'

