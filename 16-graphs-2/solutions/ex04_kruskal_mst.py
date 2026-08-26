from ex02_build_union_find import UnionFind


def min_connection_cost(n: int, weighted_edges: list[tuple[int, int, int]]) -> int | None:
    # Pattern: Kruskal's MST -- sort edges ascending, union-find skips
    # any edge that would close a cycle (never useful in a *minimum*
    # spanning tree, since a cheaper path already connects them).
    # Complexity: O(e log e) time (the sort dominates), O(n) space.
    uf = UnionFind(n)
    total_cost = 0
    edges_used = 0

    for u, v, cost in sorted(weighted_edges, key=lambda edge: edge[2]):
        if uf.union(u, v):
            total_cost += cost
            edges_used += 1
            if edges_used == n - 1:
                break

    return total_cost if edges_used == n - 1 else None
