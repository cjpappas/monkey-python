from enum import Enum

# NOTE: Can we use something more verbose like an enum?
TokenType = str

# fmt:off
class TOKEN(Enum):
    ILLEGAL = "ILLEGAL"
    EOF     = "EOF"

    # Indentifiers & literals
    IDENT   = "IDENT"  # add, foobar, x, y, ...
    INT     = "INT"
# fmt: on


# NOTE: Can we use a tuple instead of a class?
class Token:
    def __init__(self, tipe: TokenType, literal: str) -> None:
        self.tipe = tipe
        self.literal = literal
