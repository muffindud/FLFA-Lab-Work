from src.Lexer import Lexer
from src.ParseTree import ParseTree


class Parser:
    def __init__(self, path):
        program = Lexer(path)
        self.tokens = program.tokenize()
        self.index = 0
        self.ast = None

    def parse(self):
        self.ast = ParseTree("PROGRAM")
        self.parse_block(self.ast)

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

    def parse_expression(self, parent_node):
        parse_node = ParseTree("EXPRESSION")
        self.parse_term(parse_node)
        if self.tokens[self.index][0] in ["ADDITION", "SUBTRACTION"]:
            parse_node.children.append(ParseTree(self.tokens[self.index][0], self.tokens[self.index][1]))
            self.index += 1
            self.parse_expression(parse_node)
        parent_node.children.append(parse_node)

    def parse_term(self, parent_node):
        self.parse_factor(parent_node)
        if self.tokens[self.index][0] in ["MULTIPLICATION", "DIVISION"]:
            parent_node.children.append(ParseTree(self.tokens[self.index][0], self.tokens[self.index][1]))
            self.index += 1
            self.parse_term(parent_node)

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

    def parse_comparison(self, parent_node):
        parse_node = ParseTree("COMPARISON")
        self.parse_expression(parse_node)
        if self.tokens[self.index][0] in ["EQUAL", "NOT_EQUAL", "LESS_THAN", "LESS_THAN_OR_EQUAL", "GREATER_THAN", "GREATER_THAN_OR_EQUAL"]:
            parse_node.children.append(ParseTree(self.tokens[self.index][0], self.tokens[self.index][1]))
            self.index += 1
            self.parse_expression(parse_node)
        parent_node.children.append(parse_node)

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
        
    def show_ast(self):
        print(self.ast)
