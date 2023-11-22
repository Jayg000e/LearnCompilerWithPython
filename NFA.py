# NFA implementation that accepts (a|b)*abb
class NFA:
    def __init__(self):
        self.transitions = {
            0: {'ε': [1, 7]},
            1: {'ε': [2, 4]},
            2: {'a': [3]},
            3: {'ε': [6]},
            4: {'b': [5]},
            5: {'ε': [6]},
            6: {'ε': [1, 7]},
            7: {'a': [8]},
            8: {'b': [9]},
            9: {'b': [10]},
            10: {}  # No transitions from the accepting state
        }
        self.accept_states = {10}
        self.start_state = 0

    def epsilon_closure(self, states):
        closure = set(states)
        stack = list(states)

        while stack:
            state = stack.pop()
            for next_state in self.transitions.get(state, {}).get('ε', []):
                if next_state not in closure:
                    closure.add(next_state)
                    stack.append(next_state)
        return closure

    def move(self, states, input_char):
        next_states = set()
        for state in states:
            next_states.update(self.transitions.get(state, {}).get(input_char, []))
        return next_states

    def accepts(self, input_str):
        current_states = self.epsilon_closure({self.start_state})
        for char in input_str:
            current_states = self.move(current_states, char)
            current_states = self.epsilon_closure(current_states)
        return any(state in self.accept_states for state in current_states)

# Example usage
nfa = NFA()
nfa_result = nfa.accepts('aaabb')
print(nfa_result)
nfa_result = nfa.accepts('aaaba')
print(nfa_result)
