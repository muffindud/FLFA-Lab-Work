# Parser and AST Building

### Course: Formal Languages and Finite Automata
### Author: Corneliu Catlabuga FAF-213

----

## Theory
A parser is a software component that analyzes the structure of a given input, such as a programming language code 
or a natural language sentence, and determines its grammatical structure. It breaks down the input into a 
hierarchical representation, typically using a formal grammar or set of rules. The parser's output is often used for 
further processing, such as interpreting or executing the input's meaning.

An Abstract Syntax Tree (AST) is a hierarchical representation of the structure of a program or code snippet, typically 
generated 
by a parser. 
The AST captures the syntax and semantics of the code in a more abstract and organized manner, making it easier for 
subsequent stages of compilation or interpretation to analyze and manipulate the code. It serves as an intermediate 
representation that facilitates various program analysis and transformation tasks.

## Objectives
1. Get familiar with parsing, what it is and how it can be programmed [1].
2. Get familiar with the concept of AST [2].
3. In addition to what has been done in the 3rd lab work do the following:
    1. In case you didn't have a type that denotes the possible types of tokens you need to:
        1. Have a type __*TokenType*__ (like an enum) that can be used in the lexical analysis to categorize the tokens.
        2. Please use regular expressions to identify the type of the token.
    2. Implement the necessary data structures for an AST that could be used for the text you have processed in the 3rd lab work.
    3. Implement a simple parser program that could extract the syntactic information from the input text.

## Implementation description
### `ParseTree.py`
For the AST a tree data structure is used. The constructor of the ParseTree class takes in the type of the node, the 
value of the node and a list of children. The value and children are optional and are set to None if not provided.
```py
class ParseTree:
    def __init__(self, n_type, value=None, children=None):
        self.type = n_type
        self.value = value
        self.children = children or []
```
When calling the class it returns a string representation of the tree in a hierarchical structure.
```py
def __str__(self, level=0):
    # print the tree with type and value
    if self.value is None:
        ret = "\t" * level + self.type + "\n"
    else:
        ret = "\t" * level + self.type + ": " + str(self.value) + "\n"
    for child in self.children:
        ret += child.__str__(level + 1)
    return ret

```

### `Parser.py`

When instantiating the object of the Parser class takes in the path to the file with the code.  The constructor 
automatically calls the tokenize function from the Lexer class and stores the tokens in a list named `tokens`.
```py
class Parser:
    def __init__(self, path):
        program = Lexer(path)
        self.tokens = program.tokenize()
        self.index = 0
        self.ast = None
```

The `parse` function is used to parse the tokens and build the AST starting from a `PROGRAM` token. In the current 
example the program starts from a block defined by `{}`. The `parse_block` function is used to parse the block.
```py
def parse(self):
    self.ast = ParseTree("PROGRAM")
    self.parse_block(self.ast)
```

Each parse function takes in a parent node and appends the parsed node to the parent node. The respective `parse` 
statement.

The `parse_block` function is used to parse the block of code. It is denotes by `{}`. The function checks if the
current token is a `BLOCK_START` token and if it is it appends it to the parent node and calls the `parse_statement`
function. After that it checks if the current token is a `BLOCK_END` token and if it is it appends it to the parent
node. If the current token is not a `BLOCK_END` token it raises an exception.
```py
def parse_block(self, parent_node):
    parse_node = ParseTree("BLOCK")
    if self.tokens[self.index][0] == "BLOCK_START":
        parse_node.children.append(ParseTree(self.tokens[self.index][0], self.tokens[self.index][1]))
        self.index += 1
        self.parse_statement(parse_node)
        if self.tokens[self.index][0] == "BLOCK_END":
            parse_node.children.append(ParseTree(self.tokens[self.index][0], self.tokens[self.index][1]))
            self.index += 1
        else:
            raise Exception("Expected '}'")
    parent_node.children.append(parse_node)
```

The `parse_statement` function is used to parse a statement. It checks from all currently supported statements and 
calls the respective parse function. If the current token is not a statement it appends the parsed node to the 
parent node and breaks the loop.

```py
def parse_statement(self, parent_node):
    parse_node = ParseTree("STATEMENT")
    while True:
        if self.tokens[self.index][0] == "IDENTIFIER":
            parse_node.children.append(ParseTree("ASSIGNMENT_STATEMENT"))
            self.parse_assignment(parse_node)
        elif self.tokens[self.index][0] == "PRINT":
            self.parse_print(parse_node)
        elif self.tokens[self.index][0] == "IF":
            self.parse_if(parse_node)
        else:
            parent_node.children.append(parse_node)
            break
```

