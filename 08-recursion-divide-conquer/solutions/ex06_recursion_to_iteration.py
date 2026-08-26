from typing import Any


def deep_sum_iterative(nested: list[Any]) -> int:
    # Pattern: recursion -> iteration via an explicit stack. Every list we
    # meet gets pushed onto our own `stack` list instead of being recursed
    # into; every int gets added directly. Order doesn't matter for a sum,
    # so no need to reverse anything before pushing.
    # Time: O(total elements), Space: O(max depth) for the stack.
    total = 0
    stack: list[Any] = [nested]
    while stack:
        current = stack.pop()
        if isinstance(current, list):
            stack.extend(current)
        else:
            total += current
    return total


def countdown_iterative(n: int) -> list[int]:
    # Pattern: recursion -> iteration via an explicit stack. Each stack
    # entry stands in for one pending recursive call: popping n and (if
    # positive) recording it, then pushing n - 1, mirrors "record n, then
    # recurse on n - 1" without growing the call stack.
    # Time: O(n), Space: O(n) for the stack + result.
    result: list[int] = []
    stack = [n]
    while stack:
        current = stack.pop()
        if current <= 0:
            continue
        result.append(current)
        stack.append(current - 1)
    return result
