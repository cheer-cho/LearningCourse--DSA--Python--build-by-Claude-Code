# Scenario: sorting bounded data (ages, grades, three-color tags) where
# comparisons are wasted work you can skip entirely.
# Concepts: counting sort (bounded ints, stable), Dutch national flag
# three-way partition.
# Run: uv run pytest 09-sorting -k ex05

from collections.abc import Callable


def counting_sort[T](
    nums: list[T],
    max_value: int,
    key: Callable[[T], int] = lambda x: x,  # type: ignore[assignment, return-value]
) -> list[T]:
    """Return a NEW list containing `nums` sorted ascending by
    `key(element)`, where every key is an int in `[0, max_value]`.
    Does not modify `nums`. Must be STABLE: elements with equal keys
    keep their original relative order. Do NOT call `sorted()` or
    `list.sort()` — count occurrences and place elements directly,
    never compare two elements to each other.

    Raises ValueError if any key is outside `[0, max_value]`.

    counting_sort([3, 1, 1, 0, 2], max_value=3) -> [0, 1, 1, 2, 3]
    counting_sort([], max_value=5) -> []

    Target complexity: O(n + max_value) time, O(n + max_value) space.
    """
    raise NotImplementedError


def sort_colors(nums: list[int]) -> None:
    """Sort `nums` IN PLACE where every value is 0, 1, or 2 (think:
    red/white/blue tags). Returns None. One pass, three pointers
    (Dutch national flag): `low` is the boundary of placed 0s, `high`
    is the boundary of placed 2s, `mid` scans and swaps into place.

    nums = [2, 0, 1, 1, 0]; sort_colors(nums) -> nums is now [0, 0, 1, 1, 2]
    nums = []; sort_colors(nums) -> nums is still []

    Target complexity: O(n) time, single pass, O(1) space.
    """
    raise NotImplementedError
