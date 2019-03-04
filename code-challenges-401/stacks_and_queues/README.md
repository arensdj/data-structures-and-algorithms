# Stack and Queue Class
# The purpose of this program is to provide a stack and queue class. 

## Challenge
# The challenge was understanding the difference between FIFO and LIFO and how this affects the way a # stack and a queue are processed in terms of adding and removing nodes and viewing the first node.

## Approach & Efficiency
# Define three separate classes: a Stack, Queue and Node class.
# The Node class will contain the value being added to the linked list.  It also must have a property
# that references the next Node object in the linked list.
#
# The Stack class has a top property. It creates an empty stack when instantiated.  An instance of 
# this object is aware of a default empty value assigned to top when the stack is created. It has 
# methods which add and remove a node and peeks which returns the value of the node on the top of 
# the stack.
#
# The Queue class has a top property. It creates an empty queue when instantiated.  An instance of this
# class is aware of a default empty value assigned to front.  It has methods which enqueue and dequeue
# nodes from the front of the queue and peeks which returns the value of the node in front of the queue

## API
# There are no APIs in this program.