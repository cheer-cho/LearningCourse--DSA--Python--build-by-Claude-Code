from ex06_recursion_to_iteration import countdown_iterative, deep_sum_iterative


def test_deep_sum_iterative_flat_list():
    assert deep_sum_iterative([1, 2, 3]) == 6


def test_deep_sum_iterative_nested():
    assert deep_sum_iterative([1, [2, 3], [4, [5, 6]]]) == 21


def test_deep_sum_iterative_empty():
    assert deep_sum_iterative([]) == 0


def test_deep_sum_iterative_survives_recursion_limit_depth():
    # A chain of 5,000 single-element lists nested inside each other:
    # [[[...[1]...]]]. A recursive walk would raise RecursionError well
    # before reaching the bottom (default limit is 1000); the explicit
    # stack has no such ceiling.
    depth = 5_000
    nested: list = 1
    for _ in range(depth):
        nested = [nested]
    assert deep_sum_iterative(nested) == 1


def test_countdown_iterative_typical():
    assert countdown_iterative(4) == [4, 3, 2, 1]


def test_countdown_iterative_zero_is_empty():
    assert countdown_iterative(0) == []


def test_countdown_iterative_negative_is_empty():
    assert countdown_iterative(-5) == []


def test_countdown_iterative_survives_recursion_limit_depth():
    depth = 5_000
    result = countdown_iterative(depth)
    assert len(result) == depth
    assert result[0] == depth
    assert result[-1] == 1
    assert result == list(range(depth, 0, -1))
