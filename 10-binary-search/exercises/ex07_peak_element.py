# Scenario: a noisy signal trace (NOT sorted) where you just need to find
# a local maximum — a reading higher than both its neighbors. Pattern:
# binary search on an unsorted array. The array isn't monotone, but the
# SLOPE at `mid` is a reliable, monotone-enough signal about which half
# still contains a peak.
# Run: uv run pytest 10-binary-search -k ex07


def find_peak(nums: list[int]) -> int:
    """Return the index of ANY peak element in `nums`: an index `i`
    where `nums[i]` is strictly greater than each neighbor that exists
    (treat both ends of the array as bordered by -infinity, so the
    first or last element counts as a peak if it's greater than its one
    neighbor). Adjacent elements are never equal.

    Why this is still binary-searchable: compare `nums[mid]` to
    `nums[mid + 1]`. If it's uphill (`nums[mid] < nums[mid + 1]`), a peak
    is guaranteed somewhere to the right, so discard the left half.
    Otherwise a peak is guaranteed at `mid` or to its left, so discard
    the right half. Exactly one half is ever ruled out, per step — that
    is the whole requirement for binary search, and it doesn't need the
    array to be sorted.

    find_peak([1, 2, 3, 1]) -> 2
    find_peak([1, 2, 1, 3, 5, 6, 4]) -> 1 or 5 (either valid peak)
    find_peak([5]) -> 0
    find_peak([1, 2]) -> 1

    Target: O(log n) time, O(1) space.
    """
    raise NotImplementedError
