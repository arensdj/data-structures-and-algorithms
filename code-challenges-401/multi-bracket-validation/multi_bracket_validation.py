from stacks_and_queues import Stack

def multi_bracket_validation(input):
    pairs_dict = {'[': ']', '{': '}', '(': ')'}
    bracket_stack = Stack()

    input_list = list(input)

    # print('input: ', str(input_list))

    opening_bracket = pairs_dict.keys()
    closing_bracket = pairs_dict.values()

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
