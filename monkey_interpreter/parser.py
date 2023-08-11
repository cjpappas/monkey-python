from enum import Enum
from typing import Optional, Callable

from monkey_interpreter.ast import (
    Expression,
    ExpressionStatement,
    Identifier,
    IntegerLiteral,
    Let,
    Program,
    Return,
    Statement,
    PrefixExpression,
)
from monkey_interpreter.lexer import Lexer
from monkey_interpreter.token import Token, TokenType

PrefixParseFunction = Callable[[], Optional[Expression]]
InfixParseFunction = Callable[[Expression], Expression]

# fmt: off
class PRECEDENCE(Enum):
    LOWEST       = 1
    EQUALS       = 2
    LESS_GREATER = 3
    SUM          = 4
    PRODUCT      = 5
    PREFIX       = 6
    CALL         = 7
# fmt: on


class Parser:
    lexer: Lexer

    current_token: Optional[Token] = None
    peek_token: Optional[Token] = None

    errors: list[str] = []

    prefix_parse_functions: dict[TokenType, PrefixParseFunction] = {}
    infix_parse_functions: dict[TokenType, InfixParseFunction] = {}

    def __init__(self, lexer: Lexer) -> None:
        self.lexer = lexer

        # Read two tokens, so current_token and peek_token are both set
        # TODO: Better way to initialise this
        self.next_token()
        self.next_token()

        # Register parse functions
        self.regiser_prefix_function(TokenType.IDENT, self.parse_identifier)
        self.regiser_prefix_function(TokenType.INT, self.parse_integer_literal)
        self.regiser_prefix_function(TokenType.BANG, self.parse_prefix_expression)
        self.regiser_prefix_function(TokenType.MINUS, self.parse_prefix_expression)

    def regiser_prefix_function(
        self, token_type: TokenType, function: PrefixParseFunction
    ):
        self.prefix_parse_functions[token_type] = function

    def register_infix_function(
        self, token_type: TokenType, function: InfixParseFunction
    ):
        self.infix_parse_functions[token_type] = function

    def next_token(self):
        # TODO: Better way to initialise this
        self.current_token = self.peek_token
        self.peek_token = self.lexer.next_token()

    def parse_program(self) -> Program:
        program = Program([])

        if self.current_token is None:
            raise Exception("Can't parse program, current token is None")

        while self.current_token.tipe is not TokenType.EOF:
            statement = self.parse_statement()

            if statement is not None:
                program.statements.append(statement)

            self.next_token()

        return program

    def parse_statement(self) -> Optional[Statement]:
        if self.current_token is None:
            raise Exception("Can't parse statement, current token is None")

        match self.current_token.tipe:
            case TokenType.LET:
                return self.parse_let_statement()
            case TokenType.RETURN:
                return self.parse_return_statement()
            case _:
                return self.parse_expression_statement()

    def parse_let_statement(self) -> Optional[Let]:
        if self.current_token is None:
            raise Exception("Can't parse let statment, current token is None")

        statement_token = self.current_token

        if not self.expect_peek(TokenType.IDENT):
            return None

        statement_name = Identifier(self.current_token, self.current_token.literal)

        if not self.expect_peek(TokenType.ASSIGN):
            return None

        # TODO: Skipping expressions until we encounter a semicolo
        while not self.current_token_is(TokenType.SEMICOLON):
            self.next_token()

        return Let(statement_token, statement_name, "")

    def parse_return_statement(self) -> Optional[Return]:
        if self.current_token is None:
            raise Exception("Can't parse return statement, current token is None")

        statement = Return(self.current_token, "")

        # TODO: Skipping expressions until we encounter a semicolo
        while not self.current_token_is(TokenType.SEMICOLON):
            self.next_token()

        return statement

    def parse_expression_statement(self) -> ExpressionStatement:
        if self.current_token is None:
            raise Exception("Can't parse expression statement, current token is None")

        token = self.current_token
        expression = self.parse_expression(PRECEDENCE.LOWEST)

        if self.peek_token_is(TokenType.SEMICOLON):
            self.next_token()

        return ExpressionStatement(token, expression)

    def parse_expression(self, precedence: PRECEDENCE) -> Optional[Expression]:
        prefix_function = self.prefix_parse_functions.get(self.current_token.tipe)

        if prefix_function is None:
            self.errors.append(
                f"No prefix parse function for {self.current_token.tipe}"
            )
            return None

        left_expression = prefix_function()

        return left_expression

    def parse_identifier(self) -> Expression:
        return Identifier(self.current_token, self.current_token.literal)

    def parse_integer_literal(self) -> Optional[Expression]:
        try:
            value = int(self.current_token.literal)
        except ValueError:
            self.errors.append(
                f"Could not parse {self.current_token.literal} as an integer"
            )
            return None

        return IntegerLiteral(self.current_token, value)

    def parse_prefix_expression(self) -> Optional[Expression]:
        token = self.current_token
        operator = self.current_token.literal

        self.next_token()

        right = self.parse_expression(PRECEDENCE.PREFIX)

        return PrefixExpression(token, operator, right)

    def current_token_is(self, token_type: TokenType) -> bool:
        return self.current_token is not None and self.current_token.tipe is token_type

    def peek_token_is(self, token_type: TokenType) -> bool:
        return self.peek_token is not None and self.peek_token.tipe is token_type

    def peek_error(self, token_type: TokenType):
        if self.peek_token is None:
            raise Exception("Could not peek error, peek token is None")

        self.errors.append(
            f"Expected next token to be {token_type}, got {self.peek_token.tipe} instead"
        )

    def expect_peek(self, token_type: TokenType) -> bool:
        if self.peek_token_is(token_type):
            self.next_token()

            return True
        else:
            self.peek_error(token_type)
            return False
