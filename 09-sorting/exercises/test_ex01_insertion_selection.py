from ex01_insertion_selection import insertion_sort, selection_sort


def nearly_sorted(n: int) -> list[int]:
    """A sorted 0..n-1 range with a local adjacent swap every 7 slots —
    each element is at most 1 position from its sorted spot."""
    nums = list(range(n))
    for i in range(0, n - 1, 7):
        nums[i], nums[i + 1] = nums[i + 1], nums[i]
    return nums


# --- selection_sort -----------------------------------------------------


def test_selection_sort_basic():
    assert selection_sort([5, 2, 4, 1]) == [1, 2, 4, 5]


def test_selection_sort_empty():
    assert selection_sort([]) == []


def test_selection_sort_single_element():
    assert selection_sort([9]) == [9]


def test_selection_sort_duplicates():
    assert selection_sort([3, 1, 3, 1, 2]) == [1, 1, 2, 3, 3]


def test_selection_sort_negatives():
    assert selection_sort([-3, 5, -1, 0]) == [-3, -1, 0, 5]


def test_selection_sort_already_sorted():
    assert selection_sort([1, 2, 3, 4]) == [1, 2, 3, 4]


def test_selection_sort_reverse_sorted():
    assert selection_sort([4, 3, 2, 1]) == [1, 2, 3, 4]


def test_selection_sort_does_not_mutate_input():
    nums = [5, 2, 4, 1]
    selection_sort(nums)
    assert nums == [5, 2, 4, 1]


# --- insertion_sort -------------------------------------------------------


def test_insertion_sort_basic():
    assert insertion_sort([5, 2, 4, 1]) == [1, 2, 4, 5]


def test_insertion_sort_empty():
    assert insertion_sort([]) == []


def test_insertion_sort_single_element():
    assert insertion_sort([9]) == [9]


def test_insertion_sort_duplicates():
    assert insertion_sort([3, 1, 3, 1, 2]) == [1, 1, 2, 3, 3]


def test_insertion_sort_negatives():
    assert insertion_sort([-3, 5, -1, 0]) == [-3, -1, 0, 5]


def test_insertion_sort_already_sorted():
    assert insertion_sort([1, 2, 3, 4]) == [1, 2, 3, 4]


def test_insertion_sort_reverse_sorted():
    assert insertion_sort([4, 3, 2, 1]) == [1, 2, 3, 4]


def test_insertion_sort_does_not_mutate_input():
    nums = [5, 2, 4, 1]
    insertion_sort(nums)
    assert nums == [5, 2, 4, 1]


def test_insertion_sort_is_adaptive_on_nearly_sorted_input():
    # Efficiency test: shifts scale with the number of local
    # out-of-place pairs (~n/7), not with n^2 — a non-adaptive
    # implementation (or one that miscounts) blows way past this.
    n = 3000
    nums = nearly_sorted(n)
    counter = [0]
    result = insertion_sort(nums, counter)
    assert result == sorted(nums)
    assert counter[0] < n  # O(n)-ish; full O(n^2) would be ~n*n/4


def test_insertion_sort_shift_count_grows_on_reverse_sorted_input():
    # Contrast case: reverse-sorted forces every element all the way to
    # the front, so shifts should be well above the nearly-sorted bound.
    n = 200
    nums = list(range(n, 0, -1))
    counter = [0]
    insertion_sort(nums, counter)
    assert counter[0] > n
