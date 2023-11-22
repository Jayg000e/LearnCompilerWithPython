# DFA implementation that accepts (a|b)*abb

class DFA:
    def __init__(self):
        self.current_state = 'A'
        self.accept_state = 'E'
        self.states = {
            'A': {'a': 'B', 'b': 'C'},
            'B': {'a': 'B', 'b': 'D'},
            'C': {'a': 'B', 'b': 'C'},
            'D': {'a': 'B', 'b': 'E'},
            'E': {'a': 'B', 'b': 'C'}
        }

    def transition(self, input_char):
        if input_char in self.states[self.current_state]:
            self.current_state = self.states[self.current_state][input_char]
            return True
        else:
            return False  # Invalid input

    def is_accepting(self):
        return self.current_state == self.accept_state

    def reset(self):
        self.current_state = 'A'

    def __str__(self):
        return self.current_state

# Example usage
dfa = DFA()

# Process a string input through the DFA
input_string = "abba"
for char in input_string:
    if not dfa.transition(char):
        print(f"Invalid input: {char}")
        break
else:
    if dfa.is_accepting():
        print(f"The string '{input_string}' was processed successfully and reached the accepting state {dfa}.")
    else:
        print(f"The string '{input_string}' was processed successfully but did not reach the accepting state. Current state: {dfa}")

# Reset the DFA and try another string
dfa.reset()
input_string = "aababb"
for char in input_string:
    if not dfa.transition(char):
        print(f"Invalid input: {char}")
        break
else:
    if dfa.is_accepting():
        print(f"The string '{input_string}' was processed successfully and reached the accepting state {dfa}.")
    else:
        print(f"The string '{input_string}' was processed successfully but did not reach the accepting state. Current state: {dfa}")
