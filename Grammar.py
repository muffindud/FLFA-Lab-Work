from FiniteAutomaton import FiniteAutomaton


def min_len_index(arr):
    m = 0
    for i in range(len(arr)):
        if len(arr[i]) < len(arr[m]):
            m = i
    return m


class Grammar:
    non_terminal = []
    terminal = []
    production = {}
    start = ''

    def __init__(self, non_terminal, terminal, production, start):
        self.non_terminal = non_terminal
        self.terminal = terminal
        self.production = production
        self.start = start

        for key in self.production:
            self.production[key].sort(key=lambda st: len(st))
            for start in self.production[key]:
                if key in start:
                    for i in range(len(self.production[key])):
                        if self.production[key] == start and i < len(self.production[key]) - 1:
                            self.production[key].pop(i)
                            self.production[key].append(start)

    # Check if a string is valid (terminal)
    def check(self, s):
        return not any(c not in self.terminal for c in s)

    def generate_string(self, no=5):
        strings = []
        final_strings = []
        string = self.start
        strings.append(string)
        while len(final_strings) < no:
            for c in string:
                if c in self.non_terminal:
                    ind = 0
                    initial_string = string
                    string = string.replace(c, self.production[c][ind], 1)
                    if string in final_strings:
                        string = initial_string
                        ind += 1
                        string = string.replace(c, self.production[c][ind], 1)

                    if not self.check(string):
                        strings.append(string)

            if self.check(string) and string not in final_strings:
                final_strings.append(string)
                string = strings[-1]

        return final_strings

    def to_finite_automaton(self):
        transitions = {}
        for p in self.production.keys():
            for s in self.production[p]:
                for c in s:
                    if c in self.terminal:
                        if (p, c) not in transitions.items():
                            transitions[(p, c)] = []

        for p in self.production.keys():
            for s in self.production[p]:
                n = ''
                t = ''
                for c in s:
                    if c in self.terminal:
                        t = c
                    if c in self.non_terminal:
                        n = c
                    if n not in transitions[(p, t)] and n != '':
                        transitions[(p, t)].append(n)

        final = ''
        for p in transitions.keys():
            if not transitions[p]:
                final = p[1]
        return FiniteAutomaton(self.non_terminal, self.terminal, self.start, transitions, final)
