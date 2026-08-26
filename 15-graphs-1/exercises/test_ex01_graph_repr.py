from ex01_graph_repr import degrees, list_to_matrix, matrix_to_list, to_adjacency


def test_to_adjacency_undirected_basic():
    adj = to_adjacency(3, [(0, 1), (1, 2)], directed=False)
    assert adj == {0: [1], 1: [0, 2], 2: [1]}


def test_to_adjacency_directed_basic():
    adj = to_adjacency(3, [(0, 1)], directed=True)
    assert adj == {0: [1], 1: [], 2: []}


def test_to_adjacency_isolated_node_present_with_empty_list():
    adj = to_adjacency(1, [], directed=False)
    assert adj == {0: []}


def test_to_adjacency_includes_every_node_even_with_no_edges():
    adj = to_adjacency(4, [(0, 1)], directed=True)
    assert set(adj.keys()) == {0, 1, 2, 3}
    assert adj[2] == []
    assert adj[3] == []


def test_to_adjacency_undirected_self_loop():
    adj = to_adjacency(2, [(0, 0)], directed=False)
    # a self loop should appear (twice, since undirected adds both directions)
    assert adj[0].count(0) == 2


def test_to_adjacency_preserves_edge_order():
    adj = to_adjacency(3, [(0, 2), (0, 1)], directed=True)
    assert adj[0] == [2, 1]


def test_degrees_basic():
    adj = {0: [1], 1: [0, 2], 2: [1]}
    assert degrees(adj) == {0: 1, 1: 2, 2: 1}


def test_degrees_isolated_node_is_zero():
    assert degrees({0: []}) == {0: 0}


def test_degrees_directed_counts_out_degree_only():
    adj = {0: [1], 1: [], 2: []}
    assert degrees(adj) == {0: 1, 1: 0, 2: 0}


def test_matrix_to_list_basic():
    matrix = [
        [0, 1, 0],
        [0, 0, 1],
        [0, 0, 0],
    ]
    assert matrix_to_list(matrix) == {0: [1], 1: [2], 2: []}


def test_matrix_to_list_undirected_matrix_is_symmetric_result():
    matrix = [
        [0, 1],
        [1, 0],
    ]
    adj = matrix_to_list(matrix)
    assert adj == {0: [1], 1: [0]}


def test_matrix_to_list_no_edges():
    matrix = [[0, 0], [0, 0]]
    assert matrix_to_list(matrix) == {0: [], 1: []}


def test_list_to_matrix_basic():
    adj = {0: [1], 1: [2], 2: []}
    assert list_to_matrix(adj, 3) == [
        [0, 1, 0],
        [0, 0, 1],
        [0, 0, 0],
    ]


def test_list_to_matrix_no_edges():
    adj = {0: [], 1: []}
    assert list_to_matrix(adj, 2) == [[0, 0], [0, 0]]


def test_matrix_to_list_and_back_round_trip():
    matrix = [
        [0, 1, 1],
        [1, 0, 0],
        [1, 0, 0],
    ]
    adj = matrix_to_list(matrix)
    assert list_to_matrix(adj, 3) == matrix
