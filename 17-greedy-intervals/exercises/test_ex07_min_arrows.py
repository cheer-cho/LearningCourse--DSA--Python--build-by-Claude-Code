from ex07_min_arrows import min_arrows


def test_min_arrows_typical():
    assert min_arrows([[1, 6], [2, 8], [7, 12], [10, 16]]) == 2


def test_min_arrows_touching_counts_as_hit():
    assert min_arrows([[1, 2], [2, 3], [3, 4]]) == 2


def test_min_arrows_empty():
    assert min_arrows([]) == 0


def test_min_arrows_single_balloon():
    assert min_arrows([[3, 9]]) == 1


def test_min_arrows_all_overlapping_needs_one():
    assert min_arrows([[1, 10], [2, 8], [3, 6]]) == 1


def test_min_arrows_none_touching_needs_one_each():
    assert min_arrows([[1, 2], [4, 5], [7, 8]]) == 3


def test_min_arrows_unsorted_input():
    assert min_arrows([[10, 16], [1, 6], [7, 12], [2, 8]]) == 2


def test_min_arrows_efficiency_large_input():
    n = 100_000
    balloons = [[i, i] for i in range(n)]  # every balloon a distinct point
    assert min_arrows(balloons) == n
