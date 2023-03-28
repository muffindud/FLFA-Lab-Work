# Lexer and Scaner
#### Course: Formal Languages and Finite Automata
#### Author: Corneliu Catlabuga FAF-213

## Theory:
The laboratory work is implemented on the following token dictionary:
##### NOTES: 
1. The order in which tokens are deffined is important.

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
    file = None
    content = ""
    tokens = "|".join(f"(?P<{name}>{regex})" for name, regex in Tokens.tokens.items())

    def __init__(self, file_name):
        self.file = open(file_name, "r")
        self.content = self.file.read()

    def tokenize(self)
        # Tokenize the content
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
    matches = re.finditer(self.tokens, self.content)

    tokens = []
    for match in matches:
        token_name = match.lastgroup
        token_value = match.group(token_name)

        if token_name in ["WHITESPACE", "NEWLINE"]:
            continue

        if token_name == "INVALID":
            raise Exception(f"Invalid token '{token_value}'")

        tokens.append((token_name, token_value))

    return tokens
```