from ex07_bipartite_check import is_bipartite


def test_is_bipartite_simple_path_true():
    adj = {0: [1], 1: [0, 2], 2: [1]}
    assert is_bipartite(adj) is True


def test_is_bipartite_triangle_false():
    adj = {0: [1, 2], 1: [0, 2], 2: [0, 1]}
    assert is_bipartite(adj) is False


def test_is_bipartite_disconnected_both_bipartite():
    adj = {0: [1], 1: [0], 2: [3], 3: [2, 4], 4: [3]}
    assert is_bipartite(adj) is True


def test_is_bipartite_disconnected_one_odd_cycle_makes_whole_false():
    # first component is a simple edge (bipartite); second is a
    # triangle (not) -- the trap: stopping after the first component
    # would wrongly report True
    adj = {0: [1], 1: [0], 2: [3, 4], 3: [2, 4], 4: [2, 3]}
    assert is_bipartite(adj) is False


def test_is_bipartite_no_edges_is_trivially_true():
    adj = {0: [], 1: [], 2: []}
    assert is_bipartite(adj) is True


def test_is_bipartite_single_node():
    assert is_bipartite({0: []}) is True


def test_is_bipartite_even_cycle_true():
    adj = {0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [2, 0]}
    assert is_bipartite(adj) is True


def test_is_bipartite_odd_cycle_of_five_false():
    adj = {0: [1, 4], 1: [0, 2], 2: [1, 3], 3: [2, 4], 4: [3, 0]}
    assert is_bipartite(adj) is False


def test_is_bipartite_star_graph_true():
    adj = {0: [1, 2, 3], 1: [0], 2: [0], 3: [0]}
    assert is_bipartite(adj) is True
