# Checkpoint 05 — Traffic monitor
#
# A web service logs one request count per second. Build four sliding-
# window reports over that stream: a fixed-window worst case, a
# variable-window budget check, a variable-window threshold breach, and
# a fixed-window burst-pattern detector. Combines every flavor of window
# from this module.
# Run: uv run pytest 05-sliding-window -k checkpoint


def worst_minute(counts: list[int]) -> int:
    """Return the largest total request count over any 60 consecutive
    seconds in `counts`. `counts` has at least 60 entries; raise
    `ValueError` if not.

    Fixed-size window of 60 — add the entering second, drop the leaving
    one, never re-sum.

    worst_minute([1] * 60) -> 60
    worst_minute([1] * 30) -> raises ValueError  (fewer than 60 seconds of data)

    Target: O(n) time, O(1) space.
    """
    raise NotImplementedError


def longest_within_budget(counts: list[int], budget: int) -> int:
    """Return the length of the longest run of consecutive seconds whose
    total request count is <= `budget`. Every count in `counts` is
    >= 0. Return 0 if `counts` is empty, or if even the single cheapest
    second is already over `budget`.

    Variable-size window, shrink WHILE the running sum exceeds budget.

    longest_within_budget([2, 1, 1, 4, 1], 4) -> 3   ([2, 1, 1])
    longest_within_budget([5, 5, 5], 4) -> 0

    A negative `budget` can never be satisfied (every count is >= 0, so
    every non-empty window sums to >= 0): returns 0.

    Target: O(n) time, O(1) space.
    """
    raise NotImplementedError


def shortest_breach(counts: list[int], threshold: int) -> int:
    """Return the length of the shortest run of consecutive seconds
    whose total request count is >= `threshold`. Every count in
    `counts` is >= 0 and `threshold` is a positive integer. Return 0 if
    no run reaches `threshold`.

    Variable-size window, shrink WHILE the running sum still meets
    `threshold` (the inverted rule — shortest, not longest).

    shortest_breach([1, 2, 3, 4, 5], 11) -> 3   ([3, 4, 5])
    shortest_breach([1, 1, 1], 100) -> 0

    A `threshold` of 0 (or negative) is satisfied by any single second
    (every count is >= 0), so the shortest breach is 1 (0 only if
    `counts` is empty).

    Target: O(n) time, O(1) space.
    """
    raise NotImplementedError


def has_pattern_burst(counts: list[int], pattern: list[int]) -> bool:
    """Return True if any contiguous run of `counts` (of length
    `len(pattern)`) is a rearrangement of `pattern` — same multiset of
    values, any order (e.g. a known attack shape reordered in time).

    Fixed-size window + a `matched` counter, same shape as the
    permutation-in-string pattern but over small integers instead of
    characters.

    has_pattern_burst([1, 5, 2, 9, 2, 5], [5, 2, 9]) -> True   ([5, 2, 9] at index 1)
    has_pattern_burst([1, 2, 3], [4, 5]) -> False

    Target: O(n + m) time where n = len(counts), m = len(pattern).
    """
    raise NotImplementedError
