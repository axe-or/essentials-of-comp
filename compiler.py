from dataclasses import dataclass
from typing import Self

TK_IDENTIFIER = '#Identifier'
TK_STRING     = '#String'
TK_INTEGER    = '#Integer'
TK_REAL       = '#Real'
TK_BOOL       = '#Bool'
TK_NIL        = '#Nil'

@dataclass
class Token:
    """A Token is a discrete object that is formed by matching certain source code patterns.
    
    Attributes:
        kind: The type of token, for operator tokens such as `.`, `+`, `<=`, it's simply the string representing that operator. Otherwhise, it will be one of the TK_* constants.
        lexeme: The literal string for the token, as found in the source code.
        value: The primitive value the token represents, only applies to tokens representing literals
    """
    kind : str
    lexeme : str
    value : int | float | str | bool | None = None

# @dataclass
# class Lexer:
    # source : str
    # current = 0
    # previous = 0

    # def advance() -> str | None:
        # pass

    # def next() -> Token:
        # pass

class Expression:
    """Base class for all expressions."""

@dataclass
class Primary(Expression):
    """A primary expression is one whose value does not rely on any other expression."""
    value : int | float | str | bool | None = None

@dataclass
class Unary(Expression):
    """Unary expressions apply an operator token to a single sub-expression"""
    operator : Token
    operand : Expression

@dataclass
class Binary(Expression):
    """Binary expressions reduce 2 expressions into one using one operator token."""
    operator : Token
    left : Expression
    right : Expression

@dataclass
class Call(Expression):
    """Call-like expression.
    
    The left side of a call expression is usually a function, but can be any expression that
    resolves to a callable object.
    
    The argument list may be empty but *not* null.
    """
    func : Expression
    args : list[Expression]

class Statement:
    """Base class for statements.
    
    Statements can represent control flow and don't necessarily evaluate to a final value.
    """

@dataclass
class Scope(Statement):
    """Scope is a statement sequence with its own environment.
    
    Scopes are the basic building blocks of structured control flow.
    """
    statements : list[Statement]

@dataclass
class If(Statement):
    """If statement represents a structured branch.
    
    Attributes:
        condition: The condition expression, must be a boolean.
        body: Statements to executed if condition is true
        else_body: Can be null (no else), a scope (simple else) or another if (else if). Acts similar to a linked list when chaining multiple if else statements.
    """
    condition : Expression
    body : Scope
    else_body : Scope | Self | None

@dataclass
class For(Statement):
    """For statements are loops.
    
    Attributes:
        condition: The condition that gets checked before every iteration. If empty, it's an infinite loop.
        body: Statements to execute while condition is true.
    """
    condition : Expression
    body : Scope

@dataclass
class VarDeclaration(Statement):
    pass

@dataclass
class Assignment(Statement):
    left : list[Expression]
    right : list[Expression]

@dataclass
class ExprStatement(Statement):
    expression : Expression

