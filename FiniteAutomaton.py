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
        # TODO
        pass
