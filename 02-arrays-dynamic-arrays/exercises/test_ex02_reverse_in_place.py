from ex02_reverse_in_place import reverse, rotate_right


def test_reverse_typical():
    nums = [1, 2, 3, 4]
    reverse(nums)
    assert nums == [4, 3, 2, 1]


def test_reverse_empty():
    nums: list[int] = []
    reverse(nums)
    assert nums == []


def test_reverse_single_element():
    nums = [7]
    reverse(nums)
    assert nums == [7]


def test_reverse_odd_length():
    nums = [1, 2, 3, 4, 5]
    reverse(nums)
    assert nums == [5, 4, 3, 2, 1]


def test_reverse_mutates_same_object():
    nums = [1, 2, 3]
    original_id = id(nums)
    reverse(nums)
    assert id(nums) == original_id


def test_rotate_right_typical():
    nums = [1, 2, 3, 4, 5]
    rotate_right(nums, 2)
    assert nums == [4, 5, 1, 2, 3]


def test_rotate_right_k_zero_is_a_no_op():
    nums = [1, 2, 3]
    rotate_right(nums, 0)
    assert nums == [1, 2, 3]


def test_rotate_right_k_equals_length_is_a_no_op():
    nums = [1, 2, 3]
    rotate_right(nums, 3)
    assert nums == [1, 2, 3]


def test_rotate_right_k_greater_than_length_wraps():
    nums = [1, 2, 3]
    rotate_right(nums, 5)  # 5 % 3 == 2
    assert nums == [2, 3, 1]


def test_rotate_right_single_element():
    nums = [9]
    rotate_right(nums, 4)
    assert nums == [9]


def test_rotate_right_empty_list_does_not_crash():
    nums: list[int] = []
    rotate_right(nums, 3)
    assert nums == []


def test_rotate_right_mutates_same_object():
    nums = [1, 2, 3, 4]
    original_id = id(nums)
    rotate_right(nums, 1)
    assert id(nums) == original_id
