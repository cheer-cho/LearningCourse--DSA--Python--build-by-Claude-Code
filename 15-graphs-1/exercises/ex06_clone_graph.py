# Scenario: a save-game system needs a true deep copy of a connected
# level graph — mutating the clone must never touch the original.
# Pattern: DFS/BFS + hash map (old node -> new node) to handle cycles.
# Run: uv run pytest 15-graphs-1 -k ex06


class Node:
    """A graph node with a value and a list of neighbor nodes. This
    class is complete — nothing to implement here. Neighbors can form
    cycles (the graph is undirected: if A is in B's neighbor list, B
    is in A's neighbor list too), which is exactly why a naive
    recursive copy without bookkeeping would recurse forever.
    """

    def __init__(self, val: int, neighbors: list["Node"] | None = None) -> None:
        self.val = val
        self.neighbors: list[Node] = neighbors if neighbors is not None else []


def clone_graph(node: "Node | None") -> "Node | None":
    """Return a deep copy of the connected graph reachable from
    `node`: every node reachable from `node` gets its own new `Node`
    object (same `.val`, independently mutable `.neighbors` list), and
    the copy's edges mirror the original's exactly. `None` in ->
    `None` out (empty graph).

    Use a hash map from ORIGINAL node -> CLONED node, built as you
    DFS/BFS the original graph. Before recursing/enqueuing into a
    neighbor, check the map first: if that original node was already
    cloned, reuse the existing clone instead of making a new one —
    this is what correctly handles cycles (without it, a cycle sends
    the clone into infinite recursion) AND keeps the clone's shape
    identical to the original (two nodes that both point to the same
    neighbor in the original must both point to the SAME cloned
    neighbor, not two different copies of it).

    Target: O(V + E) time, O(V) space (the map, plus recursion/queue).
    """
    raise NotImplementedError
