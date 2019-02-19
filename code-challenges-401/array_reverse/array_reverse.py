# takes an array argument and returns an array with the elements in reversed order
def reverseArray(input_array):
  # array that will contain input array in reverse order
  temp_array = []

  # reverse the array
  length = len(input_array) - 1
  while (length >= 0):
    # reference the end of the input array when assigning an element in reversed array.
    temp_array.append(input_array[length])
    # subtract one from length so that input array will be accessed starting from the end 
    length = length - 1
  return temp_array

# prompt user for array of numbers
print('Enter an array of numbers: ')
input_array = input().split()

# invoke function to reverse array elements and display the reversed array
print(str(reverseArray(input_array)))
