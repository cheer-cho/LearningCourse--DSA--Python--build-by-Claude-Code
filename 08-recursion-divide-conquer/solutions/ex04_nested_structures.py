from typing import Any


def deep_sum(nested: list[Any]) -> int:
    # Pattern: recursion on shape — branch on type instead of shrinking a
    # number. Each list element either IS the base case (int) or shrinks
    # the problem by one level of nesting (list).
    # Time: O(total elements), Space: O(max depth).
    total = 0
    for item in nested:
        if isinstance(item, list):
            total += deep_sum(item)
        else:
            total += item
    return total


def max_depth_nested(nested: list[Any]) -> int:
    # Pattern: recursion on shape, tracking the deepest branch seen.
    # Time: O(total elements), Space: O(max depth).
    deepest_child = 0
    for item in nested:
        if isinstance(item, list):
            deepest_child = max(deepest_child, max_depth_nested(item))
    return 1 + deepest_child


def flatten(nested: list[Any]) -> list[int]:
    # Pattern: recursion on shape, accumulating results left to right.
    # Time: O(total elements), Space: O(total elements + max depth).
    result: list[int] = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result
