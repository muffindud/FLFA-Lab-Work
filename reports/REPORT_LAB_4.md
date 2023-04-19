# Chomsky Normal Form
#### Course: Formal Languages and Finite Automata
#### Author: Corneliu Catlabuga FAF-213

## Theory:
The grammar for the laboratory work (v9):
```
VN={S, A, B, C, D}, 
VT={a, b},
P={ 
    S → bA
    S → BC
    A → a
    A → aS
    A → bAaAb
    B → A
    B → bS
    B → aAa
    C → ε
    C → AB
    D → AB
}
```

## Objectives:
1. Learn about Chomsky Normal Form (CNF) [1].
1. Get familiar with the approaches of normalizing a grammar.
1. Implement a method for normalizing an input grammar by the rules of CNF.
    1. The implementation needs to be encapsulated in a method with an appropriate signature (also ideally in an appropriate class/type).
    1. The implemented functionality needs executed and tested.
    1. A BONUS point will be given for the student who will have unit tests that validate the functionality of the project.
    1. Also, another BONUS point would be given if the student will make the aforementioned function to accept any grammar, not only the one from the student's variant.

## Implementation description
The implemented procedures are in the Grammar.py file, as an extension of the Grammar class.
The new functions are:
1.1 Epsilon elimination
```py
def eliminate_epsilon(prod):
    # Create an initial list of directly nullable non-terminals
    # Adds to the list all the deduced indirect nullable non-terminals
    # Removes the nullable non-terminals from the productions and replaces them with the corresponding productions
    return prod, list(prod.keys())
```

1.2 Unit production elimination
```py
def eliminate_renaming(prod, vn):
    # Identify unit productions
    # Eliminate unit productions until there are no more
    return prod, list(prod.keys())
```

1.3 Inaccessible symbols elimination
```py
def eliminate_inaccessible(start, prod, vn):
    # Identify all accessible non-terminals
    # Eliminate all inaccessible non-terminals
    return prod, list(prod.keys())
```

1.4 Unproductive symbols elimination
```py
def eliminate_non_productive(prod, vt):
    # Identify all initially productive non-terminals
    # Identify all newly productive non-terminals until there are no more
    # Eliminate all unproductive non-terminals
    return prod, list(prod.keys())
```

2.1 CNF conversion
```py
def to_cnf(self):
    # Create temporary variables

    # Eliminate epsilon productions
    # Eliminate unit productions
    # Eliminate inaccessible symbols
    # Eliminate unproductive symbols

    # Create productions for terminal variables

    # Replace the terminal values in productions with new non-terminal variables
    
    # Create new non-terminal variables for productions with more than 2 symbols
    
    return Grammar(vn, vt, prod, start, False)
```

## Results:
The unittests have been implemented for each new function individually, as well as for the whole CNF conversion function. The unit tests are implemented in the `test_Grammar.py` file.

Running the main.py file in the commit `904cecc` will generate the following output:
```text
CNF production {'S': ['EA', 'BC', 'ES', 'DF', 'D', 'DS', 'EG'], 'A': ['D', 'DS', 'EH'], 'B': ['ES', 'DI', 'D', 'DS', 'EJ'], 'C': ['AB'], 'D': ['a'], 'E': ['b'], 'F': ['AD'], 'G': ['AK'], 'H': ['AL'], 'I': ['AD'], 'J': ['AM'], 'K': ['DN'], 'L': ['DO
'], 'M': ['DP'], 'N': ['AE'], 'O': ['AE'], 'P': ['AE']}
CNF non terminals ['S', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
CNF terminals ['a', 'b']
```