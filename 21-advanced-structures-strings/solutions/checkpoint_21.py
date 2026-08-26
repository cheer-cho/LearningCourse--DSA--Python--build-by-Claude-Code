from __future__ import annotations

# Combines: two segment trees (sum + min) for record/window_total/
# window_low; KMP for alert_scan (guaranteed O(n+m), no collision
# risk -- a good default for scanning an operational log where
# adversarial input isn't worth worrying about but a wasted-time
# false positive is); prefix sums for busiest_window (sum is
# invertible, so a running prefix total is simpler than a deque and
# still O(n)).


class _MergeTree:
    """Generic array-based segment tree parameterized by a merge
    function and identity element -- see ex01/ex02's discussion of
    the merge-function generalization.
    """

    def __init__(self, nums: list[int], identity: float, merge) -> None:
        self.n = len(nums)
        self.identity = identity
        self.merge = merge
        self.tree: list[int | float] = [identity] * (4 * self.n)
        if self.n > 0:
            self._build(nums, 0, 0, self.n - 1)

    def _build(self, nums: list[int], node: int, lo: int, hi: int) -> None:
        if lo == hi:
            self.tree[node] = nums[lo]
            return
        mid = (lo + hi) // 2
        self._build(nums, 2 * node + 1, lo, mid)
        self._build(nums, 2 * node + 2, mid + 1, hi)
        self.tree[node] = self.merge(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def query(self, i: int, j: int):
        return self._query(0, 0, self.n - 1, i, j)

    def _query(self, node: int, lo: int, hi: int, i: int, j: int):
        if i <= lo and hi <= j:
            return self.tree[node]
        if hi < i or lo > j:
            return self.identity
        mid = (lo + hi) // 2
        left = self._query(2 * node + 1, lo, mid, i, j)
        right = self._query(2 * node + 2, mid + 1, hi, i, j)
        return self.merge(left, right)

    def update(self, i: int, value: int) -> None:
        self._update(0, 0, self.n - 1, i, value)

    def _update(self, node: int, lo: int, hi: int, i: int, value: int) -> None:
        if lo == hi:
            self.tree[node] = value
            return
        mid = (lo + hi) // 2
        if i <= mid:
            self._update(2 * node + 1, lo, mid, i, value)
        else:
            self._update(2 * node + 2, mid + 1, hi, i, value)
        self.tree[node] = self.merge(self.tree[2 * node + 1], self.tree[2 * node + 2])


def _failure_table(pattern: str) -> list[int]:
    m = len(pattern)
    table = [0] * m
    border = 0
    for i in range(1, m):
        while border > 0 and pattern[border] != pattern[i]:
            border = table[border - 1]
        if pattern[border] == pattern[i]:
            border += 1
        table[i] = border
    return table


def _kmp_find_all(text: str, pattern: str) -> list[int]:
    n, m = len(text), len(pattern)
    if m == 0 or m > n:
        return []
    table = _failure_table(pattern)
    matches: list[int] = []
    j = 0
    for i in range(n):
        while j > 0 and pattern[j] != text[i]:
            j = table[j - 1]
        if pattern[j] == text[i]:
            j += 1
        if j == m:
            matches.append(i - j + 1)
            j = table[j - 1]
    return matches


class MetricsBoard:
    # Complexity: build O(n); record/window_total/window_low
    # O(log n) each; alert_scan O(n + m); busiest_window O(n).

    def __init__(self, initial_values: list[int]) -> None:
        self.sum_tree = _MergeTree(initial_values, 0, lambda a, b: a + b)
        self.min_tree = _MergeTree(initial_values, float("inf"), min)

    def record(self, i: int, v: int) -> None:
        self.sum_tree.update(i, v)
        self.min_tree.update(i, v)

    def window_total(self, i: int, j: int) -> int:
        return self.sum_tree.query(i, j)

    def window_low(self, i: int, j: int) -> int:
        return self.min_tree.query(i, j)

    def alert_scan(self, log_text: str, signature: str) -> list[int]:
        # Chose KMP: guaranteed O(n + m) with zero collision risk,
        # which matters for a log-scanning utility that must never
        # miss (or falsely report) a match regardless of input.
        return _kmp_find_all(log_text, signature)

    def busiest_window(self, readings: list[int], k: int) -> int:
        # Chose prefix sums: SUM is invertible (unlike min/max), so a
        # running prefix total gives O(n) with less code than a
        # monotonic deque -- reach for the simpler tool when it fits.
        n = len(readings)
        if n == 0 or k > n:
            return 0

        prefix = [0] * (n + 1)
        for idx in range(n):
            prefix[idx + 1] = prefix[idx] + readings[idx]

        best = max(prefix[end] - prefix[end - k] for end in range(k, n + 1))
        return best
