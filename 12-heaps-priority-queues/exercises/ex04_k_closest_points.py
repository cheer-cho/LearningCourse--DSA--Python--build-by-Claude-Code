# Scenario: a delivery app needs the k nearest warehouses to a
# customer's location (origin-relative coordinates). Pattern: top-k
# via a size-k heap, same inversion as ex03 but keyed on distance.
# Run: uv run pytest 12-heaps-priority-queues -k ex04


def k_closest(points: list[tuple[int, int]], k: int) -> list[tuple[int, int]]:
    """Return the `k` points closest to the origin (0, 0), in any order.

    `k` is between 1 and `len(points)`. Compare SQUARED distance
    (`x*x + y*y`) instead of calling `sqrt` — square root is monotonic
    for non-negative numbers, so it never changes which point is
    closer, and skipping it avoids float error for free.

    k_closest([(1, 1), (3, 3), (0, 1)], 2) -> two of the points, the
        pair with the smallest squared distance: {(1, 1), (0, 1)}

    Two valid approaches:
    - keep a size-k MAX-heap of (negative) squared distances (want the
      k SMALLEST distances -> the inversion again, mirrored from ex03):
      O(n log k).
    - `heapify` all n points at once and pop k times: O(n + k log n),
      better when k is close to n.

    Target complexity: O(n log k) time, O(k) space (beyond the input).
    """
    raise NotImplementedError
