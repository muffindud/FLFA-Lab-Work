# Determinism in Finite Automata. Conversion from NDFA 2 DFA. Chomsky Hierarchy.

---

#### Course: Formal Languages and Finite Automata
#### Author: Corneliu Catlabuga FAF-213

----

## Theory
The Finite Automata for the laboratory work (v9):

```
Q = {q0,q1,q2,q3,q4},
∑ = {a,b,c},
F = {q4},
δ(q0,a) = q1,
δ(q1,b) = q2,
δ(q2,c) = q0,
δ(q1,b) = q3,
δ(q3,a) = q4,
δ(q3,b) = q0.
```

## Tasks

---

1. Understand what an automaton is and what it can be used for.

2. Continuing the work in the same repository and the same project, the following need to be added:
    a. Provide a function in your grammar type/class that could classify the grammar based on Chomsky hierarchy.

    b. For this you can use the variant from the previous lab.

3. According to your variant number (by universal convention it is register ID), get the finite automaton definition and do the following tasks:

    a. Implement conversion of a finite automaton to a regular grammar.

    b. Determine whether your FA is deterministic or non-deterministic.

    c. Implement some functionality that would convert an NDFA to a DFA.
    
    d. Represent the finite automaton graphically (Optional, and can be considered as a __*bonus point*__):
      
    - You can use external libraries, tools or APIs to generate the figures/diagrams.
        
    - Your program needs to gather and send the data about the automaton and the lib/tool/API return the visual representation.

## Implementation

---

### Grammar classification
Returns the classification of the grammar based on Chomsky hierarchy.
```python
def get_classification(self):
    # 1. Create a variable to store the classification and start form the 3rd
    # 2. If all the right sides of the productions have only one non-terminal symbol, then the grammar is of type 3 
    #    else it's the 1st type
    # 3. If 1st type classification has been identified jump to step 6
    # 4. If all the right sides of the productions have only two non-terminal symbols, then the grammar is of type 2
    # 5. Repeat steps 2, 3, 4 for all productions
    # 6. If any of the productions has a terminal in the right side, then the grammar is of type 0
    # 7. Return the classification
    return classification
```

---

### Finite Automaton to Regular Grammar conversion
Converts a finite automaton to a regular grammar.
```py
def to_grammar(self):
    # 1. Create a variable to store the productions
    # 2. For each state in the finite automaton add an empty production
    # 3. For each transition create a production
    # 4. Repeat step 3 for all transitions
    # 5. Return the a grammar object
    return Grammar(self.states, self.alphabet, production, self.initial_state)
```

---

### Determinism check
Determines whether the finite automaton is deterministic or non-deterministic.
```py
def get_type(self):
    # Due to the way it's declared
    # The type can be determined by the type of transitions
    # If the transitions are a list, then the finite automaton is non-deterministic
    # If the transitions are a dictionary, then the finite automaton is deterministic
```

---

### Non-deterministic Finite Automaton to Deterministic Finite Automaton conversion
Converts a non-deterministic finite automaton to a deterministic finite automaton.
```py
def to_dfa(self):
    # Create a variable to store the states of the DFA
    # Create a variable to store the transitions of the DFA
    # Create a variable to store the final states of the DFA starting with an array with the initial state of the NFA
    
    # For each new DFA state:
    # 1. For each individual state in the DFA state identify new state and add it to the DFA states
    # 2. Repeat step 1 until all states have been identified
    # 3. Return a FinalAutomata object with the DFA states, alphabet, initial state, transitions and final states
    return FinalAutomata(dfa_states, self.alphabet, self.initial_state, dfa_transitions, dfa_final_states)
```

---

### Graphical representation
Generates a graphical representation of the finite automaton.
#### NOTE: Will only work if Graphviz is installed. If Graphviz is not installed, the function will generate a .gv file that can be used to generate the graph.
```python
def show_graph(self, name='graph'):
    # 1. Create a graph object
    # 2. Identify the type of the finite automaton
    # 3. Identify the final states of the finite automaton (for drawing purposes)
    # 4. Add the states to the graph
    # 5. Add the transitions to the graph
    # 6. Display the graph
    graph.view(filename=name+'.gv', directory='./graphs/')
```

## Output

---

```
Task 2:
Grammar classification: 3

Task 3a:
Grammar non-terminals:  ['q0', 'q1', 'q2', 'q3', 'q4']
Grammar terminals:  ['a', 'b', 'c']
Grammar start:  q0
Grammar productions:  {'q0': ['aq1'], 'q1': ['bq2', 'bq3'], 'q2': ['cq0'], 'q3': ['aq4', 'bq0']}

Task 3b:
FA1: NFA

Task 3c:
FA2: DFA
DFA states:  [['q0'], ['q1'], ['q2', 'q3'], ['q4']]
DFA alphabet:  ['a', 'b', 'c']
DFA initial state:  q0
DFA transitions:  {(('q0',), 'a'): ['q1'], (('q1',), 'b'): ['q2', 'q3'], (('q2', 'q3'), 'c'): ['q0'], (('q2', 'q3'), 'a'): ['q4'], (('q2', 'q3'), 'b'): ['q0']}
DFA final states:  [['q4']]
```

### Graphical representation
![NFA Graph](graphs/nfa.jpg) ![DFA Graph](graphs/dfa.jpg)