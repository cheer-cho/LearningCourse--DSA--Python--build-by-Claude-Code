from ex05_merge_intervals import insert_interval, merge_intervals


def test_merge_intervals_typical():
    result = merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]])
    assert result == [[1, 6], [8, 10], [15, 18]]


def test_merge_intervals_touching_stays_separate():
    assert merge_intervals([[1, 2], [2, 3]]) == [[1, 2], [2, 3]]


def test_merge_intervals_empty():
    assert merge_intervals([]) == []


def test_merge_intervals_single_interval():
    assert merge_intervals([[5, 7]]) == [[5, 7]]


def test_merge_intervals_unsorted_input():
    result = merge_intervals([[8, 10], [1, 3], [2, 6]])
    assert result == [[1, 6], [8, 10]]


def test_merge_intervals_fully_nested():
    assert merge_intervals([[1, 10], [2, 5]]) == [[1, 10]]


def test_merge_intervals_all_overlap_into_one():
    result = merge_intervals([[1, 4], [2, 5], [3, 6]])
    assert result == [[1, 6]]


def test_merge_intervals_efficiency_large_input():
    n = 100_000
    intervals = [[i, i + 2] for i in range(n)]  # heavily overlapping chain
    result = merge_intervals(intervals)
    assert result == [[0, n + 1]]


def test_insert_interval_merges_with_neighbors():
    result = insert_interval([[1, 3], [6, 9]], [2, 5])
    assert result == [[1, 5], [6, 9]]


def test_insert_interval_merges_several():
    result = insert_interval([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 9])
    assert result == [[1, 2], [3, 10], [12, 16]]


def test_insert_interval_no_overlap_inserts_in_place():
    result = insert_interval([[1, 2], [5, 6]], [3, 4])
    assert result == [[1, 2], [3, 4], [5, 6]]


def test_insert_interval_empty_schedule():
    assert insert_interval([], [5, 7]) == [[5, 7]]


def test_insert_interval_touching_stays_separate():
    result = insert_interval([[1, 2]], [2, 3])
    assert result == [[1, 2], [2, 3]]


def test_insert_interval_before_everything():
    result = insert_interval([[5, 6], [8, 9]], [1, 2])
    assert result == [[1, 2], [5, 6], [8, 9]]


def test_insert_interval_after_everything():
    result = insert_interval([[1, 2], [3, 4]], [6, 7])
    assert result == [[1, 2], [3, 4], [6, 7]]
