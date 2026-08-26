# Scenario: a scheduling tool has a pile of booked day-numbers (any
# order, possibly with gaps and duplicates) and needs the longest
# unbroken run of consecutive days. Pattern: the "set trick" — O(1)
# membership tests replace sorting.
# Run: uv run pytest 03-hashing -k ex04


def longest_consecutive(nums: list[int]) -> int:
    """Return the length of the longest run of consecutive integers
    that appears in `nums` (order in `nums` does not matter; duplicates
    don't extend a run). Return 0 for an empty list.

    Sorting would work in O(n log n), but you can do better: put every
    number in a set, then for each number that is a RUN START (its
    neighbor num - 1 is NOT in the set), walk forward counting num,
    num + 1, num + 2, ... while they're in the set. Because every
    number is only ever walked as part of its own run, the total work
    across all runs is O(n), not O(n^2).

    longest_consecutive([100, 4, 200, 1, 3, 2]) -> 4   # the run 1,2,3,4
    longest_consecutive([1, 2, 0, 1]) -> 3             # 0,1,2 (dup 1 ignored)
    longest_consecutive([]) -> 0

    Target: O(n) time, O(n) space.
    """
    raise NotImplementedError
