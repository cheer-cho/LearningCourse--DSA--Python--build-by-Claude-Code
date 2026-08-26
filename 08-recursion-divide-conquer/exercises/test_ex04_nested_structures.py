from ex04_nested_structures import deep_sum, flatten, max_depth_nested


def test_deep_sum_flat_list():
    assert deep_sum([1, 2, 3]) == 6


def test_deep_sum_nested():
    assert deep_sum([1, [2, 3], [4, [5, 6]]]) == 21


def test_deep_sum_empty():
    assert deep_sum([]) == 0


def test_deep_sum_deeply_nested_single_value():
    assert deep_sum([[[[7]]]]) == 7


def test_deep_sum_with_negatives():
    assert deep_sum([1, -2, [3, -4]]) == -2


def test_max_depth_nested_empty_is_one():
    assert max_depth_nested([]) == 1


def test_max_depth_nested_flat_is_one():
    assert max_depth_nested([1, 2, 3]) == 1


def test_max_depth_nested_two_levels():
    assert max_depth_nested([1, [2, 3]]) == 2


def test_max_depth_nested_four_levels():
    assert max_depth_nested([1, [2, [3, [4]]]]) == 4


def test_max_depth_nested_takes_the_deepest_branch():
    assert max_depth_nested([[1], [2, [3, [4, [5]]]], [6]]) == 5


def test_flatten_nested():
    assert flatten([1, [2, 3], [4, [5, 6]]]) == [1, 2, 3, 4, 5, 6]


def test_flatten_empty():
    assert flatten([]) == []


def test_flatten_preserves_order():
    assert flatten([[1], [2, [3, 4]], 5]) == [1, 2, 3, 4, 5]


def test_flatten_all_empty_sublists():
    assert flatten([[], [[]], []]) == []
