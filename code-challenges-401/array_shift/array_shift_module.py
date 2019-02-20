# This program takes an input array and an input value and inserts that value in the middle 
# of the array.  A new array is used to create this array.
def insertShiftArray(original_arr, val):
  """
    Summary of insertShiftArray function:  takes an input array and an input value.  The input
    value is inserted in the middle of the array.  A new array is used to create this array.

    Parameters:
    original_array (array): An array of values
    val (int): An integer value
    
    Returns:
    new_array (array): Returns a new array containing the the original array with the input value
    inserted in the middle.
  """

  # Find the middle of the input array for odd and even elements       
  middle_position = (len(original_arr) // 2)
  new_arr = []

  # Create a new array containing first half of input array, the input value, and the last half 
  # of input array.
  if (len(original_arr) % 2 == 0):
    for i in range(middle_position):
      new_arr.append(original_arr[i])
  else:
    for i in range(0, middle_position + 1):
      new_arr.append(original_arr[i])

  # insert input value
  new_arr.append(val)

  # append remaining input array elements
  for i in range( len(new_arr), len(original_arr) + 1):
    new_arr.append(original_arr[i - 1])

  # return new array
  return new_arr