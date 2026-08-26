from __future__ import annotations

INF = float("inf")


class RangeMinTree:
    # Pattern: segment tree, array-based (4n storage) -- identical
    # skeleton to ex01's SegmentTree, only the merge function (min
    # instead of +) and identity element (+infinity instead of 0)
    # differ. Complexity: build O(n); range_min/update O(log n) time
    # and recursion depth each; O(n) space.

    def __init__(self, nums: list[int]) -> None:
        self.n = len(nums)
        self.tree = [INF] * (4 * self.n)
        if self.n > 0:
            self._build(nums, 0, 0, self.n - 1)

    def _build(self, nums: list[int], node: int, lo: int, hi: int) -> None:
        if lo == hi:
            self.tree[node] = nums[lo]
            return
        mid = (lo + hi) // 2
        self._build(nums, 2 * node + 1, lo, mid)
        self._build(nums, 2 * node + 2, mid + 1, hi)
        self.tree[node] = min(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def range_min(self, i: int, j: int) -> int:
        return self._query(0, 0, self.n - 1, i, j)

    def _query(self, node: int, lo: int, hi: int, i: int, j: int):
        if i <= lo and hi <= j:
            return self.tree[node]
        if hi < i or lo > j:
            return INF
        mid = (lo + hi) // 2
        left = self._query(2 * node + 1, lo, mid, i, j)
        right = self._query(2 * node + 2, mid + 1, hi, i, j)
        return min(left, right)

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
        self.tree[node] = min(self.tree[2 * node + 1], self.tree[2 * node + 2])
