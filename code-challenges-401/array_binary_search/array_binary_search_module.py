""" 
  This is a  
"""
def binary_search(arr, val):
    index = -1
    start = 0
    end = len(arr) - 1
    found = False

    print('Arr: ' + str(arr))

    while (found == False):
        # import pdb; pdb.set_trace()
        middle_index = (start + end) // 2

        # print('Middle index: ' + str(middle_index))
        
        if (middle_index == -1):
            # test condition when array is empty.  Value of middle_index will be -1
            break
        if (val == arr[middle_index]):
            index = middle_index
            found = True
        else:
            if (val < arr[middle_index]):
                end = middle_index - 1
            else:
                start = middle_index + 1
        
        # print('Value: ' + str(middle_index))

    return index

# input_array = []
# value = 2
# print('Input array: ' + str(input_array) + ' Value: ' + str(value))
# # print
# result = binary_search(input_array, 2)
# print(str(result))