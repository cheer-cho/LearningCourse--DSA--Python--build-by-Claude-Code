class Node:
    def __init__(self, val: int, neighbors: list["Node"] | None = None) -> None:
        self.val = val
        self.neighbors: list[Node] = neighbors if neighbors is not None else []


def clone_graph(node: "Node | None") -> "Node | None":
    # Pattern: DFS + hash map (original node -> cloned node). The map
    # is what makes cycles safe: before recursing into a neighbor,
    # check whether it's already been cloned and reuse that clone
    # instead of recursing again (which would loop forever on a cycle)
    # or making a duplicate (which would break shared-neighbor shape).
    # Complexity: O(V + E) time, O(V) space.
    if node is None:
        return None

    clones: dict[Node, Node] = {}

    def dfs(original: Node) -> Node:
        if original in clones:
            return clones[original]
        copy = Node(original.val)
        clones[original] = copy
        copy.neighbors = [dfs(neighbor) for neighbor in original.neighbors]
        return copy

    return dfs(node)
