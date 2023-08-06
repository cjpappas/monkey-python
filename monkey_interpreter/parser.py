from typing import Optional

from monkey_interpreter.ast import Identifier, LetStatement, Program, Statement
from monkey_interpreter.lexer import Lexer
from monkey_interpreter.token import Token, TokenType


class Parser:
    lexer: Lexer

    current_token: Token
    peek_token: Token

    def __init__(self, lexer: Lexer) -> None:
        self.lexer = lexer

        # Read two tokens, so current_token and peek_token are both set
        self.next_token()
        self.next_token()

    def next_token(self):
        self.current_token = self.peek_token
        self.peek_token = self.lexer.next_token()

    def parse_program(self) -> Program:
        program = Program([])

        while self.current_token.tipe is not TokenType.EOF:
            statement = self.parse_statement()

            if statement is not None:
                program.statements.append(statement)

            self.next_token()

        return program

    def parse_statement(self) -> Optional[Statement]:
        match self.current_token.tipe:
            case TokenType.LET:
                return self.parse_let_statement()
            case _:
                return None

    def parse_let_statement(self) -> Optional[LetStatement]:
        statement_token = self.current_token

        if not self.expect_peek(TokenType.IDENT):
            return None

        statement_name = Identifier(self.current_token, self.current_token.literal)

        if not self.expect_peek(TokenType.ASSIGN):
            return None

        # TODO: Skipping expressions until we encounter a semicolo
        while not self.current_token_is(TokenType.SEMICOLON):
            self.next_token()

        return LetStatement(statement_token, statement_name, "")

    def current_token_is(self, token_type: TokenType) -> bool:
        return self.current_token.tipe is token_type

    def peek_token_is(self, token_type: TokenType) -> bool:
        return self.peek_token.tipe is token_type

    def expect_peek(self, token_type: TokenType) -> bool:
        if self.peek_token_is(token_type):
            self.next_token()

            return True

        return False
