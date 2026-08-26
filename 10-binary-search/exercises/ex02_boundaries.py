# Scenario: a sorted price list with repeated prices — you need the first
# and last position of a price, and the spot to insert a new one to keep
# it sorted. Pattern: boundary search (lower bound / upper bound), the
# workhorse behind count_occurrences, rotated search, and search-on-answer.
# Run: uv run pytest 10-binary-search -k ex02


def lower_bound(nums: list[int], x: int) -> int:
    """Return the first index `i` where `nums[i] >= x`.

    If every element is `< x`, return `len(nums)` (the insertion point at
    the end). `nums` is sorted ascending and may contain duplicates.

    lower_bound([1, 3, 3, 3, 5], 3) -> 1
    lower_bound([1, 3, 3, 3, 5], 4) -> 4
    lower_bound([1, 3, 3, 3, 5], 0) -> 0
    lower_bound([], 5) -> 0

    Target: O(log n) time, O(1) space.
    """
    raise NotImplementedError


def upper_bound(nums: list[int], x: int) -> int:
    """Return the first index `i` where `nums[i] > x`.

    If every element is `<= x`, return `len(nums)`. `nums` is sorted
    ascending and may contain duplicates.

    upper_bound([1, 3, 3, 3, 5], 3) -> 4
    upper_bound([1, 3, 3, 3, 5], 4) -> 4
    upper_bound([1, 3, 3, 3, 5], 0) -> 0

    Target: O(log n) time, O(1) space.
    """
    raise NotImplementedError


def insert_position(nums: list[int], x: int) -> int:
    """Return the index where `x` should be inserted into sorted `nums`
    to keep it sorted, preferring the LEFTMOST valid spot when `x`
    already appears (i.e. this is exactly `lower_bound`).

    insert_position([1, 3, 5, 7], 5) -> 2
    insert_position([1, 3, 5, 7], 6) -> 3
    insert_position([1, 3, 5, 7], 0) -> 0
    insert_position([], 4) -> 0

    Target: O(log n) time, O(1) space.
    """
    raise NotImplementedError
