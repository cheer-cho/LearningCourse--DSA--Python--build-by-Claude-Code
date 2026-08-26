# Scenario: matching three sensor calibration offsets that cancel out
# to zero net drift. Pattern: sort + fix the first element + opposite-
# ends two pointers on the remainder, skipping duplicate values.
# Run: uv run pytest 04-two-pointers-prefix-sums -k ex04


def three_sum_zero(nums: list[int]) -> list[tuple[int, int, int]]:
    """Return every unique triplet of VALUES from `nums` that sums to
    zero, each triplet as an ascending tuple `(a, b, c)` with
    `a <= b <= c`.

    No duplicate triplets in the output, even if `nums` has repeated
    values. Sort `nums` first, then fix one value at a time as the
    smallest of the triplet and run an opposite-ends two-pointer scan
    over the rest for the other two — skipping past duplicate values
    at every position so the same triplet is never emitted twice.

    three_sum_zero([-1, 0, 1, 2, -1, -4]) -> [(-1, -1, 2), (-1, 0, 1)]
    three_sum_zero([0, 0, 0]) -> [(0, 0, 0)]
    three_sum_zero([1, 2, 3]) -> []

    Target complexity: O(n^2) time, O(1) extra space beyond the sort
    and the output itself.
    """
    raise NotImplementedError
