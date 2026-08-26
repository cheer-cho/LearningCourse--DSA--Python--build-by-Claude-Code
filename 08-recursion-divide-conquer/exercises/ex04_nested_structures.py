# Scenario: recursion on SHAPE, not numbers — arbitrarily nested lists of
# ints, e.g. [1, [2, 3], [4, [5, 6]]]. This mirrors walking parsed JSON and
# sets up tree recursion (module 11). Pattern: recurse when you see a
# list, use the value when you see an int.
# Run: uv run pytest 08-recursion-divide-conquer -k ex04

from typing import Any


def deep_sum(nested: list[Any]) -> int:
    """Sum every integer inside an arbitrarily nested list.

    Base case: an element that is an int contributes itself.
    Shrinking step: an element that is a list contributes deep_sum(that
    sublist) — the nesting gets one level shallower each recursive call.

    deep_sum([1, [2, 3], [4, [5, 6]]]) -> 21
    deep_sum([]) -> 0
    deep_sum([[[[7]]]]) -> 7
    deep_sum([1, -2, [3, -4]]) -> -2

    Target: O(total elements) time, O(max depth) space.
    """
    raise NotImplementedError


def max_depth_nested(nested: list[Any]) -> int:
    """Return the nesting depth of `nested`. A list with no nested lists
    inside (possibly empty) has depth 1. Each level of nesting adds 1.

    Base case: a list with no list elements -> 1.
    Shrinking step: 1 + the max depth among any nested list elements
    (non-list elements don't add depth).

    max_depth_nested([]) -> 1
    max_depth_nested([1, 2, 3]) -> 1
    max_depth_nested([1, [2, 3]]) -> 2
    max_depth_nested([1, [2, [3, [4]]]]) -> 4

    Target: O(total elements) time, O(max depth) space.
    """
    raise NotImplementedError


def flatten(nested: list[Any]) -> list[int]:
    """Flatten an arbitrarily nested list of ints into one flat list,
    preserving left-to-right order.

    Base case: an element that is an int goes straight into the result.
    Shrinking step: an element that is a list contributes flatten(that
    sublist), in order.

    flatten([1, [2, 3], [4, [5, 6]]]) -> [1, 2, 3, 4, 5, 6]
    flatten([]) -> []
    flatten([[1], [2, [3, 4]], 5]) -> [1, 2, 3, 4, 5]

    Target: O(total elements) time, O(total elements + max depth) space.
    """
    raise NotImplementedError
