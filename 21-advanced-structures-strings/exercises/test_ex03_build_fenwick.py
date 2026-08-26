import random

from ex03_build_fenwick import Fenwick, count_smaller_after


def test_fenwick_starts_at_zero():
    fw = Fenwick(5)
    assert fw.prefix_sum(4) == 0


def test_fenwick_add_and_prefix_sum():
    fw = Fenwick(5)
    fw.add(0, 3)
    fw.add(2, 4)
    assert fw.prefix_sum(1) == 3
    assert fw.prefix_sum(2) == 7
    assert fw.prefix_sum(4) == 7


def test_fenwick_prefix_sum_of_empty_prefix():
    fw = Fenwick(5)
    fw.add(0, 10)
    assert fw.prefix_sum(-1) == 0


def test_fenwick_range_sum():
    fw = Fenwick(5)
    fw.add(0, 3)
    fw.add(2, 4)
    fw.add(4, 1)
    assert fw.range_sum(1, 4) == 5
    assert fw.range_sum(0, 4) == 8
    assert fw.range_sum(2, 2) == 4


def test_fenwick_multiple_adds_same_index_accumulate():
    fw = Fenwick(3)
    fw.add(1, 5)
    fw.add(1, -2)
    assert fw.prefix_sum(1) == 3


def test_fenwick_single_slot():
    fw = Fenwick(1)
    fw.add(0, 9)
    assert fw.range_sum(0, 0) == 9


def test_fenwick_matches_brute_force_random():
    n = 200
    fw = Fenwick(n)
    reference = [0] * n
    rng = random.Random(42)

    for _ in range(500):
        idx = rng.randrange(n)
        delta = rng.randint(-10, 10)
        fw.add(idx, delta)
        reference[idx] += delta

    for _ in range(50):
        i = rng.randrange(n)
        j = rng.randrange(i, n)
        assert fw.range_sum(i, j) == sum(reference[i : j + 1])


def test_count_smaller_after_typical():
    assert count_smaller_after([5, 2, 6, 1]) == [2, 1, 1, 0]


def test_count_smaller_after_empty():
    assert count_smaller_after([]) == []


def test_count_smaller_after_all_equal():
    assert count_smaller_after([1, 1, 1]) == [0, 0, 0]


def test_count_smaller_after_single_element():
    assert count_smaller_after([42]) == [0]


def test_count_smaller_after_sorted_descending():
    assert count_smaller_after([4, 3, 2, 1]) == [3, 2, 1, 0]


def test_count_smaller_after_sorted_ascending():
    assert count_smaller_after([1, 2, 3, 4]) == [0, 0, 0, 0]


def test_count_smaller_after_negative_values():
    assert count_smaller_after([-1, -5, 2, -3]) == [2, 0, 1, 0]


def test_count_smaller_after_matches_brute_force():
    rng = random.Random(7)
    nums = [rng.randint(-20, 20) for _ in range(150)]
    expected = [
        sum(1 for later in nums[i + 1 :] if later < nums[i]) for i in range(len(nums))
    ]
    assert count_smaller_after(nums) == expected


def test_fenwick_efficiency_large_input():
    # n = 100,000 point updates + prefix queries. A naive "recompute
    # the prefix sum from scratch" approach is O(n) per query here --
    # infeasible at this scale. A real Fenwick tree is instant.
    n = 100_000
    fw = Fenwick(n)
    for i in range(n):
        fw.add(i, 1)
    assert fw.prefix_sum(n - 1) == n
    assert fw.range_sum(0, n - 1) == n
    assert fw.range_sum(n // 2, n - 1) == n - n // 2


def test_count_smaller_after_efficiency_large_input():
    # Strictly descending array of 50,000 elements: every element has
    # ALL later elements smaller than it, giving a clean closed-form
    # expected answer without an O(n^2) reference computation.
    n = 50_000
    nums = list(range(n, 0, -1))
    result = count_smaller_after(nums)
    assert result == list(range(n - 1, -1, -1))
