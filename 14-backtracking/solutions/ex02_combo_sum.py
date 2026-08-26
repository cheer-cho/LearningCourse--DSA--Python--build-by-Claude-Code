def combinations_of(n: int, k: int) -> list[list[int]]:
    # Pattern: backtracking, combinations shape (for-loop with a start
    # index; only record complete-length paths, unlike subsets).
    # Why: order doesn't matter, so `start` forbids re-picking an
    # earlier number and forbids generating the same set twice.
    # Complexity: O(C(n, k) * k) time (that's the output size).
    results: list[list[int]] = []
    path: list[int] = []

    def backtrack(start: int) -> None:
        if len(path) == k:
            results.append(path.copy())
            return
        for i in range(start, n + 1):
            path.append(i)
            backtrack(i + 1)
            path.pop()

    backtrack(1)
    return results


def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    # Pattern: backtracking, combinations shape with reuse (recurse with
    # `start = i`, not `i + 1`) plus the sorted-prune: once the running
    # sum + a candidate overshoots, every later (larger) candidate would
    # too, so `break` instead of `continue`.
    # Why: sorting makes "overshoot" monotonic across the remaining loop.
    # Complexity: exponential, bounded by target / min(candidates).
    candidates_sorted = sorted(candidates)
    results: list[list[int]] = []
    path: list[int] = []

    def backtrack(start: int, remaining: int) -> None:
        if remaining == 0:
            results.append(path.copy())
            return
        for i in range(start, len(candidates_sorted)):
            candidate = candidates_sorted[i]
            if candidate > remaining:
                break  # sorted ascending: every later candidate overshoots too
            path.append(candidate)
            backtrack(i, remaining - candidate)  # i, not i + 1: reuse allowed
            path.pop()

    backtrack(0, target)
    return results
