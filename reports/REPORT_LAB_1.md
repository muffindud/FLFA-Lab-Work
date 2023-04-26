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
    # The constructor for the Grammar class takes the following parameters:
    #   - states: a list of states
    #   - alphabet: a list of characters
    #   - initial_state: the initial state
    #   - transitions: a dictionary of transitions

    # If the sort parameter is set to True, the productions will be sorted by length 
    # and place the self-contained productions at the end
```

### String check
```py
def check(self, s):
    # Check if all the characters in the string are in the alphabet
    # If not, return False
```

### String generation
```py
def generate_string(self, no=5):
    # 1. Create an empty array to store valid strings containing terminals and non-terminals
    # 2. Create an empty array to store valid strings containing only terminals
    # 3. Start from a string containing only the initial state
    # 4. Each iteration, replace a non-terminal form the string with a production and add it to the strings list if it's
    #    not already there, else use the next state for the not-terminal
    # 5. If the string contains only terminals, add it to the terminals list and take the last string from the strings list
    # 6. Repeat until the number of strings is reached
    # 7. Return the terminals list
    return final_strings
```

### Finite Automaton conversion
```py
def to_finite_automaton(self):
    # 1. Create an empty dictionary to store the transitions
    # 2. For each production, add a transition to the dictionary
    # 3. For each production, if the production is self-contained, add the state to the final states
    # 4. Return the FiniteAutomaton object
```

### FinalAutomata.py
```py
class FiniteAutomaton:
    # The constructor for the FiniteAutomaton class takes the following parameters:
    #   - states: a list of states
    #   - alphabet: a list of characters
    #   - initial_state: the initial state  
    #   - final_states: a list of final states
    #   - transitions: a dictionary of transitions
```

### String check
```py
def check(self, string):
    # 1. Check if the string has a transition for the current character
    # 2. If it does, check if the string is valid for the next state
    # 3. If it doesn't, return False
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
