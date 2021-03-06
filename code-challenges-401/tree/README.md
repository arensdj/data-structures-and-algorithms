# Trees
# This is a Binary Tree data structure in which each node has at 
# most two child nodes which are referred to as the left child 
# and the right child.

## Challenge
# The challenge was understanding how to add a new value into the tree.  The
# first value is the root node.  All subsequent values added will be done by
# comparing the new value to the value of the root node.  If value is less
# than the root node value, the new value get added to the left child.  Otherwise,
# the new value gets added to the right child.  Also, the traversal of the tree
# is tricky.  Preorder, inorder and postorder have a particular sequence.  Each of
# them are clearly explained in the docstring.

## Approach & Efficiency
# Used a recursive routine was used when traversing the binary tree to produce
# a particular traversal order and when checking if a particular value exists
# in the binary tree.

## API
# None

# Breadth-first
# Write a breadth first traversal method which takes a Binary Tree as its unique input. 
# Without utilizing any of the built-in methods available to your language, traverse the 
# input tree using a Breadth-first approach. Prints every visited node’s value.

## Challenge
# Managing the tree nodes in a queue and dequeueing the tree nodes.

## Approach & Efficiency
# Using a queue, added each tree node onto the queue while traversing the binary tree
# adding each left child and right child.  But needed to capture each node by dequeueing
# it and accessing the node value and adding it to an array before adding another tree
# node into the queue.


# Find the Maximum Value in a Binary Tree
# This function takes binary tree as its only input. Without utilizing any of the built-in methods available to your language, returns the maximum value stored in the tree. It is assumed that the values stored in the Binary Tree will be numeric.

## Challenge
# Write a recursive routine that will search the left half and right half of binary 
# tree searching for the max value and returning the max value.

## Approach & Efficiency
# Traverse each half of the binary tree searching for the max value of each half.
# Compare the max value of the left half and right half to the root value and 
# return the max value of the three values.

## Solution
