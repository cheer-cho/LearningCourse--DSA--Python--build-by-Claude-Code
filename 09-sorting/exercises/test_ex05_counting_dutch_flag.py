import random

import pytest
from ex05_counting_dutch_flag import counting_sort, sort_colors

# --- counting_sort --------------------------------------------------------


def test_counting_sort_basic():
    assert counting_sort([3, 1, 1, 0, 2], max_value=3) == [0, 1, 1, 2, 3]


def test_counting_sort_empty():
    assert counting_sort([], max_value=5) == []


def test_counting_sort_single_element():
    assert counting_sort([4], max_value=10) == [4]


def test_counting_sort_all_same_value():
    assert counting_sort([2, 2, 2], max_value=5) == [2, 2, 2]


def test_counting_sort_already_sorted():
    assert counting_sort([0, 1, 2, 3], max_value=3) == [0, 1, 2, 3]


def test_counting_sort_does_not_mutate_input():
    nums = [3, 1, 2]
    counting_sort(nums, max_value=3)
    assert nums == [3, 1, 2]


def test_counting_sort_rejects_out_of_range_value():
    with pytest.raises(ValueError):
        counting_sort([1, 5], max_value=3)
    with pytest.raises(ValueError):
        counting_sort([-1, 2], max_value=3)


def test_counting_sort_is_stable_with_key():
    # Equal keys must keep their original relative order.
    items = [(2, "a"), (1, "b"), (2, "c"), (1, "d"), (0, "e")]
    result = counting_sort(items, max_value=2, key=lambda pair: pair[0])
    assert result == [(0, "e"), (1, "b"), (1, "d"), (2, "a"), (2, "c")]


def test_counting_sort_does_not_call_sorted(monkeypatch):
    import ex05_counting_dutch_flag as mod

    def _blocked(*_args, **_kwargs):
        raise AssertionError("counting_sort must count, not compare/sort")

    monkeypatch.setattr(mod, "sorted", _blocked, raising=False)
    assert mod.counting_sort([2, 0, 1, 1], max_value=2) == [0, 1, 1, 2]


def test_counting_sort_efficiency_large_bounded_input():
    # n = 200_000 values in a small fixed range — O(n + k) finishes
    # instantly regardless of how "unsorted" the input is.
    random.seed(7)
    nums = [random.randint(0, 9) for _ in range(200_000)]
    assert counting_sort(nums, max_value=9) == sorted(nums)


# --- sort_colors ------------------------------------------------------------


def test_sort_colors_basic():
    nums = [2, 0, 1, 1, 0]
    sort_colors(nums)
    assert nums == [0, 0, 1, 1, 2]


def test_sort_colors_returns_none():
    nums = [1, 0, 2]
    assert sort_colors(nums) is None


def test_sort_colors_empty():
    nums: list[int] = []
    sort_colors(nums)
    assert nums == []


def test_sort_colors_single_element():
    nums = [1]
    sort_colors(nums)
    assert nums == [1]


def test_sort_colors_already_sorted():
    nums = [0, 0, 1, 2, 2]
    sort_colors(nums)
    assert nums == [0, 0, 1, 2, 2]


def test_sort_colors_all_same_value():
    nums = [1, 1, 1]
    sort_colors(nums)
    assert nums == [1, 1, 1]


def test_sort_colors_reverse_sorted():
    nums = [2, 2, 1, 0, 0]
    sort_colors(nums)
    assert nums == [0, 0, 1, 2, 2]


def test_sort_colors_sorts_in_place_same_object():
    nums = [2, 1, 0]
    identity = id(nums)
    sort_colors(nums)
    assert id(nums) == identity
