import heapq


class KthLargest:
    # Pattern: size-k MIN-heap holding the k largest values seen so
    # far; its root is the kth largest (the top-k inversion from
    # LESSON.md, kept alive across calls instead of recomputed).
    # Time: O(log k) per add. Space: O(k).

    def __init__(self, k: int, initial: list[int]) -> None:
        self._k = k
        self._heap: list[int] = []
        for val in initial:
            self._offer(val)

    def add(self, val: int) -> int:
        self._offer(val)
        return self._heap[0]

    def _offer(self, val: int) -> None:
        if len(self._heap) < self._k:
            heapq.heappush(self._heap, val)
        elif val > self._heap[0]:
            heapq.heapreplace(self._heap, val)
