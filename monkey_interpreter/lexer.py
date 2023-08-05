from typing import Optional

from monkey_interpreter.token import Token, TokenType, lookup_identifier


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

        self.skip_whitespace()

        match self.current_char:
            case None:
                next_token = Token(TokenType.EOF, "")
            case "=":
                if self.peek_char() == "=":
                    prev_char = self.current_char
                    self.read_char()
                    literal = prev_char + self.current_char

                    next_token = Token(TokenType.EQ, literal)
                else:
                    next_token = Token(TokenType.ASSIGN, self.current_char)
            case "+":
                next_token = Token(TokenType.PLUS, self.current_char)
            case "-":
                next_token = Token(TokenType.MINUS, self.current_char)
            case "!":
                if self.peek_char() == "=":
                    prev_char = self.current_char
                    self.read_char()
                    literal = prev_char + self.current_char

                    next_token = Token(TokenType.NOT_EQ, literal)
                else:
                    next_token = Token(TokenType.BANG, self.current_char)
            case "/":
                next_token = Token(TokenType.SLASH, self.current_char)
            case "*":
                next_token = Token(TokenType.ASTERISK, self.current_char)
            case "<":
                next_token = Token(TokenType.LT, self.current_char)
            case ">":
                next_token = Token(TokenType.GT, self.current_char)
            case ",":
                next_token = Token(TokenType.COMMA, self.current_char)
            case ";":
                next_token = Token(TokenType.SEMICOLON, self.current_char)
            case "(":
                next_token = Token(TokenType.LPAREN, self.current_char)
            case ")":
                next_token = Token(TokenType.RPAREN, self.current_char)
            case "{":
                next_token = Token(TokenType.LBRACE, self.current_char)
            case "}":
                next_token = Token(TokenType.RBRACE, self.current_char)
            case _:
                if self.is_letter(self.current_char):
                    literal = self.read_identifier()
                    tipe = lookup_identifier(literal)

                    # Exit early to avoid calling read_char()
                    return Token(tipe, literal)
                elif self.is_digit(self.current_char):
                    tipe = TokenType.INT
                    literal = self.read_number()

                    # Exit early to avoid calling read_char()
                    return Token(tipe, literal)
                else:
                    next_token = Token(TokenType.ILLEGAL, self.current_char)

        self.read_char()

        return next_token

    def peek_char(self) -> Optional[str]:
        if self.read_position >= len(self.source_input):
            return None

        return self.source_input[self.read_position]

    def read_char(self):
        if self.read_position >= len(self.source_input):
            self.current_char = None
        else:
            self.current_char = self.source_input[self.read_position]

        self.position = self.read_position
        self.read_position += 1

    def read_identifier(self) -> str:
        position = self.position

        while self.is_letter(self.current_char):
            self.read_char()

        return self.source_input[position : self.position]

    def read_number(self):
        position = self.position

        while self.is_digit(self.current_char):
            self.read_char()

        return self.source_input[position : self.position]

    def is_letter(self, char: Optional[str]) -> bool:
        return char is not None and (char.isalpha() or (char == "_"))

    def is_digit(self, char: Optional[str]) -> bool:
        return char is not None and char.isdigit()

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.read_char()
