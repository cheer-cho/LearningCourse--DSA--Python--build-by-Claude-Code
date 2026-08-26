from ex07_histogram_max_rect import largest_rectangle


def test_classic_example():
    assert largest_rectangle([2, 1, 5, 6, 2, 3]) == 10


def test_two_bars():
    assert largest_rectangle([2, 4]) == 4


def test_all_equal_bars():
    assert largest_rectangle([1, 1, 1, 1]) == 4


def test_empty_histogram():
    assert largest_rectangle([]) == 0


def test_single_bar():
    assert largest_rectangle([7]) == 7


def test_strictly_increasing_bars():
    assert largest_rectangle([1, 2, 3, 4, 5]) == 9  # bars 3,4,5: width 3 * height 3


def test_strictly_decreasing_bars():
    assert largest_rectangle([5, 4, 3, 2, 1]) == 9  # bars 5,4,3: width 3 * height 3


def test_single_tall_spike():
    assert largest_rectangle([1, 1, 5, 1, 1]) == 5


def test_large_uniform_histogram_is_fast():
    # Efficiency test: worst case for a naive O(n^2) expand-left/
    # expand-right-per-bar approach — every bar has the same height, so
    # each one would scan the full array. A monotonic stack still
    # finishes in O(n).
    n = 100_000
    heights = [3] * n
    assert largest_rectangle(heights) == 3 * n


def test_large_increasing_histogram_is_fast():
    n = 100_000
    heights = list(range(1, n + 1))
    # Best rectangle: use the last k bars, each >= n - k + 1.
    # Sweeping k from 1..n picks the true maximum of k * (n - k + 1).
    best = max(k * (n - k + 1) for k in range(1, n + 1))
    assert largest_rectangle(heights) == best
