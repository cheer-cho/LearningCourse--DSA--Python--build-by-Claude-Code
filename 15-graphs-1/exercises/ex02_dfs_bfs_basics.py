# Scenario: the fundamental "what can I reach, and in what order" ops
# every later exercise builds on. Pattern: DFS, BFS, visited-set
# discipline. Run: uv run pytest 15-graphs-1 -k ex02


def reachable(adj: dict[int, list[int]], start: int) -> set[int]:
    """Return the set of every node reachable from `start`, including
    `start` itself. DFS or BFS both work — either is fine (this
    doesn't care about order, only the final set).

    reachable({0: [1], 1: [0, 2], 2: [1], 3: []}, 0) -> {0, 1, 2}
    reachable({0: []}, 0) -> {0}

    Target: O(V + E) time, O(V) space.
    """
    raise NotImplementedError


def bfs_order(adj: dict[int, list[int]], start: int) -> list[int]:
    """Return the nodes reachable from `start`, in BFS visit order
    (the order they were DEQUEUED). Tie-break: when a node has
    multiple neighbors, visit them in the order they appear in that
    node's adjacency list. Mark a node visited the moment it's
    enqueued, not when it's dequeued (see LESSON.md gotchas — this
    matters for correctness, not just style).

    bfs_order({0: [1, 2], 1: [0, 3], 2: [0], 3: [1]}, 0) ->
        [0, 1, 2, 3]

    Target: O(V + E) time, O(V) space.
    """
    raise NotImplementedError


def connected_components(adj: dict[int, list[int]]) -> int:
    """Return the number of connected components in an UNDIRECTED
    graph given as an adjacency list (every node in `adj` is a key,
    per ex01's convention, including isolated nodes). Loop over every
    node; start a fresh traversal from each unvisited one.

    connected_components({0: [1], 1: [0], 2: [3], 3: [2], 4: []}) -> 3
    connected_components({0: [], 1: [], 2: []}) -> 3

    Target: O(V + E) time, O(V) space.
    """
    raise NotImplementedError


def path_exists(adj: dict[int, list[int]], a: int, b: int) -> bool:
    """Return True if there's a path from `a` to `b` (in either
    direction the adjacency list allows — for a directed graph this
    respects edge direction). `a == b` is always True (a node reaches
    itself trivially).

    path_exists({0: [1], 1: [2], 2: []}, 0, 2) -> True
    path_exists({0: [1], 1: [], 2: []}, 0, 2) -> False
    path_exists({0: []}, 0, 0) -> True

    Target: O(V + E) time, O(V) space.
    """
    raise NotImplementedError
