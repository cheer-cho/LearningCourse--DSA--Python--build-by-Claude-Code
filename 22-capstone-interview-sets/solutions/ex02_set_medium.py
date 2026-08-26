import heapq
from collections import Counter


def longest_run_at_most_k_genres(genres: list[str], k: int) -> int:
    # Pattern: variable-size sliding window + hash map (module 05 -
    # sliding window). Grow the right edge, track distinct-genre counts
    # in a map, shrink from the left only while the distinct count
    # exceeds k.
    # O(n) time, O(k) space.
    if k <= 0:
        return 0
    counts: dict[str, int] = {}
    left = 0
    best = 0
    for right, genre in enumerate(genres):
        counts[genre] = counts.get(genre, 0) + 1
        while len(counts) > k:
            left_genre = genres[left]
            counts[left_genre] -= 1
            if counts[left_genre] == 0:
                del counts[left_genre]
            left += 1
        best = max(best, right - left + 1)
    return best


def buildings_until_taller(heights: list[int]) -> list[int]:
    # Pattern: monotonic stack (module 06 - stacks & queues). Keep
    # indices of buildings with no taller building seen yet to their
    # right; each index is pushed once and popped once -> amortized O(n).
    # O(n) time, O(n) space.
    n = len(heights)
    result = [0] * n
    stack: list[int] = []  # indices, heights decreasing bottom to top
    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] < h:
            j = stack.pop()
            result[j] = i - j
        stack.append(i)
    return result


def top_k_frequent_skus(scans: list[str], k: int) -> list[str]:
    # Pattern: top-k via heap (module 12 - heaps & priority queues).
    # Count frequencies, then use a size-k structure instead of sorting
    # every distinct SKU.
    # O(n log k) time, O(n) space.
    counts = Counter(scans)
    # Rank each SKU by (-frequency, sku): more negative -frequency sorts
    # first (higher freq wins), and for equal frequency the smaller sku
    # string sorts first (matches the ascending tie-break). nsmallest
    # picks the k best under that ranking in O(n log k) via an internal
    # heap, already in the exact output order we need.
    top = heapq.nsmallest(k, counts.items(), key=lambda kv: (-kv[1], kv[0]))
    return [sku for sku, _freq in top]


def station_run_order(
    num_stations: int, prerequisites: list[tuple[int, int]]
) -> list[int] | None:
    # Pattern: topological sort, Kahn's BFS (module 16 - graphs 2).
    # A min-heap instead of a plain queue gives a deterministic
    # "lowest-numbered ready station first" order.
    # O((V + E) log V) time (heap ops), O(V + E) space.
    adj: list[list[int]] = [[] for _ in range(num_stations)]
    indegree = [0] * num_stations
    for after, before in prerequisites:
        adj[before].append(after)
        indegree[after] += 1

    ready = [s for s in range(num_stations) if indegree[s] == 0]
    heapq.heapify(ready)
    order: list[int] = []
    while ready:
        station = heapq.heappop(ready)
        order.append(station)
        for nxt in adj[station]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                heapq.heappush(ready, nxt)

    return order if len(order) == num_stations else None


def min_notes_for_amount(denominations: list[int], amount: int) -> int:
    # Pattern: 1-D DP, unbounded coin change (module 18 - DP on 1-D
    # sequences). dp[a] = fewest notes to make amount a; each
    # denomination can be reused, so we iterate amounts outward from 0.
    # O(amount * len(denominations)) time, O(amount) space.
    INF = amount + 1
    dp = [0] + [INF] * amount
    for a in range(1, amount + 1):
        for note in denominations:
            if note <= a and dp[a - note] + 1 < dp[a]:
                dp[a] = dp[a - note] + 1
    return dp[amount] if dp[amount] != INF else -1


def unique_arrangements(fragment: str) -> list[str]:
    # Pattern: backtracking with duplicate pruning (module 14 -
    # backtracking). Sort first so equal letters are adjacent, then
    # skip re-using an identical letter at the same recursion depth to
    # avoid generating the same permutation twice.
    # O(n! * n) time/space in the worst case, bounded by n <= 8.
    letters = sorted(fragment)
    n = len(letters)
    used = [False] * n
    path: list[str] = []
    results: list[str] = []

    def backtrack() -> None:
        if len(path) == n:
            results.append("".join(path))
            return
        for i in range(n):
            if used[i]:
                continue
            if i > 0 and letters[i] == letters[i - 1] and not used[i - 1]:
                continue  # same letter as an unused sibling -> duplicate branch
            used[i] = True
            path.append(letters[i])
            backtrack()
            path.pop()
            used[i] = False

    backtrack()
    return results
