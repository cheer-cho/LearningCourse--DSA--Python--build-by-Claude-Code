import heapq
from collections import deque

from ex02_build_union_find import UnionFind


def project_order(projects: list[str], deps: list[tuple[str, str]]) -> list[str] | None:
    # Pattern: Kahn's topological sort over named nodes -- map names to
    # indices, reuse the same in-degree + queue algorithm as ex01, map
    # the result back to names.
    # Complexity: O(n + e) time/space.
    index = {name: i for i, name in enumerate(projects)}
    n = len(projects)
    graph: list[list[int]] = [[] for _ in range(n)]
    in_degree = [0] * n
    for project, prereq in deps:
        graph[index[prereq]].append(index[project])
        in_degree[index[project]] += 1

    queue: deque[int] = deque(i for i in range(n) if in_degree[i] == 0)
    order: list[int] = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(order) != n:
        return None
    return [projects[i] for i in order]


def cheapest_grid(n: int, routes: list[tuple[int, int, int]]) -> int | None:
    # Pattern: Kruskal's MST -- identical shape to ex04's
    # min_connection_cost, reusing the from-scratch UnionFind.
    # Complexity: O(e log e) time, O(n) space.
    uf = UnionFind(n)
    total_cost = 0
    edges_used = 0
    for a, b, cost in sorted(routes, key=lambda route: route[2]):
        if uf.union(a, b):
            total_cost += cost
            edges_used += 1
            if edges_used == n - 1:
                break
    return total_cost if edges_used == n - 1 else None


def fastest_signal(n: int, routes: list[tuple[int, int, int]], hub: int) -> dict[int, int]:
    # Pattern: Dijkstra with a lazy-deletion min-heap, same as ex06's
    # delivery_times, but the adjacency list is UNDIRECTED (each route
    # pushed onto both endpoints).
    # Complexity: O(e log e) time, O(n + e) space.
    graph: list[list[tuple[int, int]]] = [[] for _ in range(n)]
    for a, b, cost in routes:
        graph[a].append((b, cost))
        graph[b].append((a, cost))

    dist = {hub: 0}
    heap: list[tuple[int, int]] = [(0, hub)]
    while heap:
        d, node = heapq.heappop(heap)
        if d > dist.get(node, float("inf")):
            continue
        for neighbor, weight in graph[node]:
            new_dist = d + weight
            if new_dist < dist.get(neighbor, float("inf")):
                dist[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))

    return {node: dist.get(node, -1) for node in range(n)}


def same_network(
    n: int, built_routes: list[tuple[int, int]], queries: list[tuple[int, int]]
) -> list[bool]:
    # Pattern: union-find batch queries -- build once, O(alpha(n)) per
    # query, instead of a fresh traversal per query.
    # Complexity: O((n + e + q) * alpha(n)) time, O(n) space.
    uf = UnionFind(n)
    for a, b in built_routes:
        uf.union(a, b)
    return [uf.connected(a, b) for a, b in queries]
