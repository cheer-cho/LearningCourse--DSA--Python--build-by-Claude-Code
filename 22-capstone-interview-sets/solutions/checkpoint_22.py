def count_ranges_with_total(fuel_deltas: list[int], target: int) -> int:
    # Pattern: prefix sums + hash map (module 04 - two pointers &
    # prefix sums). Values can be negative, so a sliding window can't
    # shrink monotonically -- prefix_sum[j] - prefix_sum[i] == target
    # turns "count ranges summing to target" into "count pairs of
    # equal prefix sums seen before," a single hash-map pass.
    # O(n) time, O(n) space.
    counts: dict[int, int] = {0: 1}
    running = 0
    total = 0
    for delta in fuel_deltas:
        running += delta
        total += counts.get(running - target, 0)
        counts[running] = counts.get(running, 0) + 1
    return total


def earliest_shelter_network(n: int, roads: list[tuple[int, int, int]]) -> int:
    # Pattern: union-find over edges processed in time order (module
    # 16 - graphs 2). "Are they all connected yet?" as roads arrive is
    # exactly online dynamic connectivity; sort by time first so union
    # order matches real-world arrival order.
    # O(m log m) time (the sort dominates), O(n + m) space.
    if n <= 1:
        return 0

    parent = list(range(n))
    rank = [0] * n

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a: int, b: int) -> bool:
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        if rank[ra] < rank[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        if rank[ra] == rank[rb]:
            rank[ra] += 1
        return True

    remaining_components = n
    for time, a, b in sorted(roads, key=lambda r: r[0]):
        if union(a, b):
            remaining_components -= 1
            if remaining_components == 1:
                return time
    return -1


def max_nonoverlapping_meetings(meetings: list[tuple[int, int]]) -> int:
    # Pattern: greedy, earliest-finish-time scheduling (module 17 -
    # greedy & intervals). Sorting by END time and always keeping the
    # meeting that frees the room soonest is the classic exchange-
    # argument greedy: any optimal schedule can be rearranged to start
    # with the earliest-ending meeting without losing count.
    # O(n log n) time, O(1) extra space.
    count = 0
    room_free_at = float("-inf")
    for start, end in sorted(meetings, key=lambda m: m[1]):
        if start >= room_free_at:
            count += 1
            room_free_at = end
    return count


class VolumeTracker:
    # Pattern: Fenwick tree / binary indexed tree (module 21 - advanced
    # structures & strings). Point updates and prefix sums both cost
    # O(log n) by walking the tree's implicit bit structure -- far
    # cheaper than an O(n) rescan per query or an O(n) shift per update.
    # update: O(log n), range_sum: O(log n).

    def __init__(self, n: int) -> None:
        self._n = n
        self._tree = [0] * (n + 1)  # 1-indexed internally

    def update(self, index: int, delta: int) -> None:
        i = index + 1
        while i <= self._n:
            self._tree[i] += delta
            i += i & (-i)

    def _prefix_sum(self, index: int) -> int:
        # Sum of buckets 0..index, inclusive (0-indexed).
        total = 0
        i = index + 1
        while i > 0:
            total += self._tree[i]
            i -= i & (-i)
        return total

    def range_sum(self, left: int, right: int) -> int:
        if left == 0:
            return self._prefix_sum(right)
        return self._prefix_sum(right) - self._prefix_sum(left - 1)
