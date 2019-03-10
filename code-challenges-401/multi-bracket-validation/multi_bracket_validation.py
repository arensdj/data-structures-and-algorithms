from stacks_and_queues import Stack

def multi_bracket_validation(input):
    """
    Summary of multi_bracket_validation function: Given an input string as its only argument, returns a boolean representing whether or not the brackets in the string are balanced. There are 3 types of brackets:  (), {}, []

    Attributes:
    input (string)

    Returns:
    True if brackets in input string are balanced
    False if brackets in input string not balanced
    """
    pairs_dict = {'[': ']', '{': '}', '(': ')'}
    bracket_stack = Stack()

    input_list = list(input)

    # print('input: ', str(input_list))

    opening_bracket = pairs_dict.keys()
    closing_bracket = pairs_dict.values()

    # For each bracket in input list, determine if it is an opening bracket.
    # If bracket is an opening bracket, push bracket on stack.  If bracket is a
    # closing bracket, determine if it corresponds to matching opening bracket. 
    # If key value pair matches, pop opening bracket off stack.
    for bracket in (input_list):
        if bracket in opening_bracket:
            print('Bracket: ', str(bracket))
            bracket_stack.push(bracket)
        elif bracket in closing_bracket:
            print('Bracket: ', str(bracket))

            for key, value in pairs_dict.items():
                if value == bracket:
                    bracket_stack.pop()
      
    if bracket_stack.peek():
        return False
    else:
        return True
