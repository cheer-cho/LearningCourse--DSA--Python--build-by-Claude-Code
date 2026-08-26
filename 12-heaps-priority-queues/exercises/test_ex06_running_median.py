import random
import statistics

import pytest
from ex06_running_median import MedianFinder


def test_median_before_any_add_raises():
    mf = MedianFinder()
    with pytest.raises(ValueError):
        mf.median()


def test_median_single_value():
    mf = MedianFinder()
    mf.add(5)
    assert mf.median() == 5.0


def test_median_two_values_averages():
    mf = MedianFinder()
    mf.add(1)
    mf.add(2)
    assert mf.median() == 1.5


def test_median_worked_example():
    mf = MedianFinder()
    for val in [5, 1, 3]:
        mf.add(val)
    assert mf.median() == 3.0


def test_median_updates_as_stream_grows():
    mf = MedianFinder()
    expected = []
    for val in [10, 2, 8, 4, 6]:
        mf.add(val)
        expected.append(val)
        assert mf.median() == statistics.median(expected)


def test_median_handles_duplicates():
    mf = MedianFinder()
    for val in [4, 4, 4, 4]:
        mf.add(val)
    assert mf.median() == 4.0


def test_median_handles_negatives():
    mf = MedianFinder()
    for val in [-5, -1, -10, 3]:
        mf.add(val)
    assert mf.median() == statistics.median([-5, -1, -10, 3])


def test_median_matches_brute_force_over_many_adds():
    rng = random.Random(17)
    mf = MedianFinder()
    seen: list[int] = []
    for _ in range(500):
        val = rng.randint(-1_000, 1_000)
        mf.add(val)
        seen.append(val)
        assert mf.median() == statistics.median(seen)


def test_median_large_stream_with_interleaved_queries():
    rng = random.Random(23)
    mf = MedianFinder()
    last_median = None
    for i in range(100_000):
        mf.add(rng.randint(-10**6, 10**6))
        if i % 10_000 == 0:
            last_median = mf.median()
    assert last_median is not None
    assert isinstance(mf.median(), float)
