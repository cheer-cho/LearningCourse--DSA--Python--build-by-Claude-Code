from ex02_build_union_find import UnionFind


def redundant_connection(edges: list[tuple[int, int]]) -> tuple[int, int]:
    # Pattern: union-find cycle detection. Why: a tree plus one extra
    # edge has exactly one cycle; the extra edge is the first one
    # (scanning left to right) whose two endpoints are ALREADY
    # connected before it's added.
    # Complexity: O(n * alpha(n)) time, O(n) space.
    n = len(edges)
    uf = UnionFind(n + 1)  # nodes are 1-based; index 0 unused
    for u, v in edges:
        if not uf.union(u, v):
            return (u, v)
    raise ValueError("no redundant edge found -- input wasn't a tree + 1 edge")


def count_provinces(matrix: list[list[int]]) -> int:
    # Pattern: union-find as a component counter -- union every direct
    # connection, then read the group count straight off the counter
    # instead of a DFS/BFS visited-set sweep.
    # Complexity: O(n^2 * alpha(n)) time, O(n) space.
    n = len(matrix)
    uf = UnionFind(n)
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] == 1:
                uf.union(i, j)
    return uf.component_count()
