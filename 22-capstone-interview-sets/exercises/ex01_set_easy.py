# Scenario: timed set 1 of 3 — SIX independent EASY problems, fresh
# scenarios, no pattern labels attached. Restate, brute force, name a
# pattern + cue, THEN code. Timebox ~15 min each.
# Run: uv run pytest 22-capstone-interview-sets -k ex01


def top_grossing_movie(sales: list[str]) -> str:
    """A cinema logs the movie title sold for every ticket during a
    screening block, in sale order. Return the title with the most
    ticket sales. Ties go to whichever title appeared FIRST in the log.

    Params:
        sales: movie title logged once per ticket sold, sale order.
    Returns:
        the best-selling title.
    Raises:
        ValueError: if `sales` is empty (message should mention "empty").

    top_grossing_movie(["nova", "nova", "atlas", "atlas", "nova"]) -> "nova"
    top_grossing_movie(["comet", "atlas"]) -> "comet"

    Target complexity: O(n) time, O(n) space.
    """
    raise NotImplementedError


def two_books_for_slot(thicknesses: list[int], target: int) -> tuple[int, int] | None:
    """A library shelf holds books sorted ascending by thickness (mm).
    Find two DIFFERENT books (by position, not value) whose thicknesses
    sum to exactly `target` — the width of a display slot.

    Params:
        thicknesses: book thicknesses, sorted ascending, may repeat.
        target: exact combined thickness to fill.
    Returns:
        `(smaller, larger)` thickness pair summing to target, or None
        if no such pair exists.

    two_books_for_slot([1, 3, 4, 6, 8], 10) -> (4, 6)
    two_books_for_slot([2, 2, 3], 4) -> (2, 2)
    two_books_for_slot([1, 2], 100) -> None

    Target complexity: O(n) time, O(1) space.
    """
    raise NotImplementedError


def busiest_call_window(calls_per_minute: list[int], k: int) -> int:
    """A call center logs calls received per minute. Find the highest
    total calls received over any window of exactly `k` consecutive
    minutes.

    Params:
        calls_per_minute: one reading per minute.
        k: window size, 1 <= k <= len(calls_per_minute).
    Returns:
        the largest sum of any k consecutive readings.
    Raises:
        ValueError: if k is not between 1 and len(calls_per_minute).

    busiest_call_window([3, 1, 4, 1, 5, 9, 2], 3) -> 16
    busiest_call_window([5], 1) -> 5

    Target complexity: O(n) time, O(1) space.
    """
    raise NotImplementedError


def is_balanced_formula(expr: str) -> bool:
    """A spreadsheet formula parser uses three bracket kinds: (), [],
    {}. Decide whether every opening bracket in `expr` is closed by
    the matching kind, in the correct nested order. Non-bracket
    characters are ignored.

    Params:
        expr: the formula source text.
    Returns:
        True if every bracket is validly nested and closed.

    is_balanced_formula("SUM(A1,[B1,{C1}])") -> True
    is_balanced_formula("SUM(A1,[B1)") -> False
    is_balanced_formula("") -> True

    Target complexity: O(n) time, O(n) space.
    """
    raise NotImplementedError


def shortest_path_to_exit(floor_plan: list[list[int]]) -> int:
    """A firefighting drone starts at the top-left cell of a smoke-
    filled building floor and must reach the exit at the bottom-right
    cell, moving one cell at a time up/down/left/right. Some cells are
    collapsed floor (blocked).

    Params:
        floor_plan: rows of 0 (clear) / 1 (blocked).
    Returns:
        the minimum number of moves from top-left to bottom-right, or
        -1 if unreachable (including an empty grid, or a blocked start
        or end cell).

    shortest_path_to_exit([[0,0,0],[1,1,0],[0,0,0]]) -> 4
    shortest_path_to_exit([[0,1],[1,0]]) -> -1
    shortest_path_to_exit([[0]]) -> 0

    Target complexity: O(rows * cols) time, O(rows * cols) space.
    """
    raise NotImplementedError


def first_ticket_with_priority(priorities: list[int], target: int) -> int:
    """A support desk queues tickets sorted ascending by priority
    number (duplicates allowed). Find the leftmost index of a ticket
    whose priority equals `target`.

    Params:
        priorities: ticket priorities, sorted ascending.
        target: the priority value to locate.
    Returns:
        the 0-based index of the FIRST ticket with that priority, or
        -1 if none has it.

    first_ticket_with_priority([1, 2, 2, 2, 5], 2) -> 1
    first_ticket_with_priority([1, 3, 5], 4) -> -1
    first_ticket_with_priority([], 1) -> -1

    Target complexity: O(log n) time, O(1) space.
    """
    raise NotImplementedError
