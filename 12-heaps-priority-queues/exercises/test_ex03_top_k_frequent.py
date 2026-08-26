import random
from collections import Counter

from ex03_top_k_frequent import top_k_frequent


def test_top_k_frequent_typical():
    result = top_k_frequent([1, 1, 1, 2, 2, 3], 2)
    assert set(result) == {1, 2}
    assert len(result) == 2


def test_top_k_frequent_k_equals_all_distinct():
    result = top_k_frequent([4, 4, 5, 6, 6, 6], 3)
    assert set(result) == {4, 5, 6}


def test_top_k_frequent_single_value():
    assert top_k_frequent([5], 1) == [5]


def test_top_k_frequent_k_one_returns_most_frequent():
    result = top_k_frequent([7, 7, 7, 8, 9], 1)
    assert result == [7]


def test_top_k_frequent_all_equal_frequency():
    result = top_k_frequent([1, 2, 3], 2)
    assert set(result).issubset({1, 2, 3})
    assert len(result) == 2


def test_top_k_frequent_negatives():
    result = top_k_frequent([-1, -1, -2, -3, -3, -3], 2)
    assert set(result) == {-3, -1}


def test_top_k_frequent_large_input():
    rng = random.Random(11)
    # A handful of "hot" values (~400 occurrences each) buried in a sea
    # of 200_000 "cold" tail values (~5 occurrences each) -- no
    # plausible tie between a hot and a cold value, so the answer set
    # is deterministic even though internal tie-breaking isn't.
    hot_values = set(range(10))
    nums = [rng.choice(list(hot_values)) for _ in range(4_000)]
    nums += [rng.randint(10_000, 60_000) for _ in range(196_000)]
    rng.shuffle(nums)

    counts = Counter(nums)
    assert min(counts[v] for v in hot_values) > max(
        (c for val, c in counts.items() if val not in hot_values), default=0
    )

    result = top_k_frequent(nums, 10)
    assert len(result) == 10
    assert set(result) == hot_values
