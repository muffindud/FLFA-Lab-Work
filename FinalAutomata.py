class FinalAutomata:
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

    def to_grammar(self):
        from Grammar import Grammar

        production = {}

        for t in self.transitions.keys():
            if t[0] not in production.keys():
                production[t[0]] = []

        for t in self.transitions.keys():
            for s in self.transitions[t]:
                if t[1] + s not in production[t[0]]:
                    production[t[0]].append(t[1] + s)

        return Grammar(self.states, self.alphabet, production, self.initial_state)

    def get_type(self):
        for t in self.transitions:
            if len(self.transitions[t]) > 1:
                return 'NFA'
        return 'DFA'

    def to_dfa(self):
        dfa_final_states = []
        dfa_transitions = {}

        dfa_states = [[self.initial_state]]

        for states in dfa_states:
            for s in states:
                new_states = []
                state_terminals = []
                for c in self.alphabet:
                    if (s, c) in self.transitions.keys():
                        new_states.append(self.transitions[(s, c)])
                        state_terminals.append(c)
                for ns in new_states:
                    if ns and ns not in dfa_states:
                        dfa_states.append(ns)
                for i in range(len(new_states)):
                    if new_states[i]:
                        dfa_transitions[(tuple(states), state_terminals[i])] = new_states[i]

        for states in dfa_states:
            if self.final_states in states:
                dfa_final_states.append(states)

        return FinalAutomata(dfa_states, self.alphabet, self.initial_state, dfa_transitions, dfa_final_states)

    def show_graph(self, name='graph'):
        import graphviz as gv

        graph = gv.Digraph()

        for state in self.states:
            shape = 'circle' if state not in self.final_states else 'doublecircle'
            graph.node(repr(state), shape=shape)

        for state in self.transitions:
            for s in [self.transitions[state]]:
                graph.edge(repr(list(state[0])), repr(s), label=state[1])

        graph.view(filename=name+'.gv')
