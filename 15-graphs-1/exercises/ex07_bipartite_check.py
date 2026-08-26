# Scenario: can a company's users be split into two teams so that no
# two users who must directly collaborate (an edge) end up on the same
# team? Pattern: BFS 2-coloring, disconnected-graph handling.
# Run: uv run pytest 15-graphs-1 -k ex07


def is_bipartite(adj: dict[int, list[int]]) -> bool:
    """Return True if the UNDIRECTED graph `adj` is bipartite: its
    nodes can be split into two groups such that every edge connects
    a node in one group to a node in the OTHER group (no edge has
    both endpoints in the same group). `adj` follows ex01's
    convention: every node is a key, including isolated ones.

    Use BFS 2-coloring: color the start node of each unvisited
    component color 0, every neighbor the OPPOSITE color of the
    current node, and every neighbor already colored the SAME as the
    current node means the graph is NOT bipartite (an edge landed
    inside one group). Remember to check every component — a graph
    with several disconnected pieces is bipartite only if EVERY piece
    is (the trap: testing just the first component and returning
    early gives a false positive).

    is_bipartite({0: [1], 1: [0, 2], 2: [1]}) -> True
        (group A = {0, 2}, group B = {1})
    is_bipartite({0: [1, 2], 1: [0, 2], 2: [0, 1]}) -> False
        (a triangle/odd cycle can never be 2-colored)
    is_bipartite({0: [1], 1: [0], 2: [3], 3: [2, 4], 4: [3]}) -> True
        (two disconnected components, each individually bipartite)

    Target: O(V + E) time, O(V) space.
    """
    raise NotImplementedError
