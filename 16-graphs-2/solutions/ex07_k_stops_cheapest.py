def cheapest_within_k_stops(
    n: int, flights: list[tuple[int, int, int]], src: int, dst: int, k: int
) -> int | None:
    # Pattern: Bellman-Ford-style bounded relaxation -- k+1 rounds,
    # each relaxing every edge against a SNAPSHOT of the previous
    # round's distances so one round can only extend a path by one
    # edge (caps the route at k+1 edges total).
    # Complexity: O(k * e) time, O(n) space.
    inf = float("inf")
    dist = [inf] * n
    dist[src] = 0

    for _ in range(k + 1):
        dist_next = dist.copy()
        for u, v, price in flights:
            if dist[u] != inf and dist[u] + price < dist_next[v]:
                dist_next[v] = dist[u] + price
        dist = dist_next

    return dist[dst] if dist[dst] != inf else None
