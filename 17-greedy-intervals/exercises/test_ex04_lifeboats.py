from ex04_lifeboats import assign_kits, min_boats


def test_min_boats_pair_fits():
    assert min_boats([1, 2], 3) == 1


def test_min_boats_typical():
    assert min_boats([3, 2, 2, 1], 3) == 3


def test_min_boats_pairs_cleanly():
    assert min_boats([5, 1, 4, 2], 6) == 2


def test_min_boats_single_person():
    assert min_boats([4], 5) == 1


def test_min_boats_everyone_pairs():
    assert min_boats([1, 1, 1, 1], 2) == 2


def test_min_boats_nobody_pairs():
    assert min_boats([5, 5, 5, 5], 5) == 4


def test_min_boats_efficiency_large_input():
    n = 200_000
    weights = [1] * n
    assert min_boats(weights, 2) == n // 2


def test_assign_kits_typical():
    assert assign_kits([1, 2, 3], [1, 2]) == 2


def test_assign_kits_more_needs_than_kits():
    assert assign_kits([1, 2], [1, 2, 3]) == 2


def test_assign_kits_no_kits():
    assert assign_kits([], [1, 2]) == 0


def test_assign_kits_no_needs():
    assert assign_kits([1, 2, 3], []) == 0


def test_assign_kits_no_kit_big_enough():
    assert assign_kits([1, 1], [5, 5]) == 0


def test_assign_kits_exact_matches():
    assert assign_kits([1, 2, 3], [3, 2, 1]) == 3


def test_assign_kits_efficiency_large_input():
    n = 200_000
    kits = list(range(n))
    needs = list(range(n))
    assert assign_kits(kits, needs) == n
