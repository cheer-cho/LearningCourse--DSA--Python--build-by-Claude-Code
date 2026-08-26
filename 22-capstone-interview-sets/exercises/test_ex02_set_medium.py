import random

from ex02_set_medium import (
    buildings_until_taller,
    longest_run_at_most_k_genres,
    min_notes_for_amount,
    station_run_order,
    top_k_frequent_skus,
    unique_arrangements,
)

# --- longest_run_at_most_k_genres -----------------------------------------


def test_longest_run_at_most_k_genres_typical():
    genres = ["house", "house", "techno", "trance", "house"]
    assert longest_run_at_most_k_genres(genres, 2) == 3


def test_longest_run_at_most_k_genres_k_one_forces_single_run():
    assert longest_run_at_most_k_genres(["a", "b", "c"], 1) == 1


def test_longest_run_at_most_k_genres_k_zero_is_zero():
    assert longest_run_at_most_k_genres(["a", "b"], 0) == 0


def test_longest_run_at_most_k_genres_empty_input():
    assert longest_run_at_most_k_genres([], 3) == 0


def test_longest_run_at_most_k_genres_whole_list_fits():
    assert longest_run_at_most_k_genres(["a", "a", "b", "b"], 2) == 4


def test_longest_run_at_most_k_genres_large_efficiency():
    rng = random.Random(1)
    genres = [rng.choice("ABCDEFGHIJ") for _ in range(200_000)]
    result = longest_run_at_most_k_genres(genres, 3)
    assert isinstance(result, int) and result >= 3


# --- buildings_until_taller --------------------------------------------


def test_buildings_until_taller_typical():
    assert buildings_until_taller([3, 1, 4, 2, 5]) == [2, 1, 2, 1, 0]


def test_buildings_until_taller_strictly_decreasing_all_zero():
    assert buildings_until_taller([5, 4, 3]) == [0, 0, 0]


def test_buildings_until_taller_single_building():
    assert buildings_until_taller([9]) == [0]


def test_buildings_until_taller_equal_heights_never_strictly_taller():
    assert buildings_until_taller([4, 4, 4]) == [0, 0, 0]


def test_buildings_until_taller_large_efficiency():
    heights = list(range(150_000, 0, -1)) + [999_999]
    result = buildings_until_taller(heights)
    assert result[0] == len(heights) - 1
    assert result[-1] == 0


# --- top_k_frequent_skus --------------------------------------------------


def test_top_k_frequent_skus_typical():
    scans = ["A", "B", "A", "C", "B", "A"]
    assert top_k_frequent_skus(scans, 2) == ["A", "B"]


def test_top_k_frequent_skus_tie_breaks_alphabetically():
    assert top_k_frequent_skus(["X", "Y", "Z"], 2) == ["X", "Y"]


def test_top_k_frequent_skus_k_equals_distinct_count():
    scans = ["m", "n", "m", "o"]
    assert top_k_frequent_skus(scans, 3) == ["m", "n", "o"]


def test_top_k_frequent_skus_single_sku():
    assert top_k_frequent_skus(["Z", "Z", "Z"], 1) == ["Z"]


def test_top_k_frequent_skus_large_efficiency():
    rng = random.Random(7)
    skus = [f"sku-{rng.randint(0, 500)}" for _ in range(200_000)]
    result = top_k_frequent_skus(skus, 5)
    assert len(result) == 5


# --- station_run_order -----------------------------------------------------


def test_station_run_order_typical():
    order = station_run_order(4, [(1, 0), (2, 0), (3, 1), (3, 2)])
    assert order == [0, 1, 2, 3]


def test_station_run_order_cycle_returns_none():
    assert station_run_order(2, [(0, 1), (1, 0)]) is None


def test_station_run_order_no_prerequisites_is_numeric_order():
    assert station_run_order(3, []) == [0, 1, 2]


def test_station_run_order_single_station():
    assert station_run_order(1, []) == [0]


def test_station_run_order_self_cycle():
    assert station_run_order(1, [(0, 0)]) is None


def test_station_run_order_respects_all_prerequisites():
    order = station_run_order(5, [(2, 0), (2, 1), (4, 2), (4, 3)])
    assert order is not None
    positions = {station: i for i, station in enumerate(order)}
    for after, before in [(2, 0), (2, 1), (4, 2), (4, 3)]:
        assert positions[before] < positions[after]


def test_station_run_order_large_chain_efficiency():
    # A 100,000-node chain of dependencies (station i+1 needs station i
    # first). Validate with a position map in O(n) -- checking each
    # prerequisite by re-scanning the order would be O(n^2) and
    # infeasible at this size.
    n = 100_000
    prerequisites = [(i + 1, i) for i in range(n - 1)]
    order = station_run_order(n, prerequisites)
    assert order is not None
    assert len(order) == n
    positions = {station: i for i, station in enumerate(order)}
    for after, before in prerequisites:
        assert positions[before] < positions[after]


# --- min_notes_for_amount --------------------------------------------------


def test_min_notes_for_amount_typical():
    assert min_notes_for_amount([1, 5, 10, 25], 30) == 2


def test_min_notes_for_amount_impossible():
    assert min_notes_for_amount([5, 10], 3) == -1


def test_min_notes_for_amount_zero_amount():
    assert min_notes_for_amount([1, 5, 10, 25], 0) == 0


def test_min_notes_for_amount_single_denomination():
    assert min_notes_for_amount([3], 9) == 3
    assert min_notes_for_amount([3], 10) == -1


def test_min_notes_for_amount_large_efficiency():
    # A naive exponential recursion (no memo) is infeasible here; the
    # O(amount * len(denominations)) DP finishes instantly.
    assert min_notes_for_amount([1, 5, 10, 25, 100], 999_999) > 0


# --- unique_arrangements -----------------------------------------------


def test_unique_arrangements_with_duplicates():
    assert unique_arrangements("AAT") == ["AAT", "ATA", "TAA"]


def test_unique_arrangements_no_duplicates():
    assert unique_arrangements("AB") == ["AB", "BA"]


def test_unique_arrangements_single_char():
    assert unique_arrangements("Z") == ["Z"]


def test_unique_arrangements_all_same_char():
    assert unique_arrangements("AAA") == ["AAA"]


def test_unique_arrangements_count_matches_multinomial():
    # "AABB" has 4! / (2! * 2!) = 6 distinct arrangements.
    result = unique_arrangements("AABB")
    assert len(result) == 6
    assert result == sorted(result)
