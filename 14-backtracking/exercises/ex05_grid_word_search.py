# Scenario: a word-search puzzle app needs to check whether a word can
# be traced through adjacent grid cells. Pattern: DFS + backtracking on
# a grid, in-place visited marking with restore-on-unchoose.
# Run: uv run pytest 14-backtracking -k ex05


def exists_in_grid(board: list[list[str]], word: str) -> bool:
    """Return True if `word` can be traced through `board` by moving
    to horizontally/vertically adjacent cells (not diagonal), never
    reusing the SAME cell twice within one trace. `board` is a
    non-empty rectangular grid of single characters; `word` is
    non-empty.

    Mark a cell visited in place before recursing into its neighbors
    (e.g. overwrite it with a sentinel that can't match any letter),
    and restore the original character before returning from that
    call — the classic choose/explore/unchoose, applied to a grid
    instead of a list.

    exists_in_grid(
        [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]],
        "ABCCED",
    ) -> True

    exists_in_grid(
        [["A","B"],
         ["C","D"]],
        "ABC",
    ) -> False   (after A->B, C is not adjacent to B — only D and A are)

    exists_in_grid([["A","A"]], "AAA") -> False   (only 2 cells, and a
        cell can't be reused: this is the reuse-forbidden trap)

    Target: O(rows * cols * 4^len(word)) time worst case, O(len(word))
    recursion depth (the grid mutation is O(1) extra space, not
    counting the recursion stack).
    """
    raise NotImplementedError
