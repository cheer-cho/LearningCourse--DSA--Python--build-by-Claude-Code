import heapq


class MedianFinder:
    # Pattern: two heaps balanced against each other -- a MAX-heap
    # `_lows` (negated, since heapq is min-heap only) for the smaller
    # half, a MIN-heap `_highs` for the larger half. Keeping
    # len(lows) - len(highs) in {0, 1} means the median is always at
    # the top of one or both heaps: O(1) to read, O(log n) to add.

    def __init__(self) -> None:
        self._lows: list[int] = []  # max-heap, values negated
        self._highs: list[int] = []  # min-heap, values as-is

    def add(self, num: int) -> None:
        heapq.heappush(self._lows, -num)
        # Push the new low's max across to highs, to keep every low
        # value <= every high value.
        heapq.heappush(self._highs, -heapq.heappop(self._lows))

        # Rebalance sizes: lows may lead highs by at most 1.
        if len(self._highs) > len(self._lows):
            heapq.heappush(self._lows, -heapq.heappop(self._highs))

    def median(self) -> float:
        if not self._lows:
            raise ValueError("median of empty stream")
        if len(self._lows) > len(self._highs):
            return float(-self._lows[0])
        return (-self._lows[0] + self._highs[0]) / 2
