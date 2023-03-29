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
```py
def min_len_index(arr):
    # Returns the index of the minimum length string from an array


class Grammar:
    # Grammar parameters

    def __init__(self, non_terminal, terminal, production, start):
        # Initialize the grammar

        for key in self.production:
            # Sort the productions by length
            # Place the self containg productions at the end

    def check(self, s):
        # Check if a string is valid (terminal)

    def generate_string(self, no=5):
        # Generate n strings from the grammar
        # Place every string containing a non terminal in 'strings'
        # Place every string containing only terminals in 'final_strings'
        while len(final_strings) < no:
            # Will check if the string is not present in 'strings'
            # If it is, will go for the next state
            # If not present, will advance the state

        return final_strings

    def to_finite_automaton(self):
        # Will convert the grammar to a finite automaton
        transitions = {}
        for p in self.production.keys():
            # Convert production to transitions

        for p in self.production.keys():
            # Identify terminal and not-terminal states

        final = ['']

        return FiniteAutomaton(self.non_terminal, self.terminal, self.start, transitions, final)
```

### FinalAutomata.py
```py
class FiniteAutomaton:
    # Finite Automaton parameters

    def __init__(self, states, alphabet, initial_state, transitions, final_states):
        # Initialize the finite automaton

    def check(self, string):
        # Start from the initial state

        for char in string:
            # Check if the state has a transition for the current character
            # If it does, advance the state
            # If not, return False

        return current_state in self.final_states
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
