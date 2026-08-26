# Scenario: combining two sorted leaderboards into one, and merging a
# smaller sorted batch directly into a buffer that already has the room for
# it. Concepts: linear merge, filling a shared buffer from the back to
# avoid overwriting data you haven't read yet.
# Run: uv run pytest 02-arrays-dynamic-arrays -k ex04


def merge(a: list[int], b: list[int]) -> list[int]:
    """Merge two ascending-sorted lists into a new ascending-sorted list.
    Does not modify `a` or `b`.

    merge([1, 3, 5], [2, 4, 6]) -> [1, 2, 3, 4, 5, 6]
    merge([], [1, 2]) -> [1, 2]
    merge([1, 1], [1]) -> [1, 1, 1]

    Target complexity: O(m + n) time, O(m + n) space (for the result).
    """
    raise NotImplementedError


def merge_into(a: list[int], m: int, b: list[int]) -> None:
    """`a` holds `m` valid sorted elements in `a[:m]`, followed by exactly
    `len(b)` unused placeholder slots — so `len(a) == m + len(b)`. Merge
    `b` into `a` IN PLACE so `a` ends up fully sorted, using no extra
    array. `b` is not modified.

    Fill `a` from the BACK: the last placeholder slot only needs to be
    written once, so writing back-to-front means you never overwrite an
    `a` value before you've had the chance to read it.

    a = [1, 3, 5, 0, 0, 0]; merge_into(a, 3, [2, 4, 6])
        -> a is now [1, 2, 3, 4, 5, 6]
    a = [0, 0, 0]; merge_into(a, 0, [1, 2, 3])
        -> a is now [1, 2, 3]
    a = [1, 2, 3]; merge_into(a, 3, [])
        -> a is still [1, 2, 3]

    Target complexity: O(m + n) time, O(1) extra space.
    """
    raise NotImplementedError
