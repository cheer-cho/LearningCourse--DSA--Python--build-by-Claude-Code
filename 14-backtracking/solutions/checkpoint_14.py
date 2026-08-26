def all_plans_within_budget(menu: list[tuple[str, float]], budget: float) -> list[list[str]]:
    # Pattern: subsets shape (record every node, not just leaves) with
    # the sorted-ascending prune: once running total + next cost
    # overshoots budget, every later (pricier) candidate overshoots too.
    # Why: sorting makes "overshoot" monotonic across the remaining
    # loop, so a single `break` collapses whole unreachable subtrees —
    # essential once `menu` is large (e.g. 30 items: 2^30 unpruned).
    # Complexity: O(2^n) worst case, far less once the budget prunes.
    menu_sorted = sorted(menu, key=lambda item: item[1])
    results: list[list[str]] = []
    path: list[str] = []

    def backtrack(start: int, running_cost: float) -> None:
        results.append(path.copy())
        for i in range(start, len(menu_sorted)):
            name, cost = menu_sorted[i]
            if running_cost + cost > budget:
                break  # sorted ascending: every later dish overshoots too
            path.append(name)
            backtrack(i + 1, running_cost + cost)
            path.pop()

    backtrack(0, 0.0)
    return results


def plans_hitting_exact(
    menu: list[tuple[str, float]], target: float, allow_repeats: bool
) -> list[list[str]]:
    # Pattern: combination-sum shape. `allow_repeats` toggles whether
    # the next recursion starts at `i` (reuse allowed) or `i + 1`
    # (each dish once) — the same reuse-vs-no-reuse choice as ex02.
    # Why: sorting + break-on-overshoot prunes exactly as in ex02.
    # Complexity: exponential worst case, bounded by target / min cost.
    menu_sorted = sorted(menu, key=lambda item: item[1])
    results: list[list[str]] = []
    path: list[str] = []
    epsilon = 1e-9

    def backtrack(start: int, remaining: float) -> None:
        if abs(remaining) < epsilon:
            results.append(path.copy())
            return
        for i in range(start, len(menu_sorted)):
            name, cost = menu_sorted[i]
            if cost > remaining + epsilon:
                break
            path.append(name)
            next_start = i if allow_repeats else i + 1
            backtrack(next_start, remaining - cost)
            path.pop()

    backtrack(0, target)
    return results


def tasting_orders(dishes: list[str]) -> list[list[str]]:
    # Pattern: permutations shape (used-tracker; every not-yet-placed
    # dish is a candidate for the next slot).
    # Complexity: O(n! * n) time/output, O(n) extra space.
    results: list[list[str]] = []
    path: list[str] = []
    used = [False] * len(dishes)

    def backtrack() -> None:
        if len(path) == len(dishes):
            results.append(path.copy())
            return
        for i in range(len(dishes)):
            if used[i]:
                continue
            used[i] = True
            path.append(dishes[i])
            backtrack()
            path.pop()
            used[i] = False

    backtrack()
    return results
