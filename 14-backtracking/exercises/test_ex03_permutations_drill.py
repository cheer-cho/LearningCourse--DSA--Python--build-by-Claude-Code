from itertools import permutations as itertools_permutations

from ex03_permutations_drill import permutations, permutations_unique


def as_set(list_of_lists: list[list[int]]) -> set[tuple[int, ...]]:
    return {tuple(item) for item in list_of_lists}


def test_permutations_of_two_elements():
    result = permutations([1, 2])
    assert as_set(result) == {(1, 2), (2, 1)}


def test_permutations_of_empty_list():
    assert permutations([]) == [[]]


def test_permutations_of_single_element():
    assert permutations([9]) == [[9]]


def test_permutations_count_is_n_factorial():
    nums = [1, 2, 3, 4]
    assert len(permutations(nums)) == 24


def test_permutations_matches_itertools():
    nums = [1, 2, 3]
    expected = {tuple(p) for p in itertools_permutations(nums)}
    assert as_set(permutations(nums)) == expected


def test_permutations_unique_basic():
    result = permutations_unique([1, 1, 2])
    expected = {(1, 1, 2), (1, 2, 1), (2, 1, 1)}
    assert as_set(result) == expected
    assert len(result) == 3


def test_permutations_unique_no_duplicate_entries():
    result = permutations_unique([2, 2, 2])
    assert result == [[2, 2, 2]]


def test_permutations_unique_all_distinct_matches_plain_permutations():
    result = permutations_unique([1, 2, 3])
    assert len(result) == 6
    assert as_set(result) == as_set(permutations([1, 2, 3]))


def test_permutations_unique_empty_list():
    assert permutations_unique([]) == [[]]
