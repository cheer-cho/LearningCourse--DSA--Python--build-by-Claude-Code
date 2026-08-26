# Scenario: merging pre-sorted shard results from a search index, then
# generalizing to sorting a shard from scratch.
# Concepts: divide & conquer, the O(n) merge step, stability.
# Run: uv run pytest 09-sorting -k ex02

from collections.abc import Callable
from typing import Any


def merge_sort[T](nums: list[T], key: Callable[[T], Any] | None = None) -> list[T]:
    """Return a NEW list containing `nums` sorted ascending. Does not
    modify `nums`.

    `key`, if given, extracts the value to compare from each element
    (like the builtin `sorted(..., key=...)`) — this lets the same
    function sort plain numbers or records. Must be STABLE: elements
    with equal keys keep their original relative order.

    merge_sort([5, 2, 4, 1]) -> [1, 2, 4, 5]
    merge_sort([("b", 1), ("a", 2)], key=lambda pair: pair[0]) -> [("a", 2), ("b", 1)]
    merge_sort([]) -> []

    Target complexity: O(n log n) time, O(n) space.
    """
    raise NotImplementedError
