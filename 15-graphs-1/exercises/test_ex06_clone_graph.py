from ex06_clone_graph import Node, clone_graph


def build_triangle() -> tuple[Node, Node, Node]:
    """1 - 2 - 3 - 1 (a 3-cycle)."""
    n1, n2, n3 = Node(1), Node(2), Node(3)
    n1.neighbors = [n2, n3]
    n2.neighbors = [n1, n3]
    n3.neighbors = [n1, n2]
    return n1, n2, n3


def collect_vals(start: Node) -> set[int]:
    visited: set[int] = set()
    seen_nodes: set[int] = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if id(node) in seen_nodes:
            continue
        seen_nodes.add(id(node))
        visited.add(node.val)
        stack.extend(node.neighbors)
    return visited


def test_clone_graph_none_input():
    assert clone_graph(None) is None


def test_clone_graph_single_node_no_neighbors():
    original = Node(1)
    clone = clone_graph(original)
    assert clone is not original
    assert clone.val == 1
    assert clone.neighbors == []


def test_clone_graph_preserves_values():
    n1, _, _ = build_triangle()
    clone = clone_graph(n1)
    assert collect_vals(clone) == {1, 2, 3}


def test_clone_graph_produces_independent_nodes():
    n1, n2, n3 = build_triangle()
    clone = clone_graph(n1)

    originals = {id(n1), id(n2), id(n3)}
    clones_seen: set[int] = set()
    stack = [clone]
    while stack:
        node = stack.pop()
        if id(node) in clones_seen:
            continue
        clones_seen.add(id(node))
        assert id(node) not in originals  # every clone is a NEW object
        stack.extend(node.neighbors)


def test_clone_graph_mutating_clone_does_not_touch_original():
    n1, _, _ = build_triangle()
    clone = clone_graph(n1)
    clone.val = 999
    clone.neighbors = []
    assert n1.val == 1
    assert len(n1.neighbors) == 2


def test_clone_graph_shared_neighbor_stays_shared_in_clone():
    # 1 -> 2, 1 -> 3, 2 -> 3 (both 1 and 2 point at 3): the clone of 3
    # reached via clone-of-1 and via clone-of-2 must be the SAME object.
    n1, n2, n3 = Node(1), Node(2), Node(3)
    n1.neighbors = [n2, n3]
    n2.neighbors = [n3]
    clone1 = clone_graph(n1)
    clone2 = next(n for n in clone1.neighbors if n.val == 2)
    clone3_via_1 = next(n for n in clone1.neighbors if n.val == 3)
    clone3_via_2 = next(n for n in clone2.neighbors if n.val == 3)
    assert clone3_via_1 is clone3_via_2


def test_clone_graph_handles_cycle_without_infinite_recursion():
    n1, _, _ = build_triangle()
    clone = clone_graph(n1)
    # each cloned node should have exactly 2 neighbors, same as original
    seen: set[int] = set()
    stack = [clone]
    while stack:
        node = stack.pop()
        if id(node) in seen:
            continue
        seen.add(id(node))
        assert len(node.neighbors) == 2
        stack.extend(node.neighbors)
    assert len(seen) == 3
