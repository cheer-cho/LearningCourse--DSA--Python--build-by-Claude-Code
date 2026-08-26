from ex06_prefix_ranges import RangeSum, build_prefix, pivot_index


def test_build_prefix_typical():
    assert build_prefix([3, 1, 4, 1, 5]) == [0, 3, 4, 8, 9, 14]


def test_build_prefix_empty():
    assert build_prefix([]) == [0]


def test_build_prefix_single_element():
    assert build_prefix([7]) == [0, 7]


def test_build_prefix_with_negatives():
    assert build_prefix([3, -1, -4, 1]) == [0, 3, 2, -2, -1]


def test_range_sum_typical_queries():
    rs = RangeSum([3, 1, 4, 1, 5])
    assert rs.query(1, 3) == 6
    assert rs.query(0, 4) == 14
    assert rs.query(2, 2) == 4


def test_range_sum_with_negatives():
    rs = RangeSum([4, -2, 3, -6, 5])
    assert rs.query(0, 2) == 5
    assert rs.query(1, 3) == -5


def test_range_sum_single_element_array():
    rs = RangeSum([9])
    assert rs.query(0, 0) == 9


def test_pivot_index_typical():
    assert pivot_index([1, 7, 3, 6, 5, 6]) == 3


def test_pivot_index_no_pivot():
    assert pivot_index([1, 2, 3]) == -1


def test_pivot_index_at_first_position():
    assert pivot_index([0, -1, 1]) == 0


def test_pivot_index_single_element():
    assert pivot_index([0]) == 0


def test_pivot_index_empty_list():
    assert pivot_index([]) == -1


def test_range_sum_efficiency_many_queries_on_large_array():
    n = 100_000
    nums = [1] * n
    rs = RangeSum(nums)
    # Every inclusive range (i, j) of all-1s sums to (j - i + 1).
    # 100_000 queries against a naive re-sum-the-slice approach would
    # be O(n) each -- far too slow at this size.
    for i in range(0, n, 2):
        j = n - 1 - (i % 4)
        if j <= i:
            continue
        assert rs.query(i, j) == j - i + 1
