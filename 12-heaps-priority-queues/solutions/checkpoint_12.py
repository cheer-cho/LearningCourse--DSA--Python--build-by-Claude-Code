import heapq
import itertools


class TriageQueue:
    # Pattern: priority queue via a heap keyed (-severity, timestamp,
    # counter). Negate severity so heapq's min-heap serves the HIGHEST
    # severity first; timestamp breaks ties FIFO; counter is a final,
    # always-unique tiebreak so two same-severity/same-timestamp
    # patients never fall through to comparing names.
    # Time: arrive/next_patient O(log n). Space: O(n).

    def __init__(self) -> None:
        self._heap: list[tuple[int, float, int, str]] = []
        self._counter = itertools.count()

    def arrive(self, name: str, severity: int, timestamp: float) -> None:
        heapq.heappush(self._heap, (-severity, timestamp, next(self._counter), name))

    def next_patient(self) -> str:
        if not self._heap:
            raise IndexError("no patients waiting")
        return heapq.heappop(self._heap)[3]

    def waiting_count(self) -> int:
        return len(self._heap)


def k_most_urgent(records: list[tuple[str, int, float]], k: int) -> list[str]:
    # Pattern: top-k via a size-k MIN-heap, same inversion as ex03 --
    # want the k records with the HIGHEST urgency, so keep a min-heap
    # of size k and evict the least-urgent one whenever a more urgent
    # record shows up. Key encodes "bigger = more urgent": severity
    # ascending, then -timestamp (earlier arrival = bigger = more
    # urgent), then a counter for a total, crash-proof order.
    # Time: O(n log k) to scan + O(k log k) to order the final k
    # (dominated by n log k since k <= n). Space: O(k).
    heap: list[tuple[tuple[int, float, int], str]] = []
    counter = itertools.count()

    for name, severity, timestamp in records:
        key = (severity, -timestamp, next(counter))
        if len(heap) < k:
            heapq.heappush(heap, (key, name))
        elif key > heap[0][0]:
            heapq.heapreplace(heap, (key, name))

    ordered = sorted(heap, key=lambda pair: pair[0], reverse=True)
    return [name for _key, name in ordered]
