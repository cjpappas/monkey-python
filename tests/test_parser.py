from unittest import TestCase

from monkey_interpreter.ast import LetStatement
from monkey_interpreter.lexer import Lexer
from monkey_interpreter.parser import Parser


class ParserTests(TestCase):
    def test_parse_program_let(self):
        lexer = Lexer("let x = 5;")
        parser = Parser(lexer)

        program = parser.parse_program()

        # Check statements
        self.assertIsNotNone(program)
        self.assertEqual(len(program.statements), 1)

        # Check for parser errors
        self.assertEqual(len(parser.errors), 0)

        # Check structure of statements
        statement = program.statements[0]

        self.assertEqual(statement.token_literal(), "let")
        assert isinstance(statement, LetStatement)
        self.assertEqual(statement.name.value, "x")
        self.assertEqual(statement.name.token_literal(), "x")

    def test_parse_program_let_error(self):
        lexer = Lexer("let x 5;")
        parser = Parser(lexer)

        self.assertGreater(len(parser.errors), 0)
