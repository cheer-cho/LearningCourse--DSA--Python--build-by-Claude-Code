import random

from ex04_k_closest_points import k_closest


def _dist_sq(p: tuple[int, int]) -> int:
    return p[0] * p[0] + p[1] * p[1]


def test_k_closest_typical():
    points = [(1, 1), (3, 3), (0, 1)]
    result = k_closest(points, 2)
    assert set(result) == {(1, 1), (0, 1)}


def test_k_closest_k_equals_len_returns_everything():
    points = [(1, 0), (0, 2), (-1, -1)]
    result = k_closest(points, 3)
    assert set(result) == set(points)


def test_k_closest_k_one_returns_nearest_single_point():
    points = [(5, 5), (0, 1), (2, 2)]
    result = k_closest(points, 1)
    assert result == [(0, 1)]


def test_k_closest_includes_origin_point():
    points = [(0, 0), (10, 10), (1, 1)]
    result = k_closest(points, 1)
    assert result == [(0, 0)]


def test_k_closest_negative_coordinates():
    points = [(-3, -4), (1, 1), (-1, 0)]
    result = k_closest(points, 2)
    assert set(result) == {(-1, 0), (1, 1)}


def test_k_closest_large_input_matches_smallest_distances():
    rng = random.Random(4)
    points = [(rng.randint(-500, 500), rng.randint(-500, 500)) for _ in range(2_000)]
    k = 25
    result = k_closest(points, k)
    assert len(result) == k

    # Any valid k-closest selection has the same sorted DISTANCES as the
    # first k of the globally sorted distances, even if ties mean the
    # exact points chosen could differ.
    all_dists_sorted = sorted(_dist_sq(p) for p in points)
    result_dists_sorted = sorted(_dist_sq(p) for p in result)
    assert result_dists_sorted == all_dists_sorted[:k]
