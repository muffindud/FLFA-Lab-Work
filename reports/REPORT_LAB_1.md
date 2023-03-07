# Intro to formal languages. Regular grammars. Finite Automata.

#### Course: Formal Languages and Finite Automata
#### Author: Corneliu Catlabuga FAF-213

----

## Theory
The grammar for the laboratory work (v9):

```
VN={S, B, D, Q}, 
VT={a, b, c, d},
P={ 
    S → aB
    S → bB
    B → cD
    D → dQ
    Q → bB
    D → a
    Q → dQ
}
```

## Objectives:

1. Understand what a language is and what it needs to have in order to be considered a formal one.

2. Provide the initial setup for the evolving project that you will work on during this semester. I said project because usually at lab works, I encourage/impose students to treat all the labs like stages of development of a whole project. Basically you need to do the following:

    a. Create a local && remote repository of a VCS hosting service (let us all use Github to avoid unnecessary headaches);

    b. Choose a programming language, and my suggestion would be to choose one that supports all the main paradigms;

    c. Create a separate folder where you will be keeping the report. This semester I wish I won't see reports alongside source code files, fingers crossed;

3. According to your variant number (by universal convention it is register ID), get the grammar definition and do the following tasks:

    a. Implement a type/class for your grammar;

    b. Add one function that would generate 5 valid strings from the language expressed by your given grammar;

    c. Implement some functionality that would convert and object of type Grammar to one of type Finite Automaton;
    
    d. For the Finite Automaton, please add a method that checks if an input string can be obtained via the state transition from it;


## Implementation description

* The Grammar.py file holds the Grammar class with a min_len_index(arr) function which returns the index of the smallest length string from an array used for sorting the elements of each production key
* The FinalAutomata.py holds the FinalAutomata class

### Grammar.py
```
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
                if not transitions[(p, t)]:
                    transitions[(p, t)].append('')

        final = ['']

        return FiniteAutomaton(self.non_terminal, self.terminal, self.start, transitions, final)
```

### FinalAutomata.py
```
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

```

## main.py
```
from Grammar import Grammar


def main():
    g = Grammar(['S', 'B', 'D', 'Q'],
                ['a', 'b', 'c', 'd'],
                {'S': ['aB', 'bB'], 'B': ['cD'], 'D': ['dQ', 'a'], 'Q': ['dB', 'dQ']},
                'S')

    # The Grammar.generate_string(n) function will generate n (default: 5)
    # strings corresponding to the specified grammar
    strings = g.generate_string()
    print('Generated strings:')
    print(strings, end='\n\n')

    # The Grammar.to_finite_automaton will convert final automaton format
    fa = g.to_finite_automaton()
    print('Generated transition:')
    print(fa.transitions, end='\n\n')

    # The FinalAutomaton.check(s) will check if the string s is derived from
    # the transition
    print('Corresponding strings:')
    for s in strings:
        print(fa.check(s))

    print()

    # Un-corresponding strings
    print('Un-corresponding:')
    print(fa.check('aa'))
    print(fa.check('mna'))
    print(fa.check('acdca'))


if __name__ == '__main__':
    main()
```

## Conclusions / Screenshots / Results
#### Outuput:
```
Generated strings:
['aca', 'acddca', 'acddcddca', 'acddcddcddca', 'acddcddcddcddca']

Generated transition:
{('S', 'a'): ['B'], ('S', 'b'): ['B'], ('B', 'c'): ['D'], ('D', 'a'): [''], ('D', 'd'): ['Q'], ('Q', 'd'): ['B', 'Q']}

Corresponding strings:
True
True
True
True
True

Un-corresponding:
False
False
False
```
