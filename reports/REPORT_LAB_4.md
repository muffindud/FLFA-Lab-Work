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
    # 1. Create an empty list to store all nullable non-terminals
    # 2. Identify all directly nullable non-terminals by checking if any of their productions are epsilon
    # 3. Identify all indirectly nullable non-terminals by checking if any of their productions contain only nullable non-terminals
    # 4. Repeat step 3 until there are no more new nullable non-terminals
    # 5. Add new productions for all non-terminals that contain nullable non-terminals
    # 6. Remove all epsilon productions
    return prod, list(prod.keys())
```

1.2 Unit production elimination
```py
def eliminate_renaming(prod, vn):
    # 1. Check if there are any unit productions
    # 2. Remove all unit productions and replace them with the productions of the non-terminal they produce
    # 3. Repeat steps 1 and 2 until there are no more unit productions
    # 4. Remove all productions that produce the same non-terminal
    return prod, list(prod.keys())
```

1.3 Inaccessible symbols elimination
```py
def eliminate_inaccessible(start, prod, vn):
    # 1. Create a list to store all accessible non-terminals starting with the start value
    # 2. For every new value in the accessible add to the accessible list all non-terminals that are in the productions of the current non-terminal
    # 3. Repeat step 2 until there are no more new accessible non-terminals
    # 4. Remove all non-terminals from the production that are not accessible
    return prod, list(prod.keys())
```

1.4 Unproductive symbols elimination
```py
def eliminate_non_productive(prod, vt):
    # 1. Create an empty list to store all productive non-terminals
    # 2. Identify all directly productive non-terminals by checking if any of their productions are only terminals
    # 3. Identify all indirectly productive non-terminals by checking if any of their productions contain only productive non-terminals
    # 4. Repeat step 3 until there are no more new productive non-terminals
    # 5. Remove all non-productive productions
    return prod, list(prod.keys())
```

2.1 CNF conversion
```py
def to_cnf(self):
    # Create temporary variables for the processing

    # Eliminate epsilon productions
    # Eliminate unit productions
    # Eliminate inaccessible symbols
    # Eliminate unproductive symbols

    # 1. Create new non-terminals for all terminal values
    # 2. Replace all terminal values with the new non-terminals in the productions
    # 3. Identify all the productions that have more than 2 non-terminals
    # 4. Create new non-terminals for all the productions identified in step 3
    # 5. Replace all the productions identified in step 3 with the new non-terminals
    # 6. Repeat steps 3, 4 and 5 until there are no more productions with more than 2 non-terminals
    # 7. Return a new Grammar object with the new CNF grammar
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