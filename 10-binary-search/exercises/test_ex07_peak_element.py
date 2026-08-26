from ex07_peak_element import find_peak


def is_peak(nums: list[int], i: int) -> bool:
    left_ok = i == 0 or nums[i - 1] < nums[i]
    right_ok = i == len(nums) - 1 or nums[i] > nums[i + 1]
    return left_ok and right_ok


def test_find_peak_middle_of_array():
    nums = [1, 2, 3, 1]
    idx = find_peak(nums)
    assert is_peak(nums, idx)
    assert idx == 2


def test_find_peak_multiple_peaks_returns_a_valid_one():
    nums = [1, 2, 1, 3, 5, 6, 4]
    idx = find_peak(nums)
    assert is_peak(nums, idx)


def test_find_peak_single_element():
    assert find_peak([5]) == 0


def test_find_peak_strictly_increasing_peak_at_end():
    nums = [1, 2, 3, 4, 5]
    idx = find_peak(nums)
    assert idx == 4
    assert is_peak(nums, idx)


def test_find_peak_strictly_decreasing_peak_at_start():
    nums = [5, 4, 3, 2, 1]
    idx = find_peak(nums)
    assert idx == 0
    assert is_peak(nums, idx)


def test_find_peak_two_elements():
    assert is_peak([1, 2], find_peak([1, 2]))
    assert is_peak([2, 1], find_peak([2, 1]))


def test_find_peak_valley_then_rise():
    nums = [1, 0, 1, 2, 1]
    idx = find_peak(nums)
    assert is_peak(nums, idx)


def test_find_peak_large_array_is_fast():
    n = 1_000_000
    nums = list(range(n // 2)) + list(range(n // 2, 0, -1))
    idx = find_peak(nums)
    assert is_peak(nums, idx)
