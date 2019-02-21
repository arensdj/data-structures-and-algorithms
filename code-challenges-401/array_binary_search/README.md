# Array Shift

#Giving attribution to the following sight which helped understand binary search
#https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-1.php

# This program takes an input array and a value and searches array for the value returning 
# the index of the matching element.  Returns -1 if not found.

## Challenge
# Finding how to break the array into chunks as array is searched for input value.      

## Approach & Efficiency
#  Search for the input value using the middle index value of the array.  The value
#  could equal the middle index element on the first search.  But if not, the algorithm
#  needs to check if the input value is less than or greater then the middle index
#  element.
 
## Solution
#  Determine the middle index of array, the first and last index of array.  Interate
#  while the value is not found and first index is <=> last index of array.  Determine
#  middle index of array.  If middle index element is equal to input value, return the
#  middle index.  Otherwise, check if input value is either to the left of the middle 
#  index or to the right of it.  The start index and end index is reassigned.  The 
#  important thing to do is omit the previous middle index in this compution. 

![alt text](https://github.com/arensdj/data-structures-and-algorithms/blob/master/code-challenges-401/assets/binary_search.pdf)
<!-- Embedded whiteboard image -->
