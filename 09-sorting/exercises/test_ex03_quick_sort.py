import random

from ex03_quick_sort import quick_sort


def test_quick_sort_basic():
    nums = [5, 2, 4, 1]
    quick_sort(nums)
    assert nums == [1, 2, 4, 5]


def test_quick_sort_returns_none():
    nums = [3, 1, 2]
    assert quick_sort(nums) is None


def test_quick_sort_empty():
    nums: list[int] = []
    quick_sort(nums)
    assert nums == []


def test_quick_sort_single_element():
    nums = [9]
    quick_sort(nums)
    assert nums == [9]


def test_quick_sort_duplicates():
    nums = [3, 1, 3, 1, 2]
    quick_sort(nums)
    assert nums == [1, 1, 2, 3, 3]


def test_quick_sort_negatives():
    nums = [-3, 5, -1, 0]
    quick_sort(nums)
    assert nums == [-3, -1, 0, 5]


def test_quick_sort_already_sorted():
    nums = [1, 2, 3, 4]
    quick_sort(nums)
    assert nums == [1, 2, 3, 4]


def test_quick_sort_all_equal():
    nums = [7, 7, 7, 7]
    quick_sort(nums)
    assert nums == [7, 7, 7, 7]


def test_quick_sort_sorts_in_place_same_object():
    nums = [5, 2, 4, 1]
    identity = id(nums)
    quick_sort(nums)
    assert id(nums) == identity
    assert nums == [1, 2, 4, 5]


def test_quick_sort_efficiency_large_random_input():
    # n = 200_000: an O(n^2) sort is infeasible here; O(n log n) is fast.
    random.seed(11)
    nums = [random.randint(0, 1_000_000) for _ in range(200_000)]
    quick_sort(nums)
    assert nums == sorted(nums)


def test_quick_sort_efficiency_already_sorted_input():
    # This is the input that breaks a fixed-first-element pivot: without
    # randomization AND recursing into the smaller side first, this is
    # both O(n^2) time and O(n) recursion depth (a RecursionError on
    # Python's default recursion limit).
    n = 200_000
    nums = list(range(n))
    quick_sort(nums)
    assert nums == list(range(n))
