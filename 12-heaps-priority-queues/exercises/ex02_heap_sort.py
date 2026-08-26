# Scenario: sort a list using nothing but the heap idea from ex01 — no
# `sorted()`, no `list.sort()`, no `heapq`. Pattern: heap sort (in-place
# max-heap: heapify bottom-up, then repeatedly swap the max to the end
# and shrink the heap). FROM SCRATCH.
# Run: uv run pytest 12-heaps-priority-queues -k ex02


def heap_sort(nums: list[int]) -> list[int]:
    """Return a NEW list with `nums`'s values sorted ascending.

    `nums` itself must be left unmodified. Use a heap (either build a
    max-heap in place and pop the max into the tail each round, or
    push everything into a min-heap and pop it all back out) — not
    Python's built-in `sorted`/`.sort()`/`heapq`.

    heap_sort([5, 1, 4, 2, 8]) -> [1, 2, 4, 5, 8]
    heap_sort([]) -> []
    heap_sort([3, 3, 1]) -> [1, 3, 3]

    Target complexity: O(n log n) time, O(n) space (for the returned
    copy; O(1) extra beyond that if you sort in place on the copy).
    """
    raise NotImplementedError
