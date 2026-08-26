from ex03_move_zeroes import move_zeroes, partition_even_odd


def test_move_zeroes_typical():
    nums = [0, 1, 0, 3, 12]
    move_zeroes(nums)
    assert nums == [1, 3, 12, 0, 0]


def test_move_zeroes_all_zeros():
    nums = [0, 0, 0]
    move_zeroes(nums)
    assert nums == [0, 0, 0]


def test_move_zeroes_no_zeros():
    nums = [1, 2, 3]
    move_zeroes(nums)
    assert nums == [1, 2, 3]


def test_move_zeroes_already_compacted():
    nums = [1, 2, 0, 0]
    move_zeroes(nums)
    assert nums == [1, 2, 0, 0]


def test_move_zeroes_empty_list():
    nums = []
    move_zeroes(nums)
    assert nums == []


def test_move_zeroes_single_zero():
    nums = [0]
    move_zeroes(nums)
    assert nums == [0]


def test_move_zeroes_preserves_order_of_negatives_and_positives():
    nums = [0, -1, 0, 2, -3]
    move_zeroes(nums)
    assert nums == [-1, 2, -3, 0, 0]


def _assert_evens_before_odds(nums: list[int], original: list[int]) -> None:
    first_odd = next((i for i, x in enumerate(nums) if x % 2 != 0), len(nums))
    assert all(x % 2 == 0 for x in nums[:first_odd])
    assert all(x % 2 != 0 for x in nums[first_odd:])
    assert sorted(nums) == sorted(original)


def test_partition_even_odd_typical():
    original = [3, 1, 2, 4]
    nums = list(original)
    partition_even_odd(nums)
    _assert_evens_before_odds(nums, original)


def test_partition_even_odd_all_even():
    original = [2, 4, 6]
    nums = list(original)
    partition_even_odd(nums)
    _assert_evens_before_odds(nums, original)


def test_partition_even_odd_all_odd():
    original = [1, 3, 5]
    nums = list(original)
    partition_even_odd(nums)
    _assert_evens_before_odds(nums, original)


def test_partition_even_odd_empty_list():
    nums: list[int] = []
    partition_even_odd(nums)
    assert nums == []


def test_partition_even_odd_single_element():
    nums = [7]
    partition_even_odd(nums)
    assert nums == [7]
