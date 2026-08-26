from ex02_dfs_bfs_basics import bfs_order, connected_components, path_exists, reachable


def test_reachable_basic():
    adj = {0: [1], 1: [0, 2], 2: [1], 3: []}
    assert reachable(adj, 0) == {0, 1, 2}


def test_reachable_single_node_no_edges():
    assert reachable({0: []}, 0) == {0}


def test_reachable_directed_respects_direction():
    adj = {0: [1], 1: [], 2: [0]}
    assert reachable(adj, 0) == {0, 1}


def test_reachable_full_cycle_all_nodes():
    adj = {0: [1], 1: [2], 2: [0]}
    assert reachable(adj, 0) == {0, 1, 2}


def test_bfs_order_basic():
    adj = {0: [1, 2], 1: [0, 3], 2: [0], 3: [1]}
    assert bfs_order(adj, 0) == [0, 1, 2, 3]


def test_bfs_order_tie_break_uses_adjacency_list_order():
    adj = {0: [2, 1], 1: [0], 2: [0]}
    assert bfs_order(adj, 0) == [0, 2, 1]


def test_bfs_order_single_node():
    assert bfs_order({0: []}, 0) == [0]


def test_bfs_order_does_not_revisit_in_cycle():
    adj = {0: [1], 1: [2], 2: [0]}
    order = bfs_order(adj, 0)
    assert order == [0, 1, 2]
    assert len(order) == len(set(order))


def test_bfs_order_diamond_shape():
    # 0 -> 1, 0 -> 2, 1 -> 3, 2 -> 3: node 3 must appear exactly once,
    # not twice (once via 1, once via 2) if visited-on-enqueue is done right
    adj = {0: [1, 2], 1: [3], 2: [3], 3: []}
    order = bfs_order(adj, 0)
    assert order.count(3) == 1
    assert order[:3] == [0, 1, 2]


def test_connected_components_basic():
    adj = {0: [1], 1: [0], 2: [3], 3: [2], 4: []}
    assert connected_components(adj) == 3


def test_connected_components_all_isolated():
    assert connected_components({0: [], 1: [], 2: []}) == 3


def test_connected_components_single_component():
    adj = {0: [1], 1: [0, 2], 2: [1]}
    assert connected_components(adj) == 1


def test_connected_components_empty_graph():
    assert connected_components({}) == 0


def test_path_exists_true():
    adj = {0: [1], 1: [2], 2: []}
    assert path_exists(adj, 0, 2) is True


def test_path_exists_false_directed():
    adj = {0: [1], 1: [], 2: []}
    assert path_exists(adj, 0, 2) is False


def test_path_exists_self_is_always_true():
    assert path_exists({0: []}, 0, 0) is True


def test_path_exists_reverse_direction_fails_when_directed():
    adj = {0: [1], 1: []}
    assert path_exists(adj, 1, 0) is False
