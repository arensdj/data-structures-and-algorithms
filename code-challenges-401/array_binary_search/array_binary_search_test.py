""" 
  This is a test program for the array_binary_search_module program 
"""
from  array_binary_search_module import binary_search

def test_array_binary_search():
"""
    This is a test function for the test_array_binary_search function 
    Attributes: 
      arr: 
      val: 
    
"""
    arr = [1, 2, 3, 4, 5, 6]
    val = 5
    
    actual = binary_search(arr, val)
    expected = 5
    assert expected == actual

