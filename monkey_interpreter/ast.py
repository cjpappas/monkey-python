from abc import ABCMeta, abstractmethod
from dataclasses import dataclass, field

from monkey_interpreter.token import Token


class Node(metaclass=ABCMeta):
    @abstractmethod
    def token_literal(self) -> str:
        raise NotImplementedError


# TODO: Does this have to be a subclass of Node? It might be enough to check from issubclass or somethign?
class Statement(Node):
    # TODO: What should this method be?
    # @abstractmethod
    # def statement_node() -> None:
    # raise NotImplementedError
    pass


# TODO: Does this have to be a subclass of Node?
class Expression(Node):
    # TODO: What should this method be?
    # @abstractmethod
    # def expression_node() -> None:
    #     raise NotImplementedError
    pass


@dataclass
class Program(Node):
    statements: list[Statement] = field(default_factory=list)

    def token_literal(self) -> str:
        if len(self.statements) > 0:
            return self.statements[0].token_literal()
        else:
            return ""


@dataclass
class Identifier(Expression):
    token: Token
    value: str

    def token_literal(self) -> str:
        return self.token.literal


@dataclass
class LetStatement(Statement):
    token: Token
    name: Identifier
    value: Expression

    def token_literal(self) -> str:
        return self.token.literal
