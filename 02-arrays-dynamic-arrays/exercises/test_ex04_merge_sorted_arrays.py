from ex04_merge_sorted_arrays import merge, merge_into


def test_merge_typical_interleaved():
    assert merge([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]


def test_merge_first_empty():
    assert merge([], [1, 2]) == [1, 2]


def test_merge_second_empty():
    assert merge([1, 2], []) == [1, 2]


def test_merge_both_empty():
    assert merge([], []) == []


def test_merge_with_duplicates_across_lists():
    assert merge([1, 1], [1]) == [1, 1, 1]


def test_merge_one_list_entirely_smaller():
    assert merge([1, 2, 3], [10, 11]) == [1, 2, 3, 10, 11]


def test_merge_does_not_mutate_inputs():
    a, b = [1, 3], [2, 4]
    merge(a, b)
    assert a == [1, 3]
    assert b == [2, 4]


def test_merge_efficiency_on_large_input():
    n = 50_000
    a = list(range(0, 2 * n, 2))  # 0, 2, 4, ...
    b = list(range(1, 2 * n, 2))  # 1, 3, 5, ...
    result = merge(a, b)
    assert len(result) == 2 * n
    assert result == sorted(a + b)


def test_merge_into_typical():
    a = [1, 3, 5, 0, 0, 0]
    merge_into(a, 3, [2, 4, 6])
    assert a == [1, 2, 3, 4, 5, 6]


def test_merge_into_a_starts_empty():
    a = [0, 0, 0]
    merge_into(a, 0, [1, 2, 3])
    assert a == [1, 2, 3]


def test_merge_into_b_empty_leaves_a_unchanged():
    a = [1, 2, 3]
    merge_into(a, 3, [])
    assert a == [1, 2, 3]


def test_merge_into_b_entirely_smaller_than_a():
    a = [5, 6, 7, 0, 0]
    merge_into(a, 3, [1, 2])
    assert a == [1, 2, 5, 6, 7]


def test_merge_into_b_entirely_larger_than_a():
    a = [1, 2, 0, 0]
    merge_into(a, 2, [3, 4])
    assert a == [1, 2, 3, 4]


def test_merge_into_with_duplicates():
    a = [2, 2, 0, 0]
    merge_into(a, 2, [2, 2])
    assert a == [2, 2, 2, 2]
