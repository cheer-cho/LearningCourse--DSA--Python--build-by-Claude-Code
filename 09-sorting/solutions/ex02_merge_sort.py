from collections.abc import Callable
from typing import Any


def merge_sort[T](nums: list[T], key: Callable[[T], Any] | None = None) -> list[T]:
    # Pattern: divide & conquer — split in half, recursively sort each
    # half, merge the two sorted halves in one linear pass. Applies
    # here for a worst-case guarantee (unlike quick sort) and stability
    # (the merge step uses <=, never leapfrogging equal elements).
    # Complexity: O(n log n) time (log n levels x O(n) merge work per
    # level), O(n) space for the merge buffers.
    get_key = key if key is not None else (lambda x: x)

    if len(nums) <= 1:
        return nums[:]

    mid = len(nums) // 2
    left = merge_sort(nums[:mid], key)
    right = merge_sort(nums[mid:], key)
    return _merge(left, right, get_key)


def _merge[T](left: list[T], right: list[T], get_key: Callable[[T], Any]) -> list[T]:
    result: list[T] = []
    i = j = 0
    while i < len(left) and j < len(right):
        # <= (not <) is what keeps the merge stable: on a tie, the left
        # half (which came first in the original array) wins.
        if get_key(left[i]) <= get_key(right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
