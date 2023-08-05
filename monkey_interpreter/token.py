from dataclasses import dataclass
from enum import Enum

# fmt:off
class TokenType(Enum):
    ILLEGAL   = "ILLEGAL"
    EOF       = "EOF"

    # Indentifiers & literals
    IDENT     = "IDENT"  # add, foobar, x, y, ...
    INT       = "INT" # 42069

    # Operators
    ASSIGN    = "="
    PLUS      = "+"
    MINUS     = "-"
    BANG      = "!"
    ASTERISK  = "*"
    SLASH     = "/"
    LT        = "<"
    GT        = ">"
    EQ        = "=="
    NOT_EQ    = "!="

    # Delimiters
    COMMA     = ","
    SEMICOLON = ";"
    LPAREN    = "("
    RPAREN    = ")"
    LBRACE    = "{"
    RBRACE    = "}"

    # Keywords
    FUNCTION  = "FUNCTION"
    LET       = "LET"
    TRUE      = "TRUE"
    FALSE     = "FALSE"
    IF        = "IF"
    ELSE      = "ELSE"
    RETURN    = "RETURN"


KEYWORDS = {
    "fn":     TokenType.FUNCTION,
    "let":    TokenType.LET,
    "true":   TokenType.TRUE,
    "false":  TokenType.FALSE,
    "if":     TokenType.IF,
    "else":   TokenType.ELSE,
    "return": TokenType.RETURN
}
# fmt: on


@dataclass
class Token:
    tipe: TokenType
    literal: str


def lookup_identifier(identifier: str) -> TokenType:
    return KEYWORDS.get(identifier, TokenType.IDENT)
