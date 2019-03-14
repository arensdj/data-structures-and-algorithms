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

## Solution
<!-- Embedded whiteboard image -->