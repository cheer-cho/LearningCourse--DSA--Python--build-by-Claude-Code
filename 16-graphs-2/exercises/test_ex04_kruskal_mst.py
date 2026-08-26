from ex04_kruskal_mst import min_connection_cost


def test_min_connection_cost_skips_the_expensive_cycle_edge():
    edges = [(0, 1, 1), (1, 2, 2), (2, 3, 3), (0, 3, 10)]
    assert min_connection_cost(4, edges) == 6


def test_min_connection_cost_disconnected_graph_returns_none():
    edges = [(0, 1, 1), (2, 3, 1)]
    assert min_connection_cost(4, edges) is None


def test_min_connection_cost_duplicate_weight_cheaper_edge_wins():
    edges = [(0, 1, 5), (0, 1, 2), (1, 2, 1)]
    assert min_connection_cost(3, edges) == 3


def test_min_connection_cost_single_node_no_edges_needed():
    assert min_connection_cost(1, []) == 0


def test_min_connection_cost_already_a_tree():
    edges = [(0, 1, 4), (1, 2, 4), (2, 3, 4)]
    assert min_connection_cost(4, edges) == 12


def test_min_connection_cost_no_edges_multiple_nodes_is_none():
    assert min_connection_cost(3, []) is None


def test_min_connection_cost_picks_cheapest_across_redundant_paths():
    # Two ways to connect everything: a cheap path (1+1+1=3) and a
    # direct expensive shortcut (100) that would only close a cycle.
    edges = [(0, 1, 1), (1, 2, 1), (2, 3, 1), (0, 3, 100), (0, 2, 50)]
    assert min_connection_cost(4, edges) == 3
