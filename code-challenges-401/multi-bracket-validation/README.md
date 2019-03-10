# Multi-bracket Validation.
# Given an input string as its only argument, returns a boolean representing 
# whether or not the brackets in the string are balanced. There are 3 types 
# of brackets:  (), {}, []

## Challenge
# Figuring out how to match the brackets when the input string contains mutilple
# brackets and combinations where there are brackets inside other brackets.

## Approach & Efficiency
# Utilized a dictionary to contain the valid bracket symbols.  The opening 
# bracket is the key and the closing bracket is the value.  Created a list
# that contains the key values for opening brackets and a second list containing 
# the values of the closing brackets.  As each bracket is processed, an opening
# bracket is pushed onto a stack.  When a closing bracket is processed, it is
# checked to verify if it matches the key in the dictionary.  For each match
# the matching opening bracket is popped of the stack.
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

## Solution
<!-- Embedded whiteboard image -->