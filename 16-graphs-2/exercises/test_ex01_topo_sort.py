from ex01_topo_sort import build_order, can_finish


def is_valid_order(order: list[int] | None, n: int, prereqs: list[tuple[int, int]]) -> bool:
    if order is None:
        return False
    if sorted(order) != list(range(n)):
        return False
    position = {node: i for i, node in enumerate(order)}
    return all(position[prereq] < position[course] for course, prereq in prereqs)


def test_build_order_simple_chain_satisfies_constraints():
    prereqs = [(1, 0), (2, 0), (3, 1), (3, 2)]
    assert is_valid_order(build_order(4, prereqs), 4, prereqs)


def test_build_order_no_prereqs_any_order_is_valid():
    order = build_order(3, [])
    assert sorted(order) == [0, 1, 2]


def test_build_order_detects_cycle_returns_none():
    assert build_order(2, [(0, 1), (1, 0)]) is None


def test_build_order_detects_longer_cycle():
    prereqs = [(1, 0), (2, 1), (0, 2)]
    assert build_order(3, prereqs) is None


def test_build_order_single_node_no_edges():
    assert build_order(1, []) == [0]


def test_build_order_disconnected_components_both_included():
    prereqs = [(1, 0), (3, 2)]
    order = build_order(4, prereqs)
    assert is_valid_order(order, 4, prereqs)


def test_can_finish_true_for_dag():
    assert can_finish(4, [(1, 0), (2, 0), (3, 1), (3, 2)]) is True


def test_can_finish_false_for_cycle():
    assert can_finish(2, [(0, 1), (1, 0)]) is False


def test_can_finish_no_prereqs():
    assert can_finish(5, []) is True


def test_build_order_large_chain_is_fast():
    # 50_000-node chain: course i requires course i-1. O(n^2) approaches
    # (e.g. rescanning all edges per step) would be far too slow; Kahn's
    # O(n + e) must finish quickly.
    n = 50_000
    prereqs = [(i, i - 1) for i in range(1, n)]
    order = build_order(n, prereqs)
    assert order == list(range(n))
