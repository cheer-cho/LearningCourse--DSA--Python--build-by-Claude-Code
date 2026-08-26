import math

from ex02_count_ops import all_pairs, halve_down, sum_all


class _Counter:
    def __init__(self) -> None:
        self.count = 0

    def tick(self) -> None:
        self.count += 1


def test_sum_all_returns_the_sum():
    counter = _Counter()
    assert sum_all([1, 2, 3, 4, 5], counter.tick) == 15


def test_sum_all_ticks_once_per_element():
    counter = _Counter()
    sum_all([1, 2, 3, 4, 5], counter.tick)
    assert counter.count == 5


def test_sum_all_empty_ticks_zero_times():
    counter = _Counter()
    assert sum_all([], counter.tick) == 0
    assert counter.count == 0


def test_sum_all_ticks_scale_linearly_with_size():
    small = _Counter()
    sum_all(list(range(10)), small.tick)
    large = _Counter()
    sum_all(list(range(1000)), large.tick)
    assert small.count == 10
    assert large.count == 1000
    assert large.count / small.count == 100  # 100x the input -> 100x the ticks


def test_all_pairs_returns_every_ordered_pair():
    counter = _Counter()
    assert all_pairs([1, 2], counter.tick) == [(1, 1), (1, 2), (2, 1), (2, 2)]


def test_all_pairs_ticks_n_squared_times():
    for n in (1, 3, 5, 10):
        counter = _Counter()
        items = list(range(n))
        result = all_pairs(items, counter.tick)
        assert counter.count == n * n
        assert len(result) == n * n


def test_all_pairs_ticks_scale_quadratically_with_size():
    small = _Counter()
    all_pairs(list(range(10)), small.tick)
    large = _Counter()
    all_pairs(list(range(100)), large.tick)
    assert small.count == 100
    assert large.count == 10_000
    assert large.count / small.count == 100  # (100/10)^2 = 100, not 10


def test_halve_down_matches_the_log_formula():
    for n in (1, 2, 3, 4, 8, 16, 17, 100, 1023, 1024):
        counter = _Counter()
        halve_down(n, counter.tick)
        assert counter.count == math.floor(math.log2(n)) + 1


def test_halve_down_zero_ticks_zero_times():
    counter = _Counter()
    assert halve_down(0, counter.tick) == 0
    assert counter.count == 0


def test_halve_down_ticks_scale_logarithmically_with_size():
    small = _Counter()
    halve_down(1024, small.tick)
    large = _Counter()
    halve_down(1024 * 1024, large.tick)
    assert small.count == 11
    assert large.count == 21
    # n grew 1024x, but ticks only grew by 10 -- that's O(log n) in action.
    assert large.count - small.count == 10
