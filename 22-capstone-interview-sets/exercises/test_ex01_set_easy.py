import pytest
from ex01_set_easy import (
    busiest_call_window,
    first_ticket_with_priority,
    is_balanced_formula,
    shortest_path_to_exit,
    top_grossing_movie,
    two_books_for_slot,
)

# --- top_grossing_movie -----------------------------------------------


def test_top_grossing_movie_clear_winner():
    assert top_grossing_movie(["nova", "nova", "atlas", "atlas", "nova"]) == "nova"


def test_top_grossing_movie_tie_goes_to_first_seen():
    assert top_grossing_movie(["comet", "atlas"]) == "comet"


def test_top_grossing_movie_single_sale():
    assert top_grossing_movie(["solo"]) == "solo"


def test_top_grossing_movie_empty_raises():
    with pytest.raises(ValueError, match="empty"):
        top_grossing_movie([])


def test_top_grossing_movie_three_way_tie_first_seen_wins():
    assert top_grossing_movie(["b", "a", "c", "b", "a", "c"]) == "b"


# --- two_books_for_slot -------------------------------------------------


def test_two_books_for_slot_typical():
    assert two_books_for_slot([1, 3, 4, 6, 8], 10) == (4, 6)


def test_two_books_for_slot_duplicates():
    assert two_books_for_slot([2, 2, 3], 4) == (2, 2)


def test_two_books_for_slot_no_match():
    assert two_books_for_slot([1, 2], 100) is None


def test_two_books_for_slot_single_element_no_match():
    assert two_books_for_slot([5], 10) is None


def test_two_books_for_slot_needs_two_distinct_positions():
    # No pair of DIFFERENT positions sums to 6 here (only a single 3,
    # and no other combination reaches the target).
    assert two_books_for_slot([2, 3, 7], 6) is None


def test_two_books_for_slot_large_efficiency():
    thicknesses = list(range(0, 200_000, 2))
    target = thicknesses[10] + thicknesses[-5]
    result = two_books_for_slot(thicknesses, target)
    assert result is not None
    assert result[0] + result[1] == target
    assert result[0] in thicknesses and result[1] in thicknesses


# --- busiest_call_window -------------------------------------------------


def test_busiest_call_window_typical():
    assert busiest_call_window([3, 1, 4, 1, 5, 9, 2], 3) == 16


def test_busiest_call_window_k_equals_length():
    assert busiest_call_window([1, 2, 3], 3) == 6


def test_busiest_call_window_single_element():
    assert busiest_call_window([5], 1) == 5


def test_busiest_call_window_invalid_k_raises():
    with pytest.raises(ValueError):
        busiest_call_window([1, 2, 3], 0)
    with pytest.raises(ValueError):
        busiest_call_window([1, 2, 3], 4)


def test_busiest_call_window_large_efficiency():
    readings = [1] * 200_000
    readings[100_000:100_050] = [100] * 50
    assert busiest_call_window(readings, 50) == 5000


# --- is_balanced_formula -------------------------------------------------


def test_is_balanced_formula_nested_valid():
    assert is_balanced_formula("SUM(A1,[B1,{C1}])") is True


def test_is_balanced_formula_mismatched():
    assert is_balanced_formula("SUM(A1,[B1)") is False


def test_is_balanced_formula_empty_is_balanced():
    assert is_balanced_formula("") is True


def test_is_balanced_formula_ignores_non_bracket_chars():
    assert is_balanced_formula("a+b*(c-d)/[e]") is True


def test_is_balanced_formula_unmatched_closer():
    assert is_balanced_formula(")(") is False


def test_is_balanced_formula_only_openers():
    assert is_balanced_formula("(((") is False


# --- shortest_path_to_exit ------------------------------------------------


def test_shortest_path_to_exit_typical():
    grid = [[0, 0, 0], [1, 1, 0], [0, 0, 0]]
    assert shortest_path_to_exit(grid) == 4


def test_shortest_path_to_exit_unreachable():
    grid = [[0, 1], [1, 0]]
    assert shortest_path_to_exit(grid) == -1


def test_shortest_path_to_exit_single_cell():
    assert shortest_path_to_exit([[0]]) == 0


def test_shortest_path_to_exit_blocked_start():
    assert shortest_path_to_exit([[1, 0], [0, 0]]) == -1


def test_shortest_path_to_exit_empty_grid():
    assert shortest_path_to_exit([]) == -1


def test_shortest_path_to_exit_large_open_grid_efficiency():
    n = 200
    grid = [[0] * n for _ in range(n)]
    assert shortest_path_to_exit(grid) == 2 * (n - 1)


# --- first_ticket_with_priority --------------------------------------------


def test_first_ticket_with_priority_finds_leftmost_of_duplicates():
    assert first_ticket_with_priority([1, 2, 2, 2, 5], 2) == 1


def test_first_ticket_with_priority_not_found():
    assert first_ticket_with_priority([1, 3, 5], 4) == -1


def test_first_ticket_with_priority_empty():
    assert first_ticket_with_priority([], 1) == -1


def test_first_ticket_with_priority_single_match():
    assert first_ticket_with_priority([7], 7) == 0


def test_first_ticket_with_priority_target_at_start():
    assert first_ticket_with_priority([2, 2, 4, 6], 2) == 0


def test_first_ticket_with_priority_large_efficiency():
    priorities = [1] * 100_000 + [2] * 100_000
    assert first_ticket_with_priority(priorities, 2) == 100_000
