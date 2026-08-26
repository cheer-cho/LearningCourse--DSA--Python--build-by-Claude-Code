from checkpoint_16 import cheapest_grid, fastest_signal, project_order, same_network


def test_project_order_valid_sequence():
    projects = ["wiring", "foundation", "roof"]
    deps = [("wiring", "foundation"), ("roof", "wiring")]
    order = project_order(projects, deps)
    assert order is not None
    position = {name: i for i, name in enumerate(order)}
    assert position["foundation"] < position["wiring"] < position["roof"]
    assert sorted(order) == sorted(projects)


def test_project_order_cycle_returns_none():
    assert project_order(["a", "b"], [("a", "b"), ("b", "a")]) is None


def test_project_order_no_deps_any_order():
    order = project_order(["x", "y", "z"], [])
    assert sorted(order) == ["x", "y", "z"]


def test_cheapest_grid_basic_triangle():
    routes = [(0, 1, 4), (1, 2, 4), (0, 2, 9)]
    assert cheapest_grid(3, routes) == 8


def test_cheapest_grid_disconnected_is_none():
    assert cheapest_grid(3, [(0, 1, 4)]) is None


def test_cheapest_grid_single_district():
    assert cheapest_grid(1, []) == 0


def test_fastest_signal_basic():
    routes = [(0, 1, 4), (1, 2, 4), (0, 2, 9)]
    assert fastest_signal(3, routes, 0) == {0: 0, 1: 4, 2: 8}


def test_fastest_signal_unreachable_district_is_negative_one():
    routes = [(0, 1, 4)]
    assert fastest_signal(3, routes, 0) == {0: 0, 1: 4, 2: -1}


def test_fastest_signal_undirected_reaches_backward_too():
    routes = [(1, 0, 3)]
    assert fastest_signal(2, routes, 0) == {0: 0, 1: 3}


def test_same_network_basic_queries():
    result = same_network(4, [(0, 1), (1, 2)], [(0, 2), (0, 3)])
    assert result == [True, False]


def test_same_network_no_built_routes_nothing_connected():
    result = same_network(3, [], [(0, 1), (1, 2)])
    assert result == [False, False]


def test_same_network_self_query_is_true():
    result = same_network(2, [], [(0, 0)])
    assert result == [True]


def test_same_network_large_batch_is_fast():
    # 50_000 districts, chained cable routes, 50_000 queries -- must
    # answer instantly via union-find rather than a fresh traversal
    # per query.
    n = 50_000
    built_routes = [(i, i + 1) for i in range(n - 1)]
    queries = [(0, i) for i in range(n)]
    result = same_network(n, built_routes, queries)
    assert all(result)
    assert len(result) == n
