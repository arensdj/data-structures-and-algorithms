""" 
  This is a binary search program that searches an input array for a value and
   returns the index to matching element in array or -1 if not found.
"""
def binary_search(arr, val):
    """
    Summary of binary_search function:  searches an input array for a value and
    returns the index to matching element in array or -1 if not found.

    Parameters:
    array (array): An array of values
    val (integer): An integer value
    
    Returns:
    index (integer): Returns index of array element
  """
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
            # reassign the end and start value excluding the middle index.
            if (val < arr[middle_index]):
                end = middle_index - 1
            else:
                start = middle_index + 1
        
    return index