# Scenario: a lottery-ticket generator (pick k numbers from 1..n) and a
# vending machine that needs every way to make exact change from coin
# values it can reuse. Pattern: backtracking, combinations shape
# (for-loop with a start index) with a sorted-input prune.
# Run: uv run pytest 14-backtracking -k ex02


def combinations_of(n: int, k: int) -> list[list[int]]:
    """Return every combination of `k` distinct numbers chosen from
    1..n inclusive (order within a combination doesn't matter — pick
    them in increasing order to avoid duplicates).

    combinations_of(4, 2) -> [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
        (any order of the outer list)
    combinations_of(3, 0) -> [[]]

    Target: O(C(n, k) * k) time (that's the output size), O(k) space
    per combination excluding the output.
    """
    raise NotImplementedError


def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    """Return every combination of `candidates` that sums to exactly
    `target`. `candidates` are all unique, positive values, and the
    SAME candidate may be reused any number of times within one
    combination. Order within a combination doesn't matter (report
    each combination's numbers in non-decreasing order).

    Sort `candidates` first. While exploring, once the running sum
    plus the current candidate exceeds `target`, every later
    (larger) candidate would overshoot too — `break` out of the loop
    instead of trying them (the prune-on-sorted optimization).

    combination_sum([2, 3, 6], 7) -> [[2, 2, 3]]
    combination_sum([2, 3, 5], 8) -> [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    combination_sum([5], 3) -> []

    Target: O(n^(target / min(candidates))) time in the worst case
    (exponential — bounded by the target and smallest candidate),
    O(target / min(candidates)) recursion depth.
    """
    raise NotImplementedError
