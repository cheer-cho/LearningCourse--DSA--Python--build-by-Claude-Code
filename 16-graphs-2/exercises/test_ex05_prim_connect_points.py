from ex05_prim_connect_points import min_cost_connect_points


def test_min_cost_connect_points_classic_example():
    points = [(0, 0), (2, 2), (3, 10), (5, 2), (7, 0)]
    assert min_cost_connect_points(points) == 20


def test_min_cost_connect_points_single_point_costs_zero():
    assert min_cost_connect_points([(5, 5)]) == 0


def test_min_cost_connect_points_two_points_is_their_distance():
    assert min_cost_connect_points([(0, 0), (3, 4)]) == 7


def test_min_cost_connect_points_collinear_points():
    points = [(0, 0), (1, 0), (2, 0), (3, 0)]
    assert min_cost_connect_points(points) == 3


def test_min_cost_connect_points_duplicate_points_cost_zero_between_them():
    points = [(1, 1), (1, 1), (5, 5)]
    assert min_cost_connect_points(points) == 8


def test_min_cost_connect_points_moderate_grid_completes_quickly():
    # A 15x15 grid of points (225 points, ~25k implicit edges). Not
    # huge, but big enough that an approach exploring every edge pair
    # without any pruning noticeably slows down; Prim with a heap
    # should still be fast.
    points = [(x, y) for x in range(15) for y in range(15)]
    cost = min_cost_connect_points(points)
    # A minimum spanning tree over an m x m unit grid costs exactly
    # m*m - 1 (connect every point to an orthogonal neighbor at distance 1).
    assert cost == 15 * 15 - 1
