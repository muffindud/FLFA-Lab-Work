class FiniteAutomaton:
    states = []
    alphabet = []
    initial_state = ''
    final_states = []
    transitions = {}

    def __init__(self, states, alphabet, initial_state, transitions, final_states):
        self.states = states
        self.alphabet = alphabet
        self.initial_state = initial_state
        self.transitions = transitions
        self.final_states = final_states

    def check(self, string):
        current_state = self.initial_state

        for char in string:
            if (current_state, char) in self.transitions:
                next_states = self.transitions[(current_state, char)]
                if not next_states:
                    return False
                current_state = next_states[0]
            else:
                return False

        return current_state in self.final_states