The `parse_assignment` function is used to parse an assignment statement. It is called when the current token is an identifier.
It checks if the next token is an `ASSIGNMENT` token and if it is it appends it to the parent node and calls the 
`parse_expression` function. If the next token is not an `ASSIGNMENT` token it raises an exception.
```py 
def parse_assignment(self, parent_node):
    if self.tokens[self.index][0] == "IDENTIFIER":
        parent_node.children.append(ParseTree(self.tokens[self.index][0], self.tokens[self.index][1]))
        self.index += 1
        if self.tokens[self.index][0] == "ASSIGNMENT":
            parent_node.children.append(ParseTree(self.tokens[self.index][0], self.tokens[self.index][1]))
            self.index += 1
            self.parse_expression(parent_node)
        else:
            raise Exception("Expected '='")
    else:
        raise Exception("Expected identifier")
```

The `parse_expression` function is used to parse an expression. It is called when the current token is a number or an identifier.
```py 
def parse_expression(self, parent_node):
    parse_node = ParseTree("EXPRESSION")
    self.parse_term(parse_node)
    if self.tokens[self.index][0] in ["ADDITION", "SUBTRACTION"]:
        parse_node.children.append(ParseTree(self.tokens[self.index][0], self.tokens[self.index][1]))
        self.index += 1
        self.parse_expression(parse_node)
    parent_node.children.append(parse_node)
```

The `parse_term` function is used to parse a term. To keep the order of operations it calls the `parse_factor` function
first and then checks if the next token is a `MULTIPLICATION` or a `DIVISION` token for recursive calling. 
```py 
def parse_term(self, parent_node):
    self.parse_factor(parent_node)
    if self.tokens[self.index][0] in ["MULTIPLICATION", "DIVISION"]:
        parent_node.children.append(ParseTree(self.tokens[self.index][0], self.tokens[self.index][1]))
        self.index += 1
        self.parse_term(parent_node)
```

The `parse_factor` function is used to parse a factor. It checks if the current token is a `LEFT_PARENTHESIS` token
and if it is it appends it to the parent node and calls the `parse_expression` function. After that it checks if the
current token is a `RIGHT_PARENTHESIS` token and if it is it appends it to the parent node. If the current token is
not a `RIGHT_PARENTHESIS` token it raises an exception. If the current token is a number or an identifier it appends
it to the parent node. If the current token is not a number or an identifier it raises an exception.
```py 
def parse_factor(self, parent_node):
    if self.tokens[self.index][0] == "LEFT_PARENTHESIS":
        parent_node.children.append(ParseTree(self.tokens[self.index][0], self.tokens[self.index][1]))
        self.index += 1
        self.parse_expression(parent_node)
        if self.tokens[self.index][0] == "RIGHT_PARENTHESIS":
            parent_node.children.append(ParseTree(self.tokens[self.index][0], self.tokens[self.index][1]))
            self.index += 1
        else:
            raise Exception("Expected ')'")
    elif self.tokens[self.index][0] in ["INTEGER", "FLOAT"]:
        parent_node.children.append(ParseTree(self.tokens[self.index][0], self.tokens[self.index][1]))
        self.index += 1
    elif self.tokens[self.index][0] == "IDENTIFIER":
        parent_node.children.append(ParseTree(self.tokens[self.index][0], self.tokens[self.index][1]))
        self.index += 1
    else:
        raise Exception("Expected factor")
```

The `parse_comparison` function is used to parse a comparison. It calls the `parse_expression` function and then checks
if the current token is a comparison token. If it is it appends it to the parent node and calls the `parse_expression`
function again. If it is not a comparison token it raises an exception.
```py
def parse_comparison(self, parent_node):
    parse_node = ParseTree("COMPARISON")
    self.parse_expression(parse_node)
    if self.tokens[self.index][0] in ["EQUAL", "NOT_EQUAL", "LESS_THAN", "LESS_THAN_OR_EQUAL", "GREATER_THAN", "GREATER_THAN_OR_EQUAL"]:
        parse_node.children.append(ParseTree(self.tokens[self.index][0], self.tokens[self.index][1]))
        self.index += 1
        self.parse_expression(parse_node)
    parent_node.children.append(parse_node)
```

The `parse_if` function is used to parse an if statement. It checks if the current token is an `IF` token and if it is
it appends it to the parent node and calls the `parse_comparison` function. After that it checks if the current token
is a `LEFT_PARENTHESIS` token and if it is it appends it to the parent node. If the current token is not a
`LEFT_PARENTHESIS` token it raises an exception. After that it calls the `parse_comparison` function and then checks if
the current token is a `RIGHT_PARENTHESIS` token and if it is it appends it to the parent node. If the current token is
not a `RIGHT_PARENTHESIS` token it raises an exception. After that it calls the `parse_block` function. After that it
checks if the current token is an `ELSE` token and if it is it appends it to the parent node and calls the `parse_block`
function.
```py 
def parse_if(self, parent_node):
    parse_node = ParseTree("IF_STATEMENT")
    if self.tokens[self.index][0] == "IF":
        self.index += 1
        if self.tokens[self.index][0] == "LEFT_PARENTHESIS":
            parse_node.children.append(ParseTree(self.tokens[self.index][0], self.tokens[self.index][1]))
            self.index += 1
            self.parse_comparison(parse_node)
            if self.tokens[self.index][0] == "RIGHT_PARENTHESIS":
                parse_node.children.append(ParseTree(self.tokens[self.index][0], self.tokens[self.index][1]))
                self.index += 1
                self.parse_block(parse_node)
                if self.tokens[self.index][0] == "ELSE":
                    parse_node.children.append(ParseTree(self.tokens[self.index][0], self.tokens[self.index][1]))
                    self.index += 1
                    self.parse_block(parse_node)
            else:
                raise Exception("Expected ')'")
        else:
            raise Exception("Expected '('")
    else:
        raise Exception("Expected 'if'")
    parent_node.children.append(parse_node)
```

