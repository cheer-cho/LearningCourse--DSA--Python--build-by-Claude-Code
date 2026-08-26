from ex03_redundant_link import count_provinces, redundant_connection


def test_redundant_connection_simple_triangle():
    assert redundant_connection([(1, 2), (1, 3), (2, 3)]) == (2, 3)


def test_redundant_connection_returns_the_last_cycle_closing_edge():
    edges = [(1, 2), (2, 3), (3, 4), (1, 4), (1, 5)]
    assert redundant_connection(edges) == (1, 4)


def test_redundant_connection_cycle_at_the_end():
    edges = [(1, 2), (2, 3), (3, 1)]
    assert redundant_connection(edges) == (3, 1)


def test_redundant_connection_larger_tree_plus_one_edge():
    edges = [(1, 2), (1, 3), (1, 4), (4, 5), (2, 5)]
    assert redundant_connection(edges) == (2, 5)


def test_count_provinces_two_groups():
    matrix = [
        [1, 1, 0],
        [1, 1, 0],
        [0, 0, 1],
    ]
    assert count_provinces(matrix) == 2


def test_count_provinces_all_isolated():
    matrix = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
    ]
    assert count_provinces(matrix) == 3


def test_count_provinces_all_connected():
    matrix = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1],
    ]
    assert count_provinces(matrix) == 1


def test_count_provinces_chain_is_one_province():
    matrix = [
        [1, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 1, 1],
        [0, 0, 1, 1],
    ]
    assert count_provinces(matrix) == 1


def test_count_provinces_single_city():
    assert count_provinces([[1]]) == 1
