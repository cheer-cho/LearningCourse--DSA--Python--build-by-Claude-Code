# Scenario: a sensor logs daily readings; find the length of the
# longest run of days you could pick (not necessarily consecutive,
# order preserved) where each reading is strictly greater than the last.
# Pattern: "max length" DP first (O(n^2)), then the classic O(n log n)
# speed-up via binary search on a cleverly maintained array.
# Run: uv run pytest 18-dp-1d -k ex07

from __future__ import annotations


def lis_length(nums: list[int]) -> int:
    """Return the length of the Longest strictly Increasing Subsequence
    of `nums` (elements need not be contiguous; original order must be
    preserved; each next element must be strictly greater).

    STATE: dp[i] = length of the longest strictly increasing
    subsequence that ENDS AT index i (nums[i] is always included).
    CHOICE: which earlier index j (j < i, nums[j] < nums[i]) to extend.
    RECURRENCE: dp[i] = 1 + max(dp[j] for j < i if nums[j] < nums[i]),
    or just 1 if no such j exists (nums[i] starts its own run).
    BASE CASE: dp[i] = 1 for every i (every single element is a valid
    length-1 increasing subsequence on its own).
    Answer: max(dp) over all i (the best run doesn't have to end at
    the last index).

    lis_length([]) -> 0
    lis_length([5]) -> 1
    lis_length([10, 9, 2, 5, 3, 7, 101, 18]) -> 4  (2, 3, 7, 101 or 2, 3, 7, 18)
    lis_length([7, 7, 7, 7]) -> 1                  (strict: no repeats extend)

    Target: O(n^2) time, O(n) space.
    """
    raise NotImplementedError


def lis_length_fast(nums: list[int]) -> int:
    """Same answer as `lis_length`, in O(n log n).

    Idea ("patience sorting"): maintain `tails`, where `tails[k]` is
    the SMALLEST possible tail value among all increasing subsequences
    of length k + 1 seen so far. `tails` is always sorted, so for each
    new number x you binary-search it: find the first position where
    x could replace an existing tail (the leftmost `tails[i] >= x`,
    i.e. `lower_bound`) and overwrite there, or append if x is bigger
    than every tail. `len(tails)` at the end is the answer — replacing
    a tail with a smaller value never shrinks a real subsequence, it
    just keeps a cheaper option open for extending later.

    Reuses the module-10 half-open binary-search template directly
    (import nothing — reimplemented inline as `_lower_bound` below) to
    find that leftmost `tails[i] >= x` in O(log n).

    lis_length_fast([]) -> 0
    lis_length_fast([10, 9, 2, 5, 3, 7, 101, 18]) -> 4
    lis_length_fast([0, 1, 0, 3, 2, 3]) -> 4

    Target: O(n log n) time, O(n) space.
    """
    raise NotImplementedError
