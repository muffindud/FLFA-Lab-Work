# Lexer and Scaner
#### Course: Formal Languages and Finite Automata
#### Author: Corneliu Catlabuga FAF-213

## Theory:
The laboratory work is implemented on the following token dictionary:
##### NOTES: 
1. The order in which tokens are defined is important.

```py
tokens = {
    # Program structure
    "BLOCK_START": r"\{",
    "BLOCK_END": r"\}",
    "NEWLINE": r"\n | \r | \r \n",
    "WHITESPACE": r"[ ]+",

    # Operators
    "ASSIGNMENT": r"=",
    "ADDITION": r"\+",
    "SUBTRACTION": r"-",
    "MULTIPLICATION": r"\*",
    "DIVISION": r"/",
    "MODULUS": r"\%",
    "EXPONENTIATION": r"\^",

    # Parenthesis
    "RIGHT_PARENTHESIS": r"\)",
    "LEFT_PARENTHESIS": r"\(",

    # Data comparison
    "GREATER_THAN": r">",
    "LESS_THAN": r"<",
    "GREATER_THAN_OR_EQUAL_TO": r">=",
    "LESS_THAN_OR_EQUAL_TO": r"<=",
    "EQUAL_TO": r"==",
    "NOT_EQUAL_TO": r"<>|><",

    # Logical operators
    "AND": r"&&",
    "OR": r"\|\|",
    "NOT": r"!",

    # Data types
    "INTEGER": r"[0-9]+",
    "FLOAT": r"[0-9]+ \. [0-9]+",

    # Commands
    "PRINT": r"print",
    "IF": r"if",
    "ELSE": r"else",

    # Identifiers / Variables
    "IDENTIFIER": r"[a-zA-Z_][a-zA-Z0-9_]*",

    # Invalid tokens
    "INVALID": r".+"
}

```

## Objectives:
1. Understand what lexical analysis [1] is.
1. Get familiar with the inner workings of a lexer/scanner/tokenizer.
1. Implement a sample lexer and show how it works.


## Implementation and description:
### Lexer deffinition
The class takes in a string that's the file name and opens it in read-only mode. The content of the file is stored in a string named `content`. 
The tokens are defined in a dictionary named `tokens` and are used to create a regex that will be used to find the tokens in the content.
```py
class Lexer:
    # The Lexer class takes as constructor a string that's the file name
    # and stores the content of the file in a string named content.
    # The `tokens` property is a dictionary that sores the tokens defined in the Tokens.py file.
```

### Tokenizer
The tokenize function uses the regex to find all the tokens in the content and returns them as a list of tuples.
1. The regex is compiled and used to find all the tokens in the content.
1. The tokens are stored in a list named `tokens`.
1. For each token found, the token name and value are extracted.
1. If the token is a `WHITESPACE` or `NEWLINE` token, it is ignored because it is not needed for the parser.
1. If the token is an `INVALID` token, an exception is raised.
1. If the token is valid, it is added to the list of tokens.
1. The list of tokens is returned.

```py
def tokenize(self):
    # Use the regex to find all the tokens in the content.
    return tokens
```

## Results
### Inputs
#### demo.txt
This file contains valid tokens.
```txt
{
    x = 1 + 2
    y = 3 + 4
    z = x + y

    if (z > 10) {
        print(z)
    }
    else {
        print(x - y)
    }
}
```
##### Output:
When running this input through the tokenizer the result is the following output:
```txt
('BLOCK_START', '{')
('IDENTIFIER', 'x')
('ASSIGNMENT', '=')
('INTEGER', '1')
('ADDITION', '+')
('INTEGER', '2')
('IDENTIFIER', 'y')
('ASSIGNMENT', '=')
('INTEGER', '3')
('ADDITION', '+')
('INTEGER', '4')
('IDENTIFIER', 'z')
('ASSIGNMENT', '=')
('IDENTIFIER', 'x')
('ADDITION', '+')
('IDENTIFIER', 'y')
('IF', 'if')
('LEFT_PARENTHESIS', '(')
('IDENTIFIER', 'z')
('GREATER_THAN', '>')
('INTEGER', '10')
('RIGHT_PARENTHESIS', ')')
('BLOCK_START', '{')
('PRINT', 'print')
('LEFT_PARENTHESIS', '(')
('IDENTIFIER', 'z')
('RIGHT_PARENTHESIS', ')')
('BLOCK_END', '}')
('ELSE', 'else')
('BLOCK_START', '{')
('PRINT', 'print')
('LEFT_PARENTHESIS', '(')
('IDENTIFIER', 'x')
('SUBTRACTION', '-')
('IDENTIFIER', 'y')
('RIGHT_PARENTHESIS', ')')
('BLOCK_END', '}')
('BLOCK_END', '}')
```

#### illegal_demo.txt
This file contains invalid tokens.
```txt
{
    x = 3
]
```
##### Output:
When running this input through the tokenizer the result is the following output:
```txt
Exception: Invalid token ']'
```
