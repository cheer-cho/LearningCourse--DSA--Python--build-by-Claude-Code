import heapq


def delivery_times(n: int, edges: list[tuple[int, int, int]], source: int) -> dict[int, int]:
    # Pattern: Dijkstra's shortest path -- min-heap frontier, lazy
    # deletion (skip a popped entry if a cheaper distance for that
    # node was already finalized).
    # Complexity: O(e log e) time, O(n + e) space.
    graph: list[list[tuple[int, int]]] = [[] for _ in range(n)]
    for u, v, time in edges:
        graph[u].append((v, time))

    dist = {source: 0}
    heap: list[tuple[int, int]] = [(0, source)]

    while heap:
        d, node = heapq.heappop(heap)
        if d > dist.get(node, float("inf")):
            continue  # stale: a cheaper path to `node` was already found

        for neighbor, weight in graph[node]:
            new_dist = d + weight
            if new_dist < dist.get(neighbor, float("inf")):
                dist[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))

    return {node: dist.get(node, -1) for node in range(n)}


def shortest_route(n: int, edges: list[tuple[int, int, int]], a: int, b: int) -> list[int] | None:
    # Pattern: Dijkstra + parent tracking -- same relaxation loop as
    # delivery_times, recording where each improvement came from so
    # the path can be replayed backward from the destination.
    # Complexity: O(e log e) time, O(n + e) space.
    graph: list[list[tuple[int, int]]] = [[] for _ in range(n)]
    for u, v, time in edges:
        graph[u].append((v, time))

    dist = {a: 0}
    parent: dict[int, int] = {}
    heap: list[tuple[int, int]] = [(0, a)]

    while heap:
        d, node = heapq.heappop(heap)
        if d > dist.get(node, float("inf")):
            continue
        if node == b:
            break

        for neighbor, weight in graph[node]:
            new_dist = d + weight
            if new_dist < dist.get(neighbor, float("inf")):
                dist[neighbor] = new_dist
                parent[neighbor] = node
                heapq.heappush(heap, (new_dist, neighbor))

    if b not in dist:
        return None

    path = [b]
    while path[-1] != a:
        path.append(parent[path[-1]])
    path.reverse()
    return path
