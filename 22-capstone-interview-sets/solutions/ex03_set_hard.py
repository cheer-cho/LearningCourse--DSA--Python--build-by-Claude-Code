import heapq


def max_survival_value(weights: list[int], values: list[int], capacity: int) -> int:
    # Pattern: 0/1 knapsack, DP-2D collapsed to a rolling 1-D array
    # (module 19 - DP on 2-D state). State: best value achievable at
    # each capacity using items considered so far. Each item is used
    # at most once, so capacity must be scanned HIGH to LOW -- scanning
    # low to high would let the same item's weight be "reused" in the
    # same pass, turning this into unbounded knapsack by accident.
    # O(n * capacity) time, O(capacity) space.
    dp = [0] * (capacity + 1)
    for weight, value in zip(weights, values):
        for cap in range(capacity, weight - 1, -1):
            dp[cap] = max(dp[cap], dp[cap - weight] + value)
    return dp[capacity]


def cheapest_delivery_with_stops(
    num_hubs: int,
    routes: list[tuple[int, int, int]],
    src: int,
    dst: int,
    max_stops: int,
) -> int:
    # Pattern: Bellman-Ford style bounded relaxation (module 16 -
    # graphs 2, "Bellman-Ford taste: k-stops cheapest path"). Dijkstra
    # doesn't track HOW MANY edges a path used, so it can't respect a
    # stop limit; relaxing from a frozen snapshot of the previous round,
    # exactly max_stops + 1 times, caps every found path at that many
    # edges.
    # O(max_stops * len(routes)) time, O(num_hubs) space.
    INF = float("inf")
    dist = [INF] * num_hubs
    dist[src] = 0
    for _ in range(max_stops + 1):
        prev = dist[:]
        for u, v, cost in routes:
            dist[v] = min(dist[v], prev[u] + cost)
    return int(dist[dst]) if dist[dst] != INF else -1


class LatencyMedianTracker:
    # Pattern: two heaps (module 12 - heaps & priority queues). A
    # max-heap ("lows", negated for Python's min-heap) holds the
    # smaller half, a min-heap ("highs") holds the larger half; keeping
    # their sizes within 1 of each other means the median is always at
    # one or both heap tops -- no re-sort needed per query.
    # add: O(log n), median: O(1).

    def __init__(self) -> None:
        self._lows: list[float] = []  # max-heap, values negated
        self._highs: list[float] = []  # min-heap, values as-is

    def add(self, value: float) -> None:
        if self._lows and value > -self._lows[0]:
            heapq.heappush(self._highs, value)
        else:
            heapq.heappush(self._lows, -value)

        # Rebalance so sizes never differ by more than 1.
        if len(self._lows) > len(self._highs) + 1:
            heapq.heappush(self._highs, -heapq.heappop(self._lows))
        elif len(self._highs) > len(self._lows):
            heapq.heappush(self._lows, -heapq.heappop(self._highs))

    def median(self) -> float:
        if not self._lows and not self._highs:
            raise ValueError("no measurements recorded yet")
        if len(self._lows) > len(self._highs):
            return -self._lows[0]
        return (-self._lows[0] + self._highs[0]) / 2


def find_signature_occurrences(log: str, signature: str) -> list[int]:
    # Pattern: KMP string matching (module 21 - advanced structures &
    # strings). The failure/LPS table lets the scan resume without
    # re-checking already-matched characters after a mismatch, instead
    # of restarting from scratch (which is what makes naive search
    # O(n * m)).
    # O(len(log) + len(signature)) time, O(len(signature)) space.
    m = len(signature)
    lps = [0] * m
    length = 0
    i = 1
    while i < m:
        if signature[i] == signature[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1

    occurrences: list[int] = []
    j = 0  # index into signature
    for i, ch in enumerate(log):
        while j and ch != signature[j]:
            j = lps[j - 1]
        if ch == signature[j]:
            j += 1
        if j == m:
            occurrences.append(i - m + 1)
            j = lps[j - 1]
    return occurrences
