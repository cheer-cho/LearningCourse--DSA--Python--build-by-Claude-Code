from ex02_combo_sum import combination_sum, combinations_of


def as_set(list_of_lists: list[list[int]]) -> set[tuple[int, ...]]:
    return {tuple(item) for item in list_of_lists}


def test_combinations_of_4_choose_2():
    result = combinations_of(4, 2)
    expected = {(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)}
    assert as_set(result) == expected
    assert len(result) == 6


def test_combinations_of_k_zero_is_one_empty_combination():
    assert combinations_of(3, 0) == [[]]


def test_combinations_of_k_equals_n():
    result = combinations_of(3, 3)
    assert as_set(result) == {(1, 2, 3)}


def test_combinations_of_count_matches_n_choose_k():
    # C(6, 3) = 20
    assert len(combinations_of(6, 3)) == 20


def test_combinations_of_each_combination_has_no_duplicates():
    for combo in combinations_of(5, 3):
        assert len(combo) == len(set(combo))


def test_combination_sum_basic():
    result = combination_sum([2, 3, 6], 7)
    assert as_set(result) == {(2, 2, 3)}


def test_combination_sum_multiple_results():
    result = combination_sum([2, 3, 5], 8)
    expected = {(2, 2, 2, 2), (2, 3, 3), (3, 5)}
    assert as_set(result) == expected


def test_combination_sum_no_solution():
    assert combination_sum([5], 3) == []


def test_combination_sum_single_candidate_reused():
    assert combination_sum([1], 4) == [[1, 1, 1, 1]]


def test_combination_sum_every_combo_sums_to_target():
    for combo in combination_sum([2, 3, 6, 7], 18):
        assert sum(combo) == 18
