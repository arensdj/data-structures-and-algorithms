""" 
    This is a test program for the linked_list program.  It will test the following:
    Tests that linked list class existss
    Can successfully instantiate an empty linked list
    Can properly insert into the linked list
    The head property will properly point to the first node in the linked list
    Can properly insert multiple nodes into the linked list
    Will return true when finding a value within the linked list that exists
    Will return false when searching for a value in the linked list that does not exist
    Can properly return a collection of all the values that exist in the linked list
    Will return an empty string when printing an empty linked list
    Will return an empty string when linked list is empty
"""

from linked_list import LinkedList

def test_exists():
    """
    Tests that a LinkedList class exists
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

    assert flowers.head.value == 'rose'
    assert flowers.head._next.value == 'lavender'
    assert flowers.head._next._next.value == 'zinnia'

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

    assert flowers.print() == 'crocus,daffodile,tulip,'

def test_print_empty_list():
    """
    Can properly return an empty collection when linked list is empty
    """
    flowers = LinkedList()

    expected = ''
    actual = ''
    assert expected == actual

def test_includes_empty_list():
    """
    Can properly return an empty array when linked list is empty
    """
    flowers = LinkedList()

    expected = ''
    actual = ''
    assert expected == actual

def test_append_item():
    flowers = LinkedList()
    flowers.insert('tulip')
    flowers.insert('daffodile')
    flowers.append_item('geranium')

    assert flowers.head._next._next.value == 'geranium'

def test_insert_before():
    flowers = LinkedList()
    flowers.insert('tulip')
    flowers.insert('daffodile')
    flowers.insert_before('tulip', 'geranium')

    assert flowers.head._next.value == 'geranium'

def test_insert_after():
    flowers = LinkedList()
    flowers.insert('tulip')
    flowers.insert('geranium')
    flowers.insert('daffodile')
    flowers.insert_after('geranium', 'pansie')

    assert flowers.head._next._next.value == 'pansie'

def test_insert_after_head():
    flowers = LinkedList()
    flowers.insert('tulip')
    flowers.insert_after('tulip', 'petunia')

    assert flowers.head._next.value == 'petunia'

def test_find_from_end():
    flowers = LinkedList()
    flowers.insert('tulip')
    flowers.insert('rose')
    flowers.insert('pansie')
    flowers.insert('geranium')
    flowers.insert('daffodile')

    expected = 'geranium'
    actual = flowers.find_from_end(3)

    assert expected == actual

def test_find_from_end_empty_ll():
    flowers = LinkedList()

    expected = ''
    actual = flowers.find_from_end(2)

    assert expected == actual

def test_find_from_end_value_too_large():
    flowers = LinkedList()
    flowers.insert('tulip')
    flowers.insert('rose')
    flowers.insert('pansie')
    flowers.insert('geranium')
    flowers.insert('daffodile')

    expected = ''
    actual = flowers.find_from_end(6)

    assert expected == actual

def test_ll_merge():
    list1 = LinkedList()
    list1.append_item('1')
    list1.append_item('3')
    list1.append_item('5')
    
    list2 = LinkedList()
    list2.append_item('2')
    list2.append_item('4')
    list2.append_item('6')

    actual = list1.ll_merge(list2)

    assert list1.print() == '1,2,3,4,5,6,'

def test_ll_merge_empty_ll():
    list1 = LinkedList()
    list1.append_item('1')
    list1.append_item('3')
    list1.append_item('5')

    list2 = LinkedList()

    actual = list1.ll_merge(list2)
    assert list1.print() == '1,3,5,'

def test_ll_merge_empty_2():
    list1 = LinkedList()
    list1.append_item('1')
    list1.append_item('3')
    list1.append_item('5')
    list1.append_item('7')

    list2 = LinkedList()
    list2.append_item('2')
    list2.append_item('4')

    actual = list1.ll_merge(list2)

    assert list1.print() == '1,2,3,4,5,7,'

def test_ll_merge_empty_2():
    list1 = LinkedList()
    list1.append_item('1')
    list1.append_item('3')

    list2 = LinkedList()
    list2.append_item('2')
    list2.append_item('4')
    list2.append_item('6')
    list2.append_item('8')

    actual = list1.ll_merge(list2)

    assert list1.print() == '1,2,3,4,6,8,'