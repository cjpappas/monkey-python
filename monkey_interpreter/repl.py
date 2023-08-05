from monkey_interpreter.lexer import Lexer
from monkey_interpreter.token import TokenType


def start():
    while True:
        print(">> ", end="")
        scanned = input()

        lexer = Lexer(scanned)
        while token := lexer.next_token():
            print(token)

            if token.tipe == TokenType.EOF:
                break
