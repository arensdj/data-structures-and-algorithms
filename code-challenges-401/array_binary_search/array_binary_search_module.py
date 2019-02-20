""" 
  This is a  
"""
def binary_search(arr, val):
    index = -1
    start = 0
    end = len(arr) - 1
    found = False

    while (found == False) and (start <= end):
        # import pdb; pdb.set_trace()
        middle_index = (start + end) // 2

        if (val == arr[middle_index]):
            index = middle_index
            found = True
        else:
            if (val < arr[middle_index]):
                end = middle_index - 1
            else:
                start = middle_index + 1
        
    return index