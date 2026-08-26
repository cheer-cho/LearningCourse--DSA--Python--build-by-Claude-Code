# Scenario: a sorted leaderboard of unique scores you need to query fast,
# and a sorted sensor log (with repeats) where you need to know how many
# times a reading occurred. Pattern: THE binary search template; boundary
# search composed from it.
# Run: uv run pytest 10-binary-search -k ex01


def binary_search(nums: list[int], target: int) -> int:
    """Find `target` in `nums` (sorted ascending, values may repeat) and
    return ANY index where it occurs, or -1 if it's absent.

    Use the course template: half-open bounds `lo, hi = 0, len(nums)`,
    loop `while lo < hi`, `mid = lo + (hi - lo) // 2`.

    binary_search([1, 3, 5, 7, 9], 7) -> 3
    binary_search([1, 3, 5, 7, 9], 4) -> -1
    binary_search([], 4) -> -1

    Target: O(log n) time, O(1) space.
    """
    raise NotImplementedError


def count_occurrences(nums: list[int], target: int) -> int:
    """Count how many times `target` appears in `nums` (sorted ascending,
    may have duplicates).

    Don't scan linearly. Binary-search for the FIRST index where
    `nums[i] >= target` and the FIRST index where `nums[i] > target`
    (two boundary searches) — the count is the gap between them. You
    may write these as two small helper searches inside this function.

    count_occurrences([1, 2, 2, 2, 3, 4], 2) -> 3
    count_occurrences([1, 2, 2, 2, 3, 4], 5) -> 0
    count_occurrences([], 1) -> 0

    Target: O(log n) time, O(1) space.
    """
    raise NotImplementedError
