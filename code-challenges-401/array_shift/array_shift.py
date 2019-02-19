def insertShiftArray(original_arr, val):
  middle_position = len(arr) // 2
  new_arr = []

  if (len(arr) % 2 == 0):
    for i in range(middle_position):
      new_arr[i] = original_arr[i]
  else:
    for i in range(middle_position + 1):
      new_arr[i] = original_arr[i]
  
  new_arr.append(val)

  for i in range(len(new_arr), len(original_arr + 1)):
    new_arr[i] = original_arr[i - 1]

  return new_arr

arr = input().split()
val = input()

new_array = insertShiftArray(arr, val)
print(str(new_array)

