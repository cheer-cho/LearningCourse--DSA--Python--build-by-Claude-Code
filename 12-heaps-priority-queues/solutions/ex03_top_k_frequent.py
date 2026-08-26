import heapq
from collections import Counter


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    # Pattern: top-k via a size-k MIN-heap keyed on frequency (the
    # k-size-heap inversion: want the k LARGEST counts -> keep a
    # min-heap so the worst of the current top-k sits at the root,
    # ready to be evicted).
    # Time: O(n log k) -- counting is O(n), then n pushes/pops each
    # bounded to heap size k. Space: O(n) for the counts.
    counts = Counter(nums)
    heap: list[tuple[int, int]] = []

    for value, count in counts.items():
        if len(heap) < k:
            heapq.heappush(heap, (count, value))
        elif count > heap[0][0]:
            heapq.heapreplace(heap, (count, value))

    return [value for _count, value in heap]
