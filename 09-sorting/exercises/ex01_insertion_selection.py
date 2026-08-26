# Scenario: a leaderboard service ingests small/nearly-sorted batches and
# needs the two simplest sorts as a baseline before the fancier ones.
# Concepts: selection sort, insertion sort, adaptivity, O(n^2) baselines.
# Run: uv run pytest 09-sorting -k ex01


def selection_sort(nums: list[int]) -> list[int]:
    """Return a NEW list containing `nums` sorted ascending.

    Repeatedly find the minimum of the unsorted remainder and place it
    next. Does not modify `nums`.

    selection_sort([5, 2, 4, 1]) -> [1, 2, 4, 5]
    selection_sort([]) -> []

    Target complexity: O(n^2) time (always, regardless of input order),
    O(n) space (for the returned copy).
    """
    raise NotImplementedError


def insertion_sort(nums: list[int], counter: list[int] | None = None) -> list[int]:
    """Return a NEW list containing `nums` sorted ascending.

    Build the sorted region one element at a time, shifting larger
    already-placed elements one slot right to make room. Does not
    modify `nums`.

    If `counter` is given (a 1-element list used as an out-param),
    increment `counter[0]` once for every single-element SHIFT
    performed (not comparisons, not the empty case where an element is
    already in place) — this is how the tests measure adaptivity on
    nearly-sorted input.

    insertion_sort([5, 2, 4, 1]) -> [1, 2, 4, 5]
    insertion_sort([]) -> []

    Target complexity: O(n) time on nearly-sorted input, O(n^2) worst
    case (reverse-sorted); O(n) space (for the returned copy).
    """
    raise NotImplementedError
