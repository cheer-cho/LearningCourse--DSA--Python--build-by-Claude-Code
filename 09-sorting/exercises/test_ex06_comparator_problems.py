from ex06_comparator_problems import (
    largest_concat_number,
    relative_order,
    sort_by_frequency,
)

# --- largest_concat_number -------------------------------------------------


def test_largest_concat_number_classic_case():
    assert largest_concat_number([3, 30, 34, 5, 9]) == "9534330"


def test_largest_concat_number_all_zeros():
    assert largest_concat_number([0, 0, 0]) == "0"


def test_largest_concat_number_empty():
    assert largest_concat_number([]) == ""


def test_largest_concat_number_single_value():
    assert largest_concat_number([12]) == "12"


def test_largest_concat_number_equal_digits_tie():
    assert largest_concat_number([2, 21]) == "221"


# --- sort_by_frequency ------------------------------------------------------


def test_sort_by_frequency_basic():
    assert sort_by_frequency([1, 1, 2, 2, 3]) == [3, 2, 2, 1, 1]


def test_sort_by_frequency_empty():
    assert sort_by_frequency([]) == []


def test_sort_by_frequency_all_unique_sorts_descending():
    assert sort_by_frequency([1, 3, 2]) == [3, 2, 1]


def test_sort_by_frequency_all_same_value():
    assert sort_by_frequency([5, 5, 5]) == [5, 5, 5]


def test_sort_by_frequency_does_not_mutate_input():
    nums = [1, 1, 2]
    sort_by_frequency(nums)
    assert nums == [1, 1, 2]


# --- relative_order ----------------------------------------------------------


def test_relative_order_classic_case():
    result = relative_order([2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6])
    assert result == [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]


def test_relative_order_empty_nums():
    assert relative_order([], [2, 1]) == []


def test_relative_order_no_unknowns():
    assert relative_order([3, 1, 2], [3, 2, 1]) == [3, 2, 1]


def test_relative_order_all_unknown_sorts_ascending():
    assert relative_order([9, 5, 7], []) == [5, 7, 9]


def test_relative_order_does_not_mutate_input():
    nums = [2, 1, 3]
    relative_order(nums, [1, 2])
    assert nums == [2, 1, 3]
