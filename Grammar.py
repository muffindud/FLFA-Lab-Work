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

    def __init__(self, non_terminal, terminal, production, start, sort=True):
        self.non_terminal = non_terminal
        self.terminal = terminal
        self.production = production
        self.start = start

        if sort:
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

    # Generates no. corresponding strings
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

    # Converts Grammar ot NFA
    def to_nfa(self):
        from FinalAutomata import FinalAutomata

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
                if not transitions[(p, t)]:
                    transitions[(p, t)].append('')

        final = ['']

        return FinalAutomata(self.non_terminal, self.terminal, self.start, transitions, final)

    # Returns the classification of the grammar
    def get_classification(self):
        classification = '3'

        for p in self.production.keys():
            if len(p) > 1:
                classification = '1'
                break
            for s in self.production[p]:
                if len(s) == 0:
                    pass
                elif len(s) > 2 or s[0] in self.non_terminal or (len(s) == 2 and s[1] in self.terminal):
                    classification = '2'

        for p in self.production.keys():
            if any(c in p for c in self.terminal):
                classification = '0'
                break

        return classification

    # Eliminates epsilon productions
    @staticmethod
    def eliminate_epsilon(prod, vn):
        # Find all initial nullable non-terminals
        nullable = []
        for p in prod.keys():
            for s in prod[p]:
                if s == '' and p not in nullable:
                    nullable.append(p)

        # Find all deductible nullable non-terminals
        new_nullable = True
        while new_nullable:
            new_nullable = False
            for p in prod.keys():
                for s in prod[p]:
                    if all(c in nullable for c in s) and p not in nullable:
                        nullable.append(p)
                        new_nullable = True

        # Eliminate epsilon productions
        for p in list(prod.keys()):
            for s in prod[p]:
                for c in s:
                    if c in nullable:
                        prod[p].append(s.replace(c, ''))

            # Remove production if is epsilon
            if p in nullable:
                prod[p].remove('')
                if not prod[p]:
                    del prod[p]

        return prod, list(prod.keys())

    # Eliminates renaming
    @staticmethod
    def eliminate_renaming(prod, vn):
        # Identify unit productions
        new_unit = True
        while new_unit:
            new_unit = False
            for p in list(prod.keys()):
                for s in prod[p]:
                    if len(s) == 1 and s in vn:
                        new_unit = True
                        for u in prod[s]:
                            if u not in prod[p]:
                                prod[p].append(u)
                        prod[p].remove(s)

        return prod, list(prod.keys())

    # Eliminates inaccessible productions
    @staticmethod
    def eliminate_inaccessible(start, prod, vn):
        accessible = [start]
        for p in prod.keys():
            for s in prod[p]:
                for c in s:
                    if c in vn and c not in accessible:
                        accessible.append(c)

        for p in list(prod.keys()):
            if p not in accessible:
                del prod[p]

        return prod, list(prod.keys())

    # Eliminates non-productive productions
    @staticmethod
    def eliminate_non_productive(prod, vt):
        productive = []
        for p in prod.keys():
            for s in prod[p]:
                if all(c in vt for c in s):
                    productive.append(p)

        new_productive = True
        while new_productive:
            new_productive = False
            for p in prod.keys():
                for s in prod[p]:
                    has_non_productive = False
                    for c in s:
                        if c in vt and c not in productive:
                            has_non_productive = True
                    if not has_non_productive:
                        if p not in productive:
                            productive.append(p)
                            new_productive = True

        for p in list(prod.keys()):
            if p not in productive:
                del prod[p]

        return prod, list(prod.keys())

    def to_cnf(self):
        vt = self.terminal
        vn = self.non_terminal
        prod = self.production
        start = self.start

        prod, vn = self.eliminate_epsilon(prod, vn)
        prod, vn = self.eliminate_renaming(prod, vn)
        prod, vn = self.eliminate_inaccessible(start, prod, vn)
        prod, vn = self.eliminate_non_productive(prod, vt)

        return Grammar(vn, vt, prod, start, False)
