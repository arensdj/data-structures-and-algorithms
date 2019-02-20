def insertShiftArray(original_arr, val):
  middle_position = (len(original_arr) // 2)
  print('Middle position: ' + str(middle_position))
  new_arr = []

  if (len(original_arr) % 2 == 0):
    for i in range(middle_position):
      new_arr.append(original_arr[i])
  else:
    for i in range(0, middle_position + 1):
      new_arr.append(original_arr[i])

  new_arr.append(val)

  for i in range( len(new_arr), len(original_arr) + 1):
    new_arr.append(original_arr[i - 1])

  return new_arr