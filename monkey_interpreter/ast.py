from abc import ABCMeta, abstractmethod
from dataclasses import dataclass

from monkey_interpreter.token import Token


class Node(metaclass=ABCMeta):
    @abstractmethod
    def token_literal(self) -> str:
        raise NotImplementedError


class Statement(Node):
    pass


class Expression(Node):
    pass


class Program(Node):
    statements: list[Statement]

    def __init__(self, statements: list[Statement]) -> None:
        self.statements = statements

    def __str__(self) -> str:
        return "".join(map(lambda s: str(s), self.statements))

    def token_literal(self) -> str:
        if len(self.statements) > 0:
            return self.statements[0].token_literal()
        else:
            return ""


@dataclass
class Identifier(Expression):
    token: Token
    value: str

    def __str__(self) -> str:
        return self.value

    def token_literal(self) -> str:
        return self.token.literal


@dataclass
class Let(Statement):
    token: Token
    name: Identifier
    value: Expression

    def __str__(self) -> str:
        return f"{self.token_literal()} {self.name} = {self.value};"

    def token_literal(self) -> str:
        return self.token.literal


@dataclass
class Return(Statement):
    token: Token
    return_value: Expression

    def __str__(self) -> str:
        return f"{self.token_literal()} {self.return_value};"

    def token_literal(self) -> str:
        return self.token.literal


@dataclass
class ExpressionStatement(Statement):
    token: Token
    expression: Expression

    def __str__(self) -> str:
        return str(self.expression)

    def token_literal(self) -> str:
        return self.token.literal


@dataclass
class IntegerLiteral(Expression):
    token: Token
    value: int

    def __str__(self) -> str:
        return self.token.literal

    def token_literal(self) -> str:
        return self.token.literal


@dataclass
class PrefixExpression(Expression):
    token: Token
    operator: str
    right: Expression

    def __str__(self) -> str:
        return f"({self.operator}{str(self.right)})"

    def token_literal(self) -> str:
        return self.token.literal
