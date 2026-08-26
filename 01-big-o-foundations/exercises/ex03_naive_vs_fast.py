# Scenario: a data-cleaning job needs to know if a batch of IDs has any
# duplicate before it proceeds. Build the honest O(n^2) version first
# (so the tick count proves you didn't cheat), then the O(n) version.
# Concepts: all-pairs comparison vs a "have I seen this before?" set.
# Run: uv run pytest 01-big-o-foundations -k ex03

from collections.abc import Callable


def has_duplicate_naive(nums: list[int], tick: Callable[[], None]) -> bool:
    """Return True if any value in `nums` appears more than once.
    Compare pairs of distinct positions (i, j) with i < j in order,
    calling `tick()` once per comparison performed. Stop and return as
    soon as you find a duplicate -- don't keep comparing after that.

    has_duplicate_naive([1, 2, 3], tick) -> False
    has_duplicate_naive([1, 2, 1], tick) -> True

    Target complexity: O(n^2) time, O(1) extra space. This is the
    deliberately naive brute force -- ex05 walks the full framework
    that gets you from here to something faster.
    """
    raise NotImplementedError


def has_duplicate_fast(nums: list[int]) -> bool:
    """Return True if any value in `nums` appears more than once.

    has_duplicate_fast([1, 2, 3]) -> False
    has_duplicate_fast([1, 2, 1]) -> True

    Target complexity: O(n) time, O(n) space.
    """
    raise NotImplementedError
