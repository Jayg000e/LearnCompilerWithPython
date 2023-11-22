grammar = {
    1: ("E", ["E", "+", "T"]),
    2: ("E", ["T"]),
    3: ("T", ["T", "*", "F"]),
    4: ("T", ["F"]),
    5: ("F", ["(", "E", ")"]),
    6: ("F", ["id"])
}

action = {
    (0, 'id'): ('s', 5),
    (0, '('): ('s', 4),
    (1, '+'): ('s', 6),
    (1, '$'): ('acc',),  # Accept
    (2, '+'): ('r', 2),
    (2, '*'): ('s', 7),
    (2, ')'): ('r', 2),
    (2, '$'): ('r', 2),
    (3, '+'): ('r', 4),
    (3, '*'): ('r', 4),
    (3, ')'): ('r', 4),
    (3, '$'): ('r', 4),
    (4, 'id'): ('s', 5),
    (4, '('): ('s', 4),
    (5, '+'): ('r', 6),
    (5, '*'): ('r', 6),
    (5, ')'): ('r', 6),
    (5, '$'): ('r', 6),
    (6, 'id'): ('s', 5),
    (6, '('): ('s', 4),
    (7, 'id'): ('s', 5),
    (7, '('): ('s', 4),
    (8, '+'): ('s', 6),
    (8, ')'): ('s', 11),
    (9, '+'): ('r', 1),
    (9, '*'): ('s', 7),
    (9, ')'): ('r', 1),
    (9, '$'): ('r', 1),
    (10, '+'): ('r', 3),
    (10, '*'): ('r', 3),
    (10, ')'): ('r', 3),
    (10, '$'): ('r', 3),
    (11, '+'): ('r', 5),
    (11, '*'): ('r', 5),
    (11, ')'): ('r', 5),
    (11, '$'): ('r', 5),
}

goto = {
    (0, 'E'): 1,
    (0, 'T'): 2,
    (0, 'F'): 3,
    (4, 'E'): 8,
    (4, 'T'): 2,
    (4, 'F'): 3,
    (6, 'T'): 9,
    (6, 'F'): 3,
    (7, 'F'): 10,
}


def parse_slr(input_tokens):
    # Initialize the parser state
    stack = [0]  # start with initial state 0
    input_tokens.append('$')  # append end-of-input symbol
    idx = 0  # start with the first token
    a = input_tokens[idx]  # current input token
    
    # Main parsing loop
    while True:
        s = stack[-1]  # top state of the stack
        if (s, a) in action:
            action_entry = action[(s, a)]
            if action_entry[0] == 's':  # shift action
                stack.append(action_entry[1])  # push next state
                idx += 1  # move to next token
                a = input_tokens[idx] if idx < len(input_tokens) else '$'  # update current input token
            elif action_entry[0] == 'r':  # reduce action
                # Number of symbols on RHS of production
                rule_len = len(grammar[action_entry[1]][1])
                if len(stack) >= rule_len + 1:  # check stack length before popping
                    stack = stack[:-rule_len]  # pop symbols off stack
                else:
                    print("Error: stack underflow during reduce action.")
                    break
                t = stack[-1]  # new top state of the stack
                non_terminal = grammar[action_entry[1]][0]  # LHS of production
                if (t, non_terminal) in goto:  # ensure GOTO entry exists
                    stack.append(goto[(t, non_terminal)])  # push new state from GOTO table
                    print(f"Reduced by rule: {action_entry[1]} {grammar[action_entry[1]]}")
                else:
                    print("Error: GOTO entry missing for state and non-terminal.")
                    break
            elif action_entry[0] == 'acc':  # accept action
                print("Parsing is done. Input is accepted.")
                break
        else:
            print(f"Error: Invalid action for state {s} and symbol {a}.")
            break

# Example usage
test_input = ['id', '+', 'id', '*', 'id']
parse_slr(test_input)

test_input = ['(','id', '+', 'id', ')','*', 'id']
parse_slr(test_input)
