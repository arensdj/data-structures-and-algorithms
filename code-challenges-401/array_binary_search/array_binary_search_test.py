""" 
  This is a test program for the array_binary_search_module program 
"""
from  array_binary_search_module import binary_search

def test_array_binary_search_even_array():
    arr = [4, 8, 15, 16, 23, 42]
    val = 15
    # arr = [1, 2, 3, 4, 5, 6]
    # val = 5
    
    actual = binary_search(arr, val)
    # expected = 4
    expected = 2
    assert expected == actual

def test_array_binary_search_odd_array():
    # arr = [1, 2, 3, 5, 6]
    # val = 2
    arr = [11, 22, 33, 44, 55, 66, 77]
    val = 90
    
    actual = binary_search(arr, val)
    # expected = 1
    expected = -1
    assert expected == actual

def test_array_binary_search_empty_array():
    arr = []
    val = 2
    
    actual = binary_search(arr, val)
    expected = -1
    assert expected == actual