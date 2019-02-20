# Array Shift
# This program takes an input array and a value and inserts that value in the middle 
# of the array.

## Challenge
# The challenge was finding the middle of the input array for odd and even elements and insert input value.    

## Approach & Efficiency
# Compute the middle of the array using floor division.  If the input array contains even
# number elements, the exact position to insert the input value is the number of array
# elements divided by two.  If input array has odd number of elements, the exact position to 
# insert the input value is the middle of the array plus one.  A new array is created to
# contain the input array with the input value inserted in the middle.
 
## Solution
# A function was written to compute the middle of the array using floor division.  For an input array that
# contains even number elements, the exact position to insert the input value is the number of array
# elements divided by two.  To handle an input array has odd number of elements, the exact position to 
# insert the input value is the middle of the array plus one.  A new array is created to
# contain the input array with the input value inserted in the middle.  The remaining elements of input
# array was appended after the input value was added.  The new array is returned.

![alt text](https://github.com/arensdj/data-structures-and-algorithms/blob/master/code-challenges-401/assets/array_shift.pdf)
<!-- Embedded whiteboard image -->
