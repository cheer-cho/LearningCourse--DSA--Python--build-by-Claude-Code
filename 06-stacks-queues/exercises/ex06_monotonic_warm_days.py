# Scenario: a weather dashboard needs, for every day, how many days
# until a strictly warmer one — and separately, a generic "next bigger
# value" lookup that shows up all over interview problems. Concepts:
# monotonic stack of INDEXES, O(n) amortized (each index pushed/popped
# at most once).
# Run: uv run pytest 06-stacks-queues -k ex06


def days_until_warmer(temps: list[int]) -> list[int]:
    """For each day, return how many days until a strictly warmer day.

    Return 0 for a day with no warmer day ahead. Keep a stack of
    INDEXES whose temperatures are still "waiting" for a warmer day;
    pop an index whenever `temps[i]` beats the top of the stack, and
    the popped index's answer is `i - popped_index`.

    days_until_warmer([73, 74, 75, 71, 69, 72, 76, 73]) -> [1, 1, 4, 2, 1, 1, 0, 0]
    days_until_warmer([30, 40, 50]) -> [1, 1, 0]
    days_until_warmer([50, 40, 30]) -> [0, 0, 0]
    days_until_warmer([]) -> []

    Target complexity: O(n) time, O(n) space — each index is pushed and
    popped at most once.
    """
    raise NotImplementedError


def next_greater(nums: list[int]) -> list[int]:
    """For each element, return the next element to its right that is
    strictly greater, or -1 if none exists.

    next_greater([2, 1, 3, 4]) -> [3, 3, 4, -1]
    next_greater([4, 3, 2, 1]) -> [-1, -1, -1, -1]
    next_greater([1, 2, 3]) -> [2, 3, -1]
    next_greater([]) -> []

    Target complexity: O(n) time, O(n) space.
    """
    raise NotImplementedError
