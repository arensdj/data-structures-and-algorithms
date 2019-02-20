from array_shift_module import insertShiftArray

def test_valid_array_valid_value_even():
  arr = [1, 2, 4, 5]
  val = 3
  
  actual = insertShiftArray(arr, val)
  expected = [1, 2, 3, 4, 5]
  assert expected == actual

def test_valid_array_valid_value_odd():
  arr = [1, 2, 3, 5, 6]
  val = 4
  
  actual = insertShiftArray(arr, val)
  expected = [1, 2, 3, 4, 5, 6]
  assert expected == actual

def test_invalid_array_valid_value():
  arr = []
  val = 4

  actual = insertShiftArray(arr, val)
  expected = [4]
  assert expected == actual


