class DFA:
    states = []
    alphabet = []
    initial_state = ''
    final_states = []
    transitions = {}

    def __init__(self, states, alphabet, initial_state, final_states, transitions):
        self.states = states
        self.alphabet = alphabet
        self.initial_state = initial_state
        self.final_states = final_states
        self.transitions = transitions