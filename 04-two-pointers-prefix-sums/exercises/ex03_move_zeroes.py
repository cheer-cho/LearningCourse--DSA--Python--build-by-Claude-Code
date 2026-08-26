# Scenario: compacting a sparse inventory list, pushing used-up slots
# (zeros) to the end without disturbing the order of items still in
# stock; then a warehouse re-sort that groups even bin IDs before odd
# ones (order within each group doesn't matter).
# Pattern: same-direction (reader/writer) and opposite-ends two
# pointers, both mutating in place.
# Run: uv run pytest 04-two-pointers-prefix-sums -k ex03


def move_zeroes(nums: list[int]) -> None:
    """Mutate `nums` in place so every 0 moves to the end, preserving
    the relative order of the non-zero elements.

    Same-direction reader/writer pattern: `write` tracks the next slot
    a non-zero value should land in; `read` scans forward. Mutates
    `nums` in place and returns nothing.

    nums = [0, 1, 0, 3, 12]
    move_zeroes(nums)  -> nums is now [1, 3, 12, 0, 0]

    Target complexity: O(n) time, O(1) extra space.
    """
    raise NotImplementedError


def partition_even_odd(nums: list[int]) -> None:
    """Mutate `nums` in place so every even number comes before every
    odd number. Order WITHIN each group is unspecified.

    Opposite-ends pattern: walk `left` forward looking for an odd
    value, `right` backward looking for an even value, and swap them.

    nums = [3, 1, 2, 4]
    partition_even_odd(nums)  -> nums now has all evens before all
    odds, e.g. [4, 2, 3, 1] (any such arrangement is acceptable)

    Target complexity: O(n) time, O(1) extra space.
    """
    raise NotImplementedError
