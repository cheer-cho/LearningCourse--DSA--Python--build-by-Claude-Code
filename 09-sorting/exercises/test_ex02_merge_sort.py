import random

from ex02_merge_sort import merge_sort


def test_merge_sort_basic():
    assert merge_sort([5, 2, 4, 1]) == [1, 2, 4, 5]


def test_merge_sort_empty():
    assert merge_sort([]) == []


def test_merge_sort_single_element():
    assert merge_sort([9]) == [9]


def test_merge_sort_duplicates():
    assert merge_sort([3, 1, 3, 1, 2]) == [1, 1, 2, 3, 3]


def test_merge_sort_negatives():
    assert merge_sort([-3, 5, -1, 0]) == [-3, -1, 0, 5]


def test_merge_sort_already_sorted():
    assert merge_sort([1, 2, 3, 4]) == [1, 2, 3, 4]


def test_merge_sort_reverse_sorted():
    assert merge_sort([4, 3, 2, 1]) == [1, 2, 3, 4]


def test_merge_sort_does_not_mutate_input():
    nums = [5, 2, 4, 1]
    merge_sort(nums)
    assert nums == [5, 2, 4, 1]


def test_merge_sort_is_stable_for_equal_keys():
    # Sort by key only (first element); a stable sort must keep the
    # original relative order of every equal-key group's tags.
    items = [(2, "a"), (1, "b"), (2, "c"), (1, "d"), (2, "e")]
    result = merge_sort(items, key=lambda pair: pair[0])
    assert result == [(1, "b"), (1, "d"), (2, "a"), (2, "c"), (2, "e")]


def test_merge_sort_efficiency_large_input():
    # n = 200_000: an O(n^2) sort is infeasible here; O(n log n) is fast.
    random.seed(9)
    nums = [random.randint(0, 1_000_000) for _ in range(200_000)]
    result = merge_sort(nums)
    assert len(result) == len(nums)
    assert result == sorted(nums)
