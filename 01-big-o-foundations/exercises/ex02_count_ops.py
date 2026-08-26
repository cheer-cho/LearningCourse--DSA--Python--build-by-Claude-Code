# Scenario: instead of reading about growth rates, you're going to
# SEE them. Each function below takes a `tick` callback and must call
# it exactly once per "unit of work" it does. The tests count ticks at
# several input sizes so you can watch O(n), O(n^2), and O(log n) grow
# at their own distinct rates.
# Concepts: linear scan, nested all-pairs scan, halving loop.
# Run: uv run pytest 01-big-o-foundations -k ex02

from collections.abc import Callable


def sum_all(nums: list[int], tick: Callable[[], None]) -> int:
    """Return the sum of `nums`, calling `tick()` exactly once per
    element visited.

    sum_all([1, 2, 3], tick) -> 6, and tick() was called 3 times.
    sum_all([], tick) -> 0, and tick() was called 0 times.

    Target complexity: O(n) time, O(1) extra space.
    """
    raise NotImplementedError


def all_pairs(items: list[int], tick: Callable[[], None]) -> list[tuple[int, int]]:
    """Return every ordered pair (a, b) with a, b drawn from `items`
    (including a paired with itself), calling `tick()` exactly once per
    pair produced.

    all_pairs([1, 2], tick) -> [(1, 1), (1, 2), (2, 1), (2, 2)], and
    tick() was called 4 times (2 * 2).

    Target complexity: O(n^2) time, O(n^2) space (the output itself
    has n^2 pairs).
    """
    raise NotImplementedError


def halve_down(n: int, tick: Callable[[], None]) -> int:
    """Repeatedly floor-divide `n` by 2 until it reaches 0, calling
    `tick()` once per value visited (including the starting value).
    Return the number of ticks.

    halve_down(8, tick) -> 4, and tick() was called 4 times
    (8 -> 4 -> 2 -> 1, then stop after visiting 1).
    halve_down(0, tick) -> 0, and tick() was called 0 times.

    Target complexity: O(log n) time, O(1) extra space.
    """
    raise NotImplementedError
