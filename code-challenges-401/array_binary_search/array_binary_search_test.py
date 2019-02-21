""" 
  This is a test program for the array_binary_search_module program 
"""
from array_binary_search_module import binary_search

def test_array_binary_search_even_array():
    """
    This is a test function for the test_array_binary_search_even_array function 
    Attributes: 
      arr: An array containing an even number of integers
      val: An integer 
    Test passes if assert evaluates to true
    """
    arr = [1, 2, 3, 4, 5, 6]
    val = 5
    
    actual = binary_search(arr, val)
    expected = 4
    assert expected == actual

def test_array_binary_search_odd_array():
    """
    This is a test function for the test_array_binary_search_odd_array function 
    Attributes: 
      arr: An array containing an odd number of integers
      val: An integer 
    Test passes if assert evaluates to true
    """
    arr = [1, 2, 3, 5, 6]
    val = 2
    
    actual = binary_search(arr, val)
    expected = 1
    assert expected == actual

def test_array_binary_search_value_not_found():
    """
    This is a test function for the test_array_binary_search_value_not_found function 
    Attributes: 
      arr: An array containing an odd number of integers
      val: An integer
    Test passes if assert evaluates to true
    """
    arr = [11, 22, 33, 44, 55, 66, 77]
    val = 90
    
    actual = binary_search(arr, val)
    expected = -1
    assert expected == actual

def test_array_binary_search_empty_array():
    """
    This is a test function for the test_array_binary_search_empty_array function 
    Attributes: 
      arr: An empty array 
      val: An integer 
    Test passes if assert evaluates to true
    """
    arr = []
    val = 2
    
    actual = binary_search(arr, val)
    expected = -1
    assert expected == actual