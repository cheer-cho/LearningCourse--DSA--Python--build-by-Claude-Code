import random

from ex02_heap_sort import heap_sort


def test_heap_sort_typical():
    assert heap_sort([5, 1, 4, 2, 8]) == [1, 2, 4, 5, 8]


def test_heap_sort_empty_list():
    assert heap_sort([]) == []


def test_heap_sort_single_element():
    assert heap_sort([42]) == [42]


def test_heap_sort_already_sorted():
    assert heap_sort([1, 2, 3, 4]) == [1, 2, 3, 4]


def test_heap_sort_reverse_sorted():
    assert heap_sort([9, 7, 5, 3, 1]) == [1, 3, 5, 7, 9]


def test_heap_sort_with_duplicates():
    assert heap_sort([3, 1, 3, 1, 2]) == [1, 1, 2, 3, 3]


def test_heap_sort_negatives_and_positives():
    assert heap_sort([-3, 5, -1, 0, 2]) == [-3, -1, 0, 2, 5]


def test_heap_sort_does_not_mutate_input():
    nums = [5, 1, 4, 2, 8]
    original = list(nums)
    heap_sort(nums)
    assert nums == original


def test_heap_sort_returns_new_object():
    nums = [3, 1, 2]
    assert heap_sort(nums) is not nums


def test_heap_sort_large_random_input():
    rng = random.Random(3)
    nums = [rng.randint(-1_000_000, 1_000_000) for _ in range(100_000)]
    assert heap_sort(nums) == sorted(nums)
