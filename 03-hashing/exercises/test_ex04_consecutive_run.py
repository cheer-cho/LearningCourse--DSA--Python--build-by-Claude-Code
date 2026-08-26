import random

from ex04_consecutive_run import longest_consecutive


def test_longest_consecutive_typical():
    assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4


def test_longest_consecutive_with_duplicate():
    assert longest_consecutive([1, 2, 0, 1]) == 3


def test_longest_consecutive_empty_list():
    assert longest_consecutive([]) == 0


def test_longest_consecutive_single_element():
    assert longest_consecutive([42]) == 1


def test_longest_consecutive_all_same_element():
    assert longest_consecutive([5, 5, 5, 5]) == 1


def test_longest_consecutive_no_run_all_isolated():
    assert longest_consecutive([10, 30, 50]) == 1


def test_longest_consecutive_negative_numbers():
    assert longest_consecutive([-3, -2, -1, 0, 1]) == 5


def test_longest_consecutive_already_sorted():
    assert longest_consecutive([1, 2, 3, 4, 5]) == 5


def test_longest_consecutive_efficiency_large_input():
    # 200_000 numbers built from shuffled chunks of a known range, so the
    # true answer is known ahead of time. An O(n^2) "for each number,
    # scan the whole list for its neighbors" approach would never finish
    # at this size; the O(n) set-trick handles it instantly.
    n = 200_000
    nums = list(range(n))
    rng = random.Random(42)
    rng.shuffle(nums)
    assert longest_consecutive(nums) == n
