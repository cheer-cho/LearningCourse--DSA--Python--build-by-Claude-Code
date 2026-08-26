from collections.abc import Callable


def counting_sort[T](
    nums: list[T],
    max_value: int,
    key: Callable[[T], int] = lambda x: x,  # type: ignore[assignment, return-value]
) -> list[T]:
    # Pattern: counting sort — count occurrences of each key value,
    # turn counts into starting offsets (prefix sum), then place every
    # element directly at its final index. Applies here because keys
    # are bounded ints, so we never need to compare two elements.
    # Complexity: O(n + max_value) time and space.
    counts = [0] * (max_value + 1)
    for item in nums:
        k = key(item)
        if not (0 <= k <= max_value):
            raise ValueError(f"key {k!r} is outside [0, {max_value}]")
        counts[k] += 1

    # counts[v] becomes "how many items have key < v" — the starting
    # offset for value v in the output.
    offset = 0
    for v in range(max_value + 1):
        count = counts[v]
        counts[v] = offset
        offset += count

    result: list[T | None] = [None] * len(nums)
    for item in nums:  # single left-to-right pass keeps it stable
        k = key(item)
        result[counts[k]] = item
        counts[k] += 1
    return result  # type: ignore[return-value]


def sort_colors(nums: list[int]) -> None:
    # Pattern: Dutch national flag — three pointers (low/mid/high)
    # partition into three regions in one pass. Applies here for the
    # bounded 3-value case (0/1/2), beating even counting sort's two
    # passes. Complexity: O(n) time, one pass, O(1) space.
    low, mid, high = 0, 0, len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
            # don't advance mid: the swapped-in value from `high` is
            # unexamined and needs its own check next iteration
