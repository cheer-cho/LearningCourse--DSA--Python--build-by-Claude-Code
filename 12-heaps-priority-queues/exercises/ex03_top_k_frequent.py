# Scenario: a stream analytics dashboard needs the k most-frequent
# values in a huge log of events. Pattern: top-k via a size-k heap.
# `heapq` is allowed from here on.
# Run: uv run pytest 12-heaps-priority-queues -k ex03


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    """Return the `k` most frequent values in `nums`, in any order.

    `k` is between 1 and the number of distinct values in `nums`. Ties
    in frequency may be broken any way you like.

    top_k_frequent([1, 1, 1, 2, 2, 3], 2) -> [1, 2]  (order doesn't matter)
    top_k_frequent([5], 1) -> [5]

    Three ways to solve this, in increasing cleverness:
    - sort all distinct values by count: O(n log n).
    - keep a MIN-heap of size k (the k-size-heap inversion — see
      LESSON.md): O(n log k), better when k is much smaller than n.
    - bucket by count (index = count, 1..n possible buckets): O(n),
      the best possible, since you still have to look at every value
      once. Not required here, but worth knowing.

    Target complexity: O(n log k) time, O(n) space.
    """
    raise NotImplementedError
