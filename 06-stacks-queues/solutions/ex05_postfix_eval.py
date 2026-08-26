_OPERATORS = {"+", "-", "*", "/"}


def _truncate_divide(a: int, b: int) -> int:
    return int(a / b)  # int() on a float truncates toward zero


def eval_postfix(tokens: list[str]) -> int:
    # Pattern: stack of operands. Pushing numbers and, on an operator,
    # popping the two most recently pushed operands (right first, then
    # left) is exactly what a stack gives you for free — no need to
    # track precedence or parentheses like infix evaluation would.
    # Complexity: O(n) time, O(n) space.
    stack: list[int] = []
    for token in tokens:
        if token in _OPERATORS:
            right = stack.pop()
            left = stack.pop()
            if token == "+":
                stack.append(left + right)
            elif token == "-":
                stack.append(left - right)
            elif token == "*":
                stack.append(left * right)
            else:
                stack.append(_truncate_divide(left, right))
        else:
            stack.append(int(token))
    return stack[-1]
