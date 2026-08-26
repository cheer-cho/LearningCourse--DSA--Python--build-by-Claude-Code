from ex06_interval_scheduling import (
    can_attend_all,
    max_non_overlapping,
    min_removals,
    min_rooms,
)


def test_max_non_overlapping_typical():
    result = max_non_overlapping([[1, 2], [2, 3], [3, 4], [1, 4]])
    assert result == 3


def test_max_non_overlapping_empty():
    assert max_non_overlapping([]) == 0


def test_max_non_overlapping_single_interval():
    assert max_non_overlapping([[1, 5]]) == 1


def test_max_non_overlapping_all_disjoint():
    result = max_non_overlapping([[1, 2], [5, 6], [10, 11]])
    assert result == 3


def test_max_non_overlapping_all_identical():
    assert max_non_overlapping([[1, 5], [1, 5], [1, 5]]) == 1


def test_min_removals_typical():
    result = min_removals([[1, 2], [2, 3], [3, 4], [1, 3]])
    assert result == 1


def test_min_removals_all_identical():
    assert min_removals([[1, 2], [1, 2], [1, 2]]) == 2


def test_min_removals_no_overlap_needs_no_removals():
    assert min_removals([[1, 2], [3, 4], [5, 6]]) == 0


def test_min_removals_empty():
    assert min_removals([]) == 0


def test_can_attend_all_touching_is_fine():
    assert can_attend_all([[1, 2], [2, 3], [3, 4]]) is True


def test_can_attend_all_overlap_fails():
    assert can_attend_all([[1, 3], [2, 4]]) is False


def test_can_attend_all_empty():
    assert can_attend_all([]) is True


def test_can_attend_all_single_interval():
    assert can_attend_all([[1, 2]]) is True


def test_min_rooms_typical():
    assert min_rooms([[0, 30], [5, 10], [15, 20]]) == 2


def test_min_rooms_touching_reuses_room():
    assert min_rooms([[1, 2], [2, 3]]) == 1


def test_min_rooms_empty():
    assert min_rooms([]) == 0


def test_min_rooms_all_same_time_needs_n_rooms():
    assert min_rooms([[1, 5], [1, 5], [1, 5]]) == 3


def test_min_rooms_no_overlap_needs_one_room():
    assert min_rooms([[1, 2], [5, 6], [10, 11]]) == 1


def test_min_rooms_efficiency_large_input():
    n = 100_000
    # n/2 meetings all overlapping at time 0, plus n/2 disjoint later ones
    intervals = [[0, 1000] for _ in range(n // 2)]
    intervals += [[2000 + i, 2001 + i] for i in range(n // 2)]
    assert min_rooms(intervals) == n // 2
