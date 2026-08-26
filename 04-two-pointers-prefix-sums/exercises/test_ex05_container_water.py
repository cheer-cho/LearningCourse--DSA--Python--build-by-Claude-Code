from ex05_container_water import max_container


def test_max_container_typical():
    assert max_container([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49


def test_max_container_two_elements():
    assert max_container([1, 1]) == 1


def test_max_container_all_same_height():
    assert max_container([4, 4, 4, 4]) == 12


def test_max_container_decreasing_heights():
    assert max_container([5, 4, 3, 2, 1]) == 6


def test_max_container_increasing_heights():
    assert max_container([1, 2, 3, 4, 5]) == 6


def test_max_container_tall_walls_beat_wide_short_ones():
    # The two 9-height walls (indices 1 and 6) beat the wider but
    # shorter pair at the very ends (indices 0 and 7, height 1 each).
    assert max_container([1, 9, 1, 1, 1, 1, 9, 1]) == 45


def test_max_container_efficiency_on_large_input():
    n = 200_000
    heights = [5] * n
    # Constant height -> the best pair is always the two ends.
    # An O(n^2) scan of every pair would be far too slow at this size.
    assert max_container(heights) == 5 * (n - 1)
