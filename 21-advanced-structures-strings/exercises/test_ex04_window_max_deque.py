from ex04_window_max_deque import window_maxes


def test_window_maxes_typical():
    assert window_maxes([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]


def test_window_maxes_all_same():
    assert window_maxes([9, 9, 9], 1) == [9, 9, 9]


def test_window_maxes_empty_input():
    assert window_maxes([], 3) == []


def test_window_maxes_k_equals_length():
    assert window_maxes([4, 2, 7, 1], 4) == [7]


def test_window_maxes_k_equals_one_returns_input():
    assert window_maxes([5, 1, 4, 2], 1) == [5, 1, 4, 2]


def test_window_maxes_strictly_increasing():
    assert window_maxes([1, 2, 3, 4, 5], 2) == [2, 3, 4, 5]


def test_window_maxes_strictly_decreasing():
    assert window_maxes([5, 4, 3, 2, 1], 2) == [5, 4, 3, 2]


def test_window_maxes_negative_numbers():
    assert window_maxes([-4, -2, -8, -1], 2) == [-2, -2, -1]


def test_window_maxes_efficiency_large_input():
    # n = 200,000, k = 1,000. A naive scan-each-window approach is
    # O(n*k) here (~2 * 10^8 comparisons) -- painfully slow. A
    # monotonic deque handles it in O(n).
    n = 200_000
    k = 1_000
    nums = list(range(n))  # strictly increasing
    result = window_maxes(nums, k)
    # in a strictly increasing array, each window's max is its last element
    assert result == list(range(k - 1, n))
