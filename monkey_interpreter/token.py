from dataclasses import dataclass

# NOTE: Can we use something more verbose like an enum?
TokenType = str

# fmt:off
ILLEGAL   = "ILLEGAL"
EOF       = "EOF"

# Indentifiers & literals
IDENT     = "IDENT"  # add, foobar, x, y, ...
INT       = "INT" # 42069

    # Operators
ASSIGN    = "="
PLUS      = "+"

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
# fmt: on


@dataclass
class Token:
    tipe: TokenType
    literal: str
