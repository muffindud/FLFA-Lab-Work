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
