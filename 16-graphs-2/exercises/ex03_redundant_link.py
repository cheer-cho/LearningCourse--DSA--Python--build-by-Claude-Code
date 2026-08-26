# Scenario: a cable installer accidentally wired one redundant link
# into what should be a tree-shaped network, and a city planner wants
# to know which regions are already cabled together. Pattern:
# union-find applied to cycle detection and component counting.
# Run: uv run pytest 16-graphs-2 -k ex03


def redundant_connection(edges: list[tuple[int, int]]) -> tuple[int, int]:
    """`edges` describes an undirected graph over nodes `1..n` (n =
    len(edges)) that was originally a tree (n nodes, n-1 edges) and
    then got exactly one extra edge added, creating exactly one cycle.
    Return the extra edge -- specifically, whichever edge in `edges`
    (in input order) is the LAST one that, when added, would close a
    cycle.

    Process edges left to right with a UnionFind(n + 1) (index 0
    unused, nodes are 1-based). For each `(u, v)`, if `u` and `v` are
    already connected, this edge closes a cycle -- return it
    immediately (the first such edge found IS the last one added that
    creates the cycle, since everything before it built a valid tree).
    Otherwise union them and continue.

    redundant_connection([(1, 2), (1, 3), (2, 3)]) -> (2, 3)
    redundant_connection([(1, 2), (2, 3), (3, 4), (1, 4), (1, 5)])
        -> (1, 4)

    Target: O(n * alpha(n)) time, O(n) space.
    """
    raise NotImplementedError


def count_provinces(matrix: list[list[int]]) -> int:
    """`matrix` is an n x n adjacency matrix (`matrix[i][j] == 1` means
    city `i` and city `j` are directly connected; the matrix is
    symmetric and `matrix[i][i] == 1`). A "province" is a maximal
    group of directly-or-indirectly connected cities. Return the
    number of provinces.

    Union every direct connection, then read `component_count()` off
    the UnionFind. (DFS/BFS flood-fill from module 15 solves this too
    -- union-find just avoids the explicit visited-set/recursion and
    reads the answer straight off a counter.)

    count_provinces([[1, 1, 0], [1, 1, 0], [0, 0, 1]]) -> 2
    count_provinces([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) -> 3

    Target: O(n^2 * alpha(n)) time (n^2 to read the matrix), O(n) space.
    """
    raise NotImplementedError
