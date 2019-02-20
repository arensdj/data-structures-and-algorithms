""" 
  This is a test program for the array_shift_module program 
"""
from array_shift_module import insertShiftArray

def test_valid_array_valid_value_even():
  """
    This is a test function for the test_valid_array_valid_value_even function 
    Attributes: 
      arr: An array containing an even number of integers
      val: An integer 
    Test passes if assert evaluates to true
  """
  arr = [1, 2, 4, 5]
  val = 3
  
  actual = insertShiftArray(arr, val)
  expected = [1, 2, 3, 4, 5]
  assert expected == actual

def test_valid_array_valid_value_odd():
  """
    This is a test function for the test_valid_array_valid_value_odd function 
    Attributes: 
      arr: An array containing an odd number of integers
      val: An integer 
    Test passes if assert evaluates to true
  """
  arr = [1, 2, 3, 5, 6]
  val = 4
  
  actual = insertShiftArray(arr, val)
  expected = [1, 2, 3, 4, 5, 6]
  assert expected == actual

def test_invalid_array_valid_value():
  """
    This is a test function for the test_invalid_array_valid_value function 
    Attributes: 
      arr: An empty array 
      val: An integer 
    Test passes if assert evaluates to true
  """
  arr = []
  val = 4

  actual = insertShiftArray(arr, val)
  expected = [4]
  assert expected == actual