The `parse_print` function is used to parse a print statement. It checks if the current token is a `PRINT` token and if
it is it appends it to the parent node. After that it checks if the current token is a `LEFT_PARENTHESIS` token and if
it is it appends it to the parent node and calls the `parse_expression` function. After that it checks if the current
token is a `RIGHT_PARENTHESIS` token and if it is it appends it to the parent node. If the current token is not a
`RIGHT_PARENTHESIS` token it raises an exception. If the current token is not a `LEFT_PARENTHESIS` token it raises an
exception. If the current token is not a `PRINT` token it raises an exception.
```py 
def parse_print(self, parent_node):
    parse_node = ParseTree("PRINT_STATEMENT")
    if self.tokens[self.index][0] == "PRINT":
        self.index += 1
        if self.tokens[self.index][0] == "LEFT_PARENTHESIS":
            parse_node.children.append(ParseTree(self.tokens[self.index][0], self.tokens[self.index][1]))
            self.index += 1
            self.parse_expression(parse_node)
            if self.tokens[self.index][0] == "RIGHT_PARENTHESIS":
                parse_node.children.append(ParseTree(self.tokens[self.index][0], self.tokens[self.index][1]))
                self.index += 1
            else:
                raise Exception("Expected ')'")
        else:
            raise Exception("Expected '('")
    else:
        raise Exception("Expected 'print'")
    parent_node.children.append(parse_node)
```

The `show_ast` function is used to print the AST.
```py
def show_ast(self):
    print(self.ast)
```

## Testing and debugging
### `demo.txt`
The following code is used to test the parser.
```
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

When the `demo.txt` file is parsed the following AST is generated.
```
PROGRAM
	BLOCK
		BLOCK_START: {
		STATEMENT
			ASSIGNMENT_STATEMENT
			IDENTIFIER: x
			ASSIGNMENT: =
			EXPRESSION
				INTEGER: 1
				ADDITION: +
				EXPRESSION
					INTEGER: 2
			ASSIGNMENT_STATEMENT
			IDENTIFIER: y
			ASSIGNMENT: =
			EXPRESSION
				INTEGER: 3
				ADDITION: +
				EXPRESSION
					INTEGER: 4
			ASSIGNMENT_STATEMENT
			IDENTIFIER: z
			ASSIGNMENT: =
			EXPRESSION
				IDENTIFIER: x
				ADDITION: +
				EXPRESSION
					IDENTIFIER: y
			IF_STATEMENT
				LEFT_PARENTHESIS: (
				COMPARISON
					EXPRESSION
						IDENTIFIER: z
					GREATER_THAN: >
					EXPRESSION
						INTEGER: 10
				RIGHT_PARENTHESIS: )
				BLOCK
					BLOCK_START: {
					STATEMENT
						PRINT_STATEMENT
							LEFT_PARENTHESIS: (
							EXPRESSION
								IDENTIFIER: z
							RIGHT_PARENTHESIS: )
					BLOCK_END: }
				ELSE: else
				BLOCK
					BLOCK_START: {
					STATEMENT
						PRINT_STATEMENT
							LEFT_PARENTHESIS: (
							EXPRESSION
								IDENTIFIER: x
								SUBTRACTION: -
								EXPRESSION
									IDENTIFIER: y
							RIGHT_PARENTHESIS: )
					BLOCK_END: }
		BLOCK_END: }
```

## Conclusions
In conclusion, parsers and Abstract Syntax Trees (ASTs) play crucial roles in software development and language processing. Parsers analyze the structure of input code or language constructs and provide a foundation for further analysis and interpretation. ASTs, generated by parsers, represent the hierarchical and abstracted structure of code, enabling efficient program analysis, transformations, and optimizations. Together, parsers and ASTs form the backbone of many programming tools and compilers, empowering developers to build robust and intelligent software systems.

## References
[1] [Parsing Wiki](https://en.wikipedia.org/wiki/Parsing)

[2] [Abstract Syntax Tree Wiki](https://en.wikipedia.org/wiki/Abstract_syntax_tree)

[3] [GitHub Copilot](https://github.com/features/copilot) 
