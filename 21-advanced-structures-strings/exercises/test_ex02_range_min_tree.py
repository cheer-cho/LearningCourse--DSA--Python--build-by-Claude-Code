from ex02_range_min_tree import RangeMinTree


def test_build_and_full_range_min():
    rt = RangeMinTree([5, 2, 8, 1, 9])
    assert rt.range_min(0, 4) == 1


def test_range_min_sub_range():
    rt = RangeMinTree([5, 2, 8, 1, 9])
    assert rt.range_min(0, 2) == 2
    assert rt.range_min(2, 4) == 1


def test_range_min_single_element():
    rt = RangeMinTree([5, 2, 8, 1, 9])
    assert rt.range_min(3, 3) == 1


def test_update_changes_future_queries():
    rt = RangeMinTree([5, 2, 8, 1, 9])
    rt.update(3, 20)
    assert rt.range_min(0, 4) == 2


def test_update_raising_the_only_minimum():
    rt = RangeMinTree([3, 3, 1, 3])
    rt.update(2, 100)
    assert rt.range_min(0, 3) == 3


def test_single_element_tree():
    rt = RangeMinTree([42])
    assert rt.range_min(0, 0) == 42
    rt.update(0, -5)
    assert rt.range_min(0, 0) == -5


def test_negative_values():
    rt = RangeMinTree([-5, 3, -20, 8])
    assert rt.range_min(0, 3) == -20
    rt.update(2, 100)
    assert rt.range_min(0, 3) == -5


def test_all_equal_values():
    rt = RangeMinTree([4, 4, 4, 4])
    assert rt.range_min(1, 2) == 4


def test_empty_array_builds_without_error():
    rt = RangeMinTree([])
    assert isinstance(rt, RangeMinTree)


def test_range_min_tree_efficiency_large_input():
    # Mirrors ex01's efficiency test, confirming the min-merge
    # generalization is still O(log n) per op, not accidentally O(n).
    n = 100_000
    rt = RangeMinTree(list(range(n)))  # strictly increasing: min of any range is its left edge

    for i in range(0, n, 2):
        rt.update(i, n + i)  # push evens far above the range, odds stay small
        if i % 20_000 == 0:
            assert rt.range_min(0, i) >= 0

    assert rt.range_min(0, n - 1) == 1  # index 1 is the smallest untouched odd
    assert rt.range_min(0, 0) == n  # index 0 was pushed up to n
