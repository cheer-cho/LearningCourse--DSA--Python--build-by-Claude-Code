import heapq


def min_cost_connect_points(points: list[tuple[int, int]]) -> int:
    # Pattern: Prim's MST on an implicit dense graph -- grow one tree,
    # a min-heap picks the cheapest edge leaving it, lazy-skip stale
    # (already-visited) heap entries instead of removing them.
    # Why Prim over Kruskal here: the graph is dense (n^2/2 edges) and
    # never materialized; Prim computes distances on demand instead of
    # building + sorting every edge up front.
    # Complexity: O(n^2 log n) time, O(n^2) heap space worst case.
    n = len(points)
    if n <= 1:
        return 0

    visited = [False] * n
    heap: list[tuple[int, int]] = [(0, 0)]
    total_cost = 0
    visited_count = 0

    while heap and visited_count < n:
        dist, node = heapq.heappop(heap)
        if visited[node]:
            continue  # stale entry from before `node` was added -- skip

        visited[node] = True
        visited_count += 1
        total_cost += dist

        x1, y1 = points[node]
        for other in range(n):
            if not visited[other]:
                x2, y2 = points[other]
                manhattan = abs(x1 - x2) + abs(y1 - y2)
                heapq.heappush(heap, (manhattan, other))

    return total_cost
