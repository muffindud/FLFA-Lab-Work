class NFA:
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

    def show_graph(self):
        import networkx as nx
        import matplotlib.pyplot as plt

        G = nx.DiGraph()

        G.add_nodes_from(self.states)

        for t in self.transitions:
            for s in self.transitions[t]:
                G.add_edge(t[0], s, label=t[1])

        pos = nx.spring_layout(G)
        nx.draw_networkx_nodes(G, pos)
        nx.draw_networkx_edges(G, pos)
        nx.draw_networkx_labels(G, pos)
        nx.draw_networkx_edge_labels(G, pos)

        plt.show()
