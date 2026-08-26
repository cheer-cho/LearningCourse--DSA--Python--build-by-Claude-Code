# Scenario: a stack-based calculator evaluates Reverse Polish Notation
# straight from a token stream — no parentheses, no precedence rules,
# just a stack. Concepts: using a stack to evaluate postfix expressions.
# Run: uv run pytest 06-stacks-queues -k ex05


def eval_postfix(tokens: list[str]) -> int:
    """Evaluate a postfix (Reverse Polish Notation) expression.

    `tokens` is a list of integer literals and operators from
    '+ - * /', e.g. ["3", "4", "+", "2", "*"] means (3 + 4) * 2.
    Division truncates TOWARD ZERO, not floor: Python's `//` floors
    -7 // 2 to -4, but here -7 / 2 truncates to -3 (matches C/Java
    integer division).

    eval_postfix(["3", "4", "+", "2", "*"]) -> 14
    eval_postfix(["10", "3", "/"]) -> 3
    eval_postfix(["-7", "2", "/"]) -> -3
    eval_postfix(["5"]) -> 5

    Division by zero raises ZeroDivisionError. `tokens` is always a
    valid, fully-formed postfix expression (exactly enough operands for
    every operator, one value left at the end).

    Target complexity: O(n) time, O(n) space.
    """
    raise NotImplementedError
