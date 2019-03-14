# FizzBuzz Tree
# Write a function called FizzBuzzTree which takes a tree as an argument.
# Without utilizing any of the built-in methods available to your language
# determine whether or not the value of each node is divisible by 3, 5 or both, 
# and change the value of each of the nodes:
# If the value is divisible by 3, replace the value with “Fizz”
# If the value is divisible by 5, replace the value with “Buzz”
# If the value is divisible by 3 and 5, replace the value with “FizzBuzz”
# Return the tree with its new values.

## Challenge
# The challenge was to writing a recursive function that will evaluate each
# node value in the tree.

## Approach & Efficiency
# Once a current node was set to the root node of the binary search tree,
# check if the current node has a left child and a right child.  If it 
# does, the FizzBuzzTree function was called.  This is where the recursion
# happens.  And the node value is evaluated and changed accordingly.

## Solution