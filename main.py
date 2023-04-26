from src.Grammar import Grammar


def main():
    grammar = Grammar(
        ['S', 'A', 'B', 'C', 'D'],
        ['a', 'b'],
        {
            'S': ['bA', 'BC'],
            'A': ['a', 'aS', 'bAaAb'],
            'B': ['A', 'bS', 'aAa'],
            'C': ['', 'AB'],
            'D': ['AB']
        },
        'S',
        sort=False
    )

    cnf = grammar.to_cnf()
    print("CNF production", cnf.production)
    print("CNF non terminals", cnf.non_terminal)
    print("CNF terminals", cnf.terminal)


if __name__ == '__main__':
    main()
