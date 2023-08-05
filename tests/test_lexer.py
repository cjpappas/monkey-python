from unittest import TestCase

from monkey_interpreter.lexer import Lexer
from monkey_interpreter.token import Token, TokenType


class LexerTestCase(TestCase):
    def test_next_token_assign(self):
        lexer = Lexer("=")
        next_token = lexer.next_token()

        self.assertIsNotNone(next_token)
        self.assertEqual(
            next_token.tipe,  # pyright: ignore[reportOptionalMemberAccess]
            TokenType.ASSIGN,
        )
        self.assertEqual(
            next_token.literal,  # pyright: ignore[reportOptionalMemberAccess]
            "=",
        )

    def test_next_token_plus(self):
        lexer = Lexer("+")
        next_token = lexer.next_token()

        self.assertIsNotNone(next_token)
        self.assertEqual(
            next_token.tipe,  # pyright: ignore[reportOptionalMemberAccess]
            TokenType.PLUS,
        )
        self.assertEqual(
            next_token.literal,  # pyright: ignore[reportOptionalMemberAccess]
            "+",
        )

    def test_next_token_minus(self):
        lexer = Lexer("-")
        next_token = lexer.next_token()

        self.assertIsNotNone(next_token)
        self.assertEqual(
            next_token.tipe,  # pyright: ignore[reportOptionalMemberAccess]
            TokenType.MINUS,
        )
        self.assertEqual(
            next_token.literal,  # pyright: ignore[reportOptionalMemberAccess]
            "-",
        )

    def test_next_token_bang(self):
        lexer = Lexer("!")
        next_token = lexer.next_token()

        self.assertIsNotNone(next_token)
        self.assertEqual(
            next_token.tipe,  # pyright: ignore[reportOptionalMemberAccess]
            TokenType.BANG,
        )
        self.assertEqual(
            next_token.literal,  # pyright: ignore[reportOptionalMemberAccess]
            "!",
        )

    def test_next_token_asterisk(self):
        lexer = Lexer("*")
        next_token = lexer.next_token()

        self.assertIsNotNone(next_token)
        self.assertEqual(
            next_token.tipe,  # pyright: ignore[reportOptionalMemberAccess]
            TokenType.ASTERISK,
        )
        self.assertEqual(
            next_token.literal,  # pyright: ignore[reportOptionalMemberAccess]
            "*",
        )

    def test_next_token_slash(self):
        lexer = Lexer("/")
        next_token = lexer.next_token()

        self.assertIsNotNone(next_token)
        self.assertEqual(
            next_token.tipe,  # pyright: ignore[reportOptionalMemberAccess]
            TokenType.SLASH,
        )
        self.assertEqual(
            next_token.literal,  # pyright: ignore[reportOptionalMemberAccess]
            "/",
        )

    def test_next_token_lt(self):
        lexer = Lexer("<")
        next_token = lexer.next_token()

        self.assertIsNotNone(next_token)
        self.assertEqual(
            next_token.tipe,  # pyright: ignore[reportOptionalMemberAccess]
            TokenType.LT,
        )
        self.assertEqual(
            next_token.literal,  # pyright: ignore[reportOptionalMemberAccess]
            "<",
        )

    def test_next_token_gt(self):
        lexer = Lexer(">")
        next_token = lexer.next_token()

        self.assertIsNotNone(next_token)
        self.assertEqual(
            next_token.tipe,  # pyright: ignore[reportOptionalMemberAccess]
            TokenType.GT,
        )
        self.assertEqual(
            next_token.literal,  # pyright: ignore[reportOptionalMemberAccess]
            ">",
        )

    def test_next_token_eq(self):
        lexer = Lexer("==")
        next_token = lexer.next_token()

        self.assertIsNotNone(next_token)
        self.assertEqual(
            next_token.tipe,  # pyright: ignore[reportOptionalMemberAccess]
            TokenType.EQ,
        )
        self.assertEqual(
            next_token.literal,  # pyright: ignore[reportOptionalMemberAccess]
            "==",
        )

    def test_next_token_not_eq(self):
        lexer = Lexer("!=")
        next_token = lexer.next_token()

        self.assertIsNotNone(next_token)
        self.assertEqual(
            next_token.tipe,  # pyright: ignore[reportOptionalMemberAccess]
            TokenType.NOT_EQ,
        )
        self.assertEqual(
            next_token.literal,  # pyright: ignore[reportOptionalMemberAccess]
            "!=",
        )

    def test_next_token_comma(self):
        lexer = Lexer(",")
        next_token = lexer.next_token()

        self.assertIsNotNone(next_token)
        self.assertEqual(
            next_token.tipe,  # pyright: ignore[reportOptionalMemberAccess]
            TokenType.COMMA,
        )
        self.assertEqual(
            next_token.literal,  # pyright: ignore[reportOptionalMemberAccess]
            ",",
        )

    def test_next_token_semicolon(self):
        lexer = Lexer(";")
        next_token = lexer.next_token()

        self.assertIsNotNone(next_token)
        self.assertEqual(
            next_token.tipe,  # pyright: ignore[reportOptionalMemberAccess]
            TokenType.SEMICOLON,
        )
        self.assertEqual(
            next_token.literal,  # pyright: ignore[reportOptionalMemberAccess]
            ";",
        )

    def test_next_token_left_parenthesis(self):
        lexer = Lexer("(")
        next_token = lexer.next_token()

        self.assertIsNotNone(next_token)
        self.assertEqual(
            next_token.tipe,  # pyright: ignore[reportOptionalMemberAccess]
            TokenType.LPAREN,
        )
        self.assertEqual(
            next_token.literal,  # pyright: ignore[reportOptionalMemberAccess]
            "(",
        )

    def test_next_token_right_parenthesis(self):
        lexer = Lexer(")")
        next_token = lexer.next_token()

        self.assertIsNotNone(next_token)
        self.assertEqual(
            next_token.tipe,  # pyright: ignore[reportOptionalMemberAccess]
            TokenType.RPAREN,
        )
        self.assertEqual(
            next_token.literal,  # pyright: ignore[reportOptionalMemberAccess]
            ")",
        )

    def test_next_token_left_brace(self):
        lexer = Lexer("{")
        next_token = lexer.next_token()

        self.assertIsNotNone(next_token)
        self.assertEqual(
            next_token.tipe,  # pyright: ignore[reportOptionalMemberAccess]
            TokenType.LBRACE,
        )
        self.assertEqual(
            next_token.literal,  # pyright: ignore[reportOptionalMemberAccess]
            "{",
        )

    def test_next_token_right_brace(self):
        lexer = Lexer("}")
        next_token = lexer.next_token()

        self.assertIsNotNone(next_token)
        self.assertEqual(
            next_token.tipe,  # pyright: ignore[reportOptionalMemberAccess]
            TokenType.RBRACE,
        )
        self.assertEqual(
            next_token.literal,  # pyright: ignore[reportOptionalMemberAccess]
            "}",
        )

    def test_next_token_eof(self):
        lexer = Lexer("")
        next_token = lexer.next_token()

        self.assertIsNotNone(next_token)
        self.assertEqual(
            next_token.tipe,  # pyright: ignore[reportOptionalMemberAccess]
            TokenType.EOF,
        )
        self.assertEqual(
            next_token.literal,  # pyright: ignore[reportOptionalMemberAccess]
            "",
        )

    def test_next_token_illegal(self):
        lexer = Lexer("@")
        next_token = lexer.next_token()

        self.assertIsNotNone(next_token)
        self.assertEqual(
            next_token.tipe,  # pyright: ignore[reportOptionalMemberAccess]
            TokenType.ILLEGAL,
        )
        self.assertEqual(
            next_token.literal,  # pyright: ignore[reportOptionalMemberAccess]
            "@",
        )

    def test_next_token_int(self):
        lexer = Lexer("5")
        next_token = lexer.next_token()

        self.assertIsNotNone(next_token)
        self.assertEqual(
            next_token.tipe,  # pyright: ignore[reportOptionalMemberAccess]
            TokenType.INT,
        )
        self.assertEqual(
            next_token.literal,  # pyright: ignore[reportOptionalMemberAccess]
            "5",
        )

    def test_next_token_identifier(self):
        lexer = Lexer("add")
        next_token = lexer.next_token()

        self.assertIsNotNone(next_token)
        self.assertEqual(
            next_token.tipe,  # pyright: ignore[reportOptionalMemberAccess]
            TokenType.IDENT,
        )
        self.assertEqual(
            next_token.literal,  # pyright: ignore[reportOptionalMemberAccess]
            "add",
        )

    def test_next_token_keyword_function(self):
        lexer = Lexer("fn")
        next_token = lexer.next_token()

        self.assertIsNotNone(next_token)
        self.assertEqual(
            next_token.tipe,  # pyright: ignore[reportOptionalMemberAccess]
            TokenType.FUNCTION,
        )
        self.assertEqual(
            next_token.literal,  # pyright: ignore[reportOptionalMemberAccess]
            "fn",
        )

    def test_next_token_keyword_let(self):
        lexer = Lexer("let")
        next_token = lexer.next_token()

        self.assertIsNotNone(next_token)
        self.assertEqual(
            next_token.tipe,  # pyright: ignore[reportOptionalMemberAccess]
            TokenType.LET,
        )
        self.assertEqual(
            next_token.literal,  # pyright: ignore[reportOptionalMemberAccess]
            "let",
        )

    def test_next_token_keyword_true(self):
        lexer = Lexer("true")
        next_token = lexer.next_token()

        self.assertIsNotNone(next_token)
        self.assertEqual(
            next_token.tipe,  # pyright: ignore[reportOptionalMemberAccess]
            TokenType.TRUE,
        )
        self.assertEqual(
            next_token.literal,  # pyright: ignore[reportOptionalMemberAccess]
            "true",
        )

    def test_next_token_keyword_false(self):
        lexer = Lexer("false")
        next_token = lexer.next_token()

        self.assertIsNotNone(next_token)
        self.assertEqual(
            next_token.tipe,  # pyright: ignore[reportOptionalMemberAccess]
            TokenType.FALSE,
        )
        self.assertEqual(
            next_token.literal,  # pyright: ignore[reportOptionalMemberAccess]
            "false",
        )

    def test_next_token_keyword_if(self):
        lexer = Lexer("if")
        next_token = lexer.next_token()

        self.assertIsNotNone(next_token)
        self.assertEqual(
            next_token.tipe,  # pyright: ignore[reportOptionalMemberAccess]
            TokenType.IF,
        )
        self.assertEqual(
            next_token.literal,  # pyright: ignore[reportOptionalMemberAccess]
            "if",
        )

    def test_next_token_keyword_else(self):
        lexer = Lexer("else")
        next_token = lexer.next_token()

        self.assertIsNotNone(next_token)
        self.assertEqual(
            next_token.tipe,  # pyright: ignore[reportOptionalMemberAccess]
            TokenType.ELSE,
        )
        self.assertEqual(
            next_token.literal,  # pyright: ignore[reportOptionalMemberAccess]
            "else",
        )

    def test_next_token_keyword_return(self):
        lexer = Lexer("return")
        next_token = lexer.next_token()

        self.assertIsNotNone(next_token)
        self.assertEqual(
            next_token.tipe,  # pyright: ignore[reportOptionalMemberAccess]
            TokenType.RETURN,
        )
        self.assertEqual(
            next_token.literal,  # pyright: ignore[reportOptionalMemberAccess]
            "return",
        )

    def test_next_token_program(self):
        lexer = Lexer(
            """let five = 5; let ten = 10;

let add = fn(x, y) {

x + y; };

let result = add(five, ten);
!-/*5;
5 < 10 > 5;

if (5 < 10) { 
    return true;
} else {
    return false;
}

10 == 10;
10 != 9;
"""
        )

        tests: list[Token] = [
            Token(TokenType.LET, "let"),
            Token(TokenType.IDENT, "five"),
            Token(TokenType.ASSIGN, "="),
            Token(TokenType.INT, "5"),
            Token(TokenType.SEMICOLON, ";"),
            Token(TokenType.LET, "let"),
            Token(TokenType.IDENT, "ten"),
            Token(TokenType.ASSIGN, "="),
            Token(TokenType.INT, "10"),
            Token(TokenType.SEMICOLON, ";"),
            Token(TokenType.LET, "let"),
            Token(TokenType.IDENT, "add"),
            Token(TokenType.ASSIGN, "="),
            Token(TokenType.FUNCTION, "fn"),
            Token(TokenType.LPAREN, "("),
            Token(TokenType.IDENT, "x"),
            Token(TokenType.COMMA, ","),
            Token(TokenType.IDENT, "y"),
            Token(TokenType.RPAREN, ")"),
            Token(TokenType.LBRACE, "{"),
            Token(TokenType.IDENT, "x"),
            Token(TokenType.PLUS, "+"),
            Token(TokenType.IDENT, "y"),
            Token(TokenType.SEMICOLON, ";"),
            Token(TokenType.RBRACE, "}"),
            Token(TokenType.SEMICOLON, ";"),
            Token(TokenType.LET, "let"),
            Token(TokenType.IDENT, "result"),
            Token(TokenType.ASSIGN, "="),
            Token(TokenType.IDENT, "add"),
            Token(TokenType.LPAREN, "("),
            Token(TokenType.IDENT, "five"),
            Token(TokenType.COMMA, ","),
            Token(TokenType.IDENT, "ten"),
            Token(TokenType.RPAREN, ")"),
            Token(TokenType.SEMICOLON, ";"),
            Token(TokenType.BANG, "!"),
            Token(TokenType.MINUS, "-"),
            Token(TokenType.SLASH, "/"),
            Token(TokenType.ASTERISK, "*"),
            Token(TokenType.INT, "5"),
            Token(TokenType.SEMICOLON, ";"),
            Token(TokenType.INT, "5"),
            Token(TokenType.LT, "<"),
            Token(TokenType.INT, "10"),
            Token(TokenType.GT, ">"),
            Token(TokenType.INT, "5"),
            Token(TokenType.SEMICOLON, ";"),
            Token(TokenType.IF, "if"),
            Token(TokenType.LPAREN, "("),
            Token(TokenType.INT, "5"),
            Token(TokenType.LT, "<"),
            Token(TokenType.INT, "10"),
            Token(TokenType.RPAREN, ")"),
            Token(TokenType.LBRACE, "{"),
            Token(TokenType.RETURN, "return"),
            Token(TokenType.TRUE, "true"),
            Token(TokenType.SEMICOLON, ";"),
            Token(TokenType.RBRACE, "}"),
            Token(TokenType.ELSE, "else"),
            Token(TokenType.LBRACE, "{"),
            Token(TokenType.RETURN, "return"),
            Token(TokenType.FALSE, "false"),
            Token(TokenType.SEMICOLON, ";"),
            Token(TokenType.RBRACE, "}"),
            Token(TokenType.INT, "10"),
            Token(TokenType.EQ, "=="),
            Token(TokenType.INT, "10"),
            Token(TokenType.SEMICOLON, ";"),
            Token(TokenType.INT, "10"),
            Token(TokenType.NOT_EQ, "!="),
            Token(TokenType.INT, "9"),
            Token(TokenType.SEMICOLON, ";"),
            Token(TokenType.EOF, ""),
        ]

        for index, token in enumerate(tests):
            with self.subTest(i=index):
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
