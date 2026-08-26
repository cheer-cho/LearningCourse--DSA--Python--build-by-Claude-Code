from ex06_dijkstra_delivery import delivery_times, shortest_route


def test_delivery_times_prefers_cheaper_indirect_route():
    edges = [(0, 1, 4), (0, 2, 1), (2, 1, 1)]
    assert delivery_times(3, edges, 0) == {0: 0, 1: 2, 2: 1}


def test_delivery_times_marks_unreachable_as_negative_one():
    edges = [(0, 1, 5)]
    assert delivery_times(3, edges, 0) == {0: 0, 1: 5, 2: -1}


def test_delivery_times_source_maps_to_zero():
    result = delivery_times(1, [], 0)
    assert result == {0: 0}


def test_delivery_times_ignores_more_expensive_direct_edge():
    edges = [(0, 1, 10), (0, 2, 1), (2, 3, 1), (3, 1, 1)]
    result = delivery_times(4, edges, 0)
    assert result[1] == 3


def test_shortest_route_returns_the_cheaper_path():
    edges = [(0, 1, 4), (0, 2, 1), (2, 1, 1)]
    assert shortest_route(3, edges, 0, 1) == [0, 2, 1]


def test_shortest_route_same_node_returns_single_element():
    assert shortest_route(3, [(0, 1, 1)], 1, 1) == [1]


def test_shortest_route_unreachable_returns_none():
    assert shortest_route(2, [], 0, 1) is None


def test_shortest_route_direct_edge_when_it_is_cheapest():
    edges = [(0, 1, 1), (0, 2, 5), (2, 1, 1)]
    assert shortest_route(3, edges, 0, 1) == [0, 1]


def test_delivery_times_large_graph_is_fast():
    # A layered graph: 5_000 layers of 10 nodes each (50_000 nodes),
    # with edges chaining layer i to layer i+1 -- 50_000 edges total.
    # A naive approach re-scanning all edges per relaxation round would
    # be far too slow; a proper heap-based Dijkstra finishes quickly.
    layers = 5_000
    width = 10
    n = layers * width
    edges: list[tuple[int, int, int]] = []
    for layer in range(layers - 1):
        base = layer * width
        next_base = (layer + 1) * width
        for i in range(width):
            edges.append((base + i, next_base + i, 1))
    result = delivery_times(n, edges, 0)
    assert result[0] == 0
    assert result[width] == 1
    assert result[(layers - 1) * width] == layers - 1
    # node 1 (same layer as source, no edge from 0) is unreachable
    assert result[1] == -1
