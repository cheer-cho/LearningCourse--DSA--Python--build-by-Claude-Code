from ex01_subsets_drill import subsets, subsets_with_dup


def as_set(list_of_lists: list[list[int]]) -> set[frozenset[int]]:
    return {frozenset(item) for item in list_of_lists}


def test_subsets_of_two_elements():
    result = subsets([1, 2])
    assert len(result) == 4
    assert as_set(result) == {frozenset(), frozenset({1}), frozenset({2}), frozenset({1, 2})}


def test_subsets_of_empty_list():
    assert subsets([]) == [[]]


def test_subsets_of_single_element():
    result = subsets([5])
    assert as_set(result) == {frozenset(), frozenset({5})}


def test_subsets_count_is_two_to_the_n():
    nums = [1, 2, 3, 4, 5]
    assert len(subsets(nums)) == 2**5


def test_subsets_no_duplicate_subsets_produced():
    result = subsets([1, 2, 3])
    seen = [frozenset(item) for item in result]
    assert len(seen) == len(set(seen))


def as_multiset(list_of_lists: list[list[int]]) -> set[tuple[int, ...]]:
    # frozenset would collapse [2] and [2, 2] to the same set — use
    # sorted tuples so multiplicity (how many 2's) is preserved.
    return {tuple(sorted(item)) for item in list_of_lists}


def test_subsets_with_dup_basic():
    result = subsets_with_dup([1, 2, 2])
    expected = as_multiset([[], [1], [2], [1, 2], [2, 2], [1, 2, 2]])
    assert as_multiset(result) == expected
    assert len(result) == len(expected)


def test_subsets_with_dup_no_repeated_subset_in_output():
    result = subsets_with_dup([4, 4, 4])
    # multiset-aware: [], [4], [4,4], [4,4,4] -> 4 distinct subsets
    assert len(result) == 4


def test_subsets_with_dup_all_unique_matches_plain_subsets():
    result = subsets_with_dup([1, 2, 3])
    assert len(result) == 8
    assert as_set(result) == as_set(subsets([1, 2, 3]))


def test_subsets_with_dup_empty_list():
    assert subsets_with_dup([]) == [[]]
