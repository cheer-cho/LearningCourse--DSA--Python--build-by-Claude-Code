import heapq


def k_closest(points: list[tuple[int, int]], k: int) -> list[tuple[int, int]]:
    # Pattern: top-k SMALLEST via a size-k MAX-heap (negate the
    # distance so Python's min-heap `heapq` behaves like a max-heap on
    # distance). Compare squared distance -- monotonic, no sqrt needed.
    # Time: O(n log k). Space: O(k) for the heap.
    heap: list[tuple[int, tuple[int, int]]] = []

    for point in points:
        dist_sq = point[0] * point[0] + point[1] * point[1]
        if len(heap) < k:
            heapq.heappush(heap, (-dist_sq, point))
        elif -dist_sq > heap[0][0]:
            heapq.heapreplace(heap, (-dist_sq, point))

    return [point for _neg_dist, point in heap]
