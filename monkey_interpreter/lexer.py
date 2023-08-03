from typing import Optional

import monkey_interpreter.token as token
from monkey_interpreter.token import Token


class Lexer:
    source_input: str
    position: int = 0
    read_position: int = 0
    current_char: Optional[str]

    def __init__(self, source_input: str) -> None:
        self.source_input = source_input
        self.read_char()

    def next_token(self) -> Optional[Token]:
        next_token: Optional[Token] = None

        match self.current_char:
            case None:
                next_token = Token(token.EOF, "")
            case "=":
                next_token = Token(token.ASSIGN, self.current_char)
            case "+":
                next_token = Token(token.PLUS, self.current_char)
            case ",":
                next_token = Token(token.COMMA, self.current_char)
            case ";":
                next_token = Token(token.SEMICOLON, self.current_char)
            case "(":
                next_token = Token(token.LPAREN, self.current_char)
            case ")":
                next_token = Token(token.RPAREN, self.current_char)
            case "{":
                next_token = Token(token.LBRACE, self.current_char)
            case "}":
                next_token = Token(token.RBRACE, self.current_char)

        self.read_char()

        return next_token

    def read_char(self):
        if self.read_position >= len(self.source_input):
            self.current_char = None
        else:
            self.current_char = self.source_input[self.read_position]

        self.position = self.read_position
        self.read_position += 1
