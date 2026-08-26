# Scenario: a graph library needs to build and convert between the two
# core representations before anything else in this module can work.
# Pattern: adjacency list construction, degree counting, list<->matrix
# conversion. Run: uv run pytest 15-graphs-1 -k ex01


def to_adjacency(n: int, edges: list[tuple[int, int]], directed: bool) -> dict[int, list[int]]:
    """Build an adjacency-list graph over nodes `0..n-1` from an edge
    list. Every node from 0 to n-1 must appear as a key, even isolated
    nodes with no edges (empty list) — later exercises rely on that.

    If `directed` is False, each edge `(a, b)` adds `b` to `a`'s list
    AND `a` to `b`'s list. If `directed` is True, `(a, b)` adds only
    `b` to `a`'s list. Preserve the order edges were given in each
    node's neighbor list (append as you go, no sorting).

    to_adjacency(3, [(0, 1), (1, 2)], directed=False) ->
        {0: [1], 1: [0, 2], 2: [1]}
    to_adjacency(3, [(0, 1)], directed=True) ->
        {0: [1], 1: [], 2: []}
    to_adjacency(1, [], directed=False) -> {0: []}

    Target: O(V + E) time, O(V + E) space.
    """
    raise NotImplementedError


def degrees(adj: dict[int, list[int]]) -> dict[int, int]:
    """Return a dict mapping each node to its degree: the number of
    entries in its neighbor list. (For a directed graph built by
    `to_adjacency`, this is the OUT-degree; for an undirected one,
    it's the plain degree.)

    degrees({0: [1], 1: [0, 2], 2: [1]}) -> {0: 1, 1: 2, 2: 1}
    degrees({0: []}) -> {0: 0}

    Target: O(V + E) time, O(V) space.
    """
    raise NotImplementedError


def matrix_to_list(matrix: list[list[int]]) -> dict[int, list[int]]:
    """Convert an n×n adjacency matrix (`matrix[i][j] == 1` means an
    edge from i to j, 0 means no edge) into an adjacency-list dict.
    Every node 0..n-1 appears as a key. Preserve column order (j
    ascending) within each node's neighbor list.

    matrix_to_list([[0, 1, 0], [0, 0, 1], [0, 0, 0]]) ->
        {0: [1], 1: [2], 2: []}

    Target: O(V^2) time (every cell must be inspected once), O(V + E)
    space for the result.
    """
    raise NotImplementedError


def list_to_matrix(adj: dict[int, list[int]], n: int) -> list[list[int]]:
    """Convert an adjacency-list dict (nodes 0..n-1) into an n×n
    adjacency matrix: `matrix[i][j] == 1` if j is in adj[i]'s
    neighbor list, else 0.

    list_to_matrix({0: [1], 1: [2], 2: []}, 3) ->
        [[0, 1, 0], [0, 0, 1], [0, 0, 0]]

    Target: O(V^2) time, O(V^2) space (the matrix itself).
    """
    raise NotImplementedError
