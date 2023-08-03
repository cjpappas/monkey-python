from unittest import TestCase

from monkey_interpreter.lexer import Lexer
from monkey_interpreter.token import Token
import monkey_interpreter.token as TOKEN


class LexerTests(TestCase):
    def test_next_token(self):
        lexer = Lexer("=+(){},;")

        tests: list[Token] = [
            Token(TOKEN.ASSIGN, "="),
            Token(TOKEN.PLUS, "+"),
            Token(TOKEN.LPAREN, "("),
            Token(TOKEN.RPAREN, ")"),
            Token(TOKEN.LBRACE, "{"),
            Token(TOKEN.RBRACE, "}"),
            Token(TOKEN.COMMA, ","),
            Token(TOKEN.SEMICOLON, ";"),
            Token(TOKEN.EOF, ""),
        ]

        for token in tests:
            next_token = lexer.next_token()

            self.assertIsNotNone(next_token)
            self.assertEqual(
                next_token.tipe,  # pyright: ignore[reportOptionalMemberAccess]
                token.tipe,
            )
            self.assertEqual(
                next_token.literal,  # pyright: ignore[reportOptionalMemberAccess]
                token.literal,
            )
