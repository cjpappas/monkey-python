from unittest import TestCase

from monkey_interpreter.ast import (
    Let,
    Return,
    IntegerLiteral,
    ExpressionStatement,
    Expression,
    PrefixExpression,
)
from monkey_interpreter.lexer import Lexer
from monkey_interpreter.parser import Parser


class ParserTests(TestCase):
    def test_parse_program_let(self):
        tests: list[tuple[str, str]] = [
            ("let x = 5;", "x"),
            ("let y = 10;", "y"),
            ("let foobar = 838383;", "foobar"),
        ]

        for index, (source_input, identifier) in enumerate(tests):
            with self.subTest(i=index):
                lexer = Lexer(source_input)
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
                assert isinstance(statement, Let)
                self.assertEqual(statement.name.value, identifier)
                self.assertEqual(statement.name.token_literal(), identifier)

    def test_parse_program_let_error(self):
        tests: list[str] = ["let x 5;", "let = 10;", "let 838383;"]

        for index, source_input in enumerate(tests):
            with self.subTest(i=index):
                lexer = Lexer(source_input)
                parser = Parser(lexer)

                parser.parse_program()

                self.assertGreater(len(parser.errors), 0)

    def test_parse_program_return(self):
        tests: list[str] = ["return 5;", "return 10;", "return add(15);"]

        for index, source_input in enumerate(tests):
            with self.subTest(i=index):
                lexer = Lexer(source_input)
                parser = Parser(lexer)

                program = parser.parse_program()

                # Check statements
                self.assertIsNotNone(program)
                self.assertEqual(len(program.statements), 1)

                # Check for parser errors
                self.assertEqual(len(parser.errors), 0)

                # Check structure of statements
                statement = program.statements[0]

                self.assertEqual(statement.token_literal(), "return")
                assert isinstance(statement, Return)

    def test_parse_program_integer_literal(self):
        lexer = Lexer("5;")
        parser = Parser(lexer)

        program = parser.parse_program()

        # Check statements
        self.assertIsNotNone(program)
        self.assertEqual(len(program.statements), 1)

        statement = program.statements[0]
        assert isinstance(statement, ExpressionStatement)

        literal = statement.expression
        assert isinstance(literal, IntegerLiteral)
        self.assertEqual(literal.value, 5)
        self.assertEqual(literal.token_literal(), "5")

    def test_parse_program_prefix_expressions(self):
        tests: list[tuple[str, str, int]] = [("!5", "!", 5), ("-15", "-", 15)]

        for index, (source_input, operator, value) in enumerate(tests):
            with self.subTest(i=index):
                lexer = Lexer(source_input)
                parser = Parser(lexer)
                program = parser.parse_program()

                self.assertEqual(len(parser.errors), 0)
                self.assertEqual(len(program.statements), 1)

                statement = program.statements[0]
                assert isinstance(statement, ExpressionStatement)

                expression = statement.expression
                assert isinstance(expression, PrefixExpression)

                self.assertEqual(expression.operator, operator)
                test_integer_literal(expression, value)


def test_integer_literal(expression: Expression, value: int) -> bool:
    return (
        isinstance(expression, IntegerLiteral)
        and expression.value == value
        and expression.token_literal() == str(value)
    )
