from Grammar import Grammar


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

    print(grammar.production)
    grammar = grammar.to_cnf()


if __name__ == '__main__':
    main()
