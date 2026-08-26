from __future__ import annotations


class Fenwick:
    # Pattern: Fenwick tree (Binary Indexed Tree). lowbit(i) = i & -i
    # isolates the lowest set bit. add(): walk UP, i += lowbit(i).
    # prefix_sum(): walk DOWN, i -= lowbit(i). Internally 1-indexed
    # (index 0 is never used -- lowbit(0) == 0 would loop forever).
    # Complexity: O(n) space; add/prefix_sum O(log n) each;
    # range_sum O(log n) (two prefix_sum calls).

    def __init__(self, n: int) -> None:
        self.n = n
        self.tree = [0] * (n + 1)

    def add(self, i: int, delta: int) -> None:
        pos = i + 1  # translate to 1-indexed
        while pos <= self.n:
            self.tree[pos] += delta
            pos += pos & (-pos)

    def prefix_sum(self, i: int) -> int:
        if i < 0:
            return 0
        pos = i + 1  # translate to 1-indexed
        total = 0
        while pos > 0:
            total += self.tree[pos]
            pos -= pos & (-pos)
        return total

    def range_sum(self, i: int, j: int) -> int:
        return self.prefix_sum(j) - self.prefix_sum(i - 1)


def count_smaller_after(nums: list[int]) -> list[int]:
    # Pattern: Fenwick tree over coordinate-compressed ranks, scanned
    # right to left. add(rank, 1) marks "one more element with this
    # rank seen so far (to the right)"; prefix_sum(rank - 1) counts
    # how many already-seen elements rank strictly below the current
    # one -- exactly "smaller elements after me."
    # Complexity: O(n log n) time (n inserts/queries, each O(log n));
    # O(n) space.
    n = len(nums)
    if n == 0:
        return []

    sorted_unique = sorted(set(nums))
    rank_of = {value: rank for rank, value in enumerate(sorted_unique)}

    fw = Fenwick(len(sorted_unique))
    result = [0] * n

    for i in range(n - 1, -1, -1):
        rank = rank_of[nums[i]]
        result[i] = fw.prefix_sum(rank - 1)
        fw.add(rank, 1)

    return result
