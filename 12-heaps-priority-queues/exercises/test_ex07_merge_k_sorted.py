import random

from ex07_merge_k_sorted import merge_k_sorted


def test_merge_k_sorted_typical():
    result = merge_k_sorted([[1, 4, 7], [2, 5], [3, 6, 8, 9]])
    assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_merge_k_sorted_no_lists():
    assert merge_k_sorted([]) == []


def test_merge_k_sorted_all_empty_lists():
    assert merge_k_sorted([[], [], []]) == []


def test_merge_k_sorted_some_empty_lists():
    assert merge_k_sorted([[], [1], []]) == [1]


def test_merge_k_sorted_single_list():
    assert merge_k_sorted([[1, 2, 3]]) == [1, 2, 3]


def test_merge_k_sorted_duplicates_across_lists():
    result = merge_k_sorted([[1, 3, 3], [2, 3], [3, 3]])
    assert result == [1, 2, 3, 3, 3, 3, 3]


def test_merge_k_sorted_negatives():
    result = merge_k_sorted([[-5, -1, 4], [-3, 0, 2]])
    assert result == [-5, -3, -1, 0, 2, 4]


def test_merge_k_sorted_ties_do_not_crash_with_unorderable_payload():
    # Same value appears as the head of two lists at once -- if the
    # solution didn't add a tie-breaker to the heap key, comparing the
    # lists themselves would raise TypeError.
    result = merge_k_sorted([[5, 9], [5, 6]])
    assert result == [5, 5, 6, 9]


def test_merge_k_sorted_large_input():
    rng = random.Random(31)
    lists = []
    for _ in range(1_000):
        length = 100
        values = sorted(rng.randint(-10**6, 10**6) for _ in range(length))
        lists.append(values)

    result = merge_k_sorted(lists)
    expected = sorted(val for lst in lists for val in lst)
    assert result == expected
