from ex02_pair_sum import pair_sum


def _check(nums: list[int], target: int, result: tuple[int, int] | None) -> None:
    assert result is not None
    i, j = result
    assert i != j
    assert nums[i] + nums[j] == target


def test_pair_sum_typical():
    result = pair_sum([2, 7, 11, 15], 9)
    _check([2, 7, 11, 15], 9, result)
    assert set(result) == {0, 1}


def test_pair_sum_duplicate_values():
    result = pair_sum([3, 3], 6)
    _check([3, 3], 6, result)
    assert set(result) == {0, 1}


def test_pair_sum_no_pair_returns_none():
    assert pair_sum([1, 2, 3], 100) is None


def test_pair_sum_empty_list_returns_none():
    assert pair_sum([], 5) is None


def test_pair_sum_single_element_returns_none():
    assert pair_sum([5], 10) is None


def test_pair_sum_negative_numbers():
    result = pair_sum([-3, 4, 1, 90], -2)
    _check([-3, 4, 1, 90], -2, result)


def test_pair_sum_target_zero():
    result = pair_sum([0, 4, -4, 8], 0)
    _check([0, 4, -4, 8], 0, result)


def test_pair_sum_does_not_reuse_same_index():
    # Only one 5 in the list; target needs two of them, so no valid pair.
    assert pair_sum([5, 1, 2], 10) is None


def test_pair_sum_efficiency_large_input():
    # 200_000 distinct values 0..n-1; the ONLY pair summing to target is
    # the last two elements (n-2, n-1), so a nested-loop brute force
    # would scan nearly the whole n^2 grid before finding it. The O(n)
    # complement-map approach handles this instantly.
    n = 200_000
    nums = list(range(n))
    target = (n - 2) + (n - 1)
    result = pair_sum(nums, target)
    _check(nums, target, result)
    assert set(result) == {n - 2, n - 1}
