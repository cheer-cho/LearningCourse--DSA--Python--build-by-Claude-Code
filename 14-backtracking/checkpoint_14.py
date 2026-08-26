# Checkpoint 14 — Meal-plan builder
#
# A restaurant's menu is a list of (dish, cost) pairs. Build three
# planning tools, one per backtracking shape from this module:
#   - all_plans_within_budget: subsets shape + prune
#   - plans_hitting_exact: combination-sum shape (reuse toggle)
#   - tasting_orders: permutations shape
#
# Run: uv run pytest 14-backtracking -k checkpoint_14


def all_plans_within_budget(menu: list[tuple[str, float]], budget: float) -> list[list[str]]:
    """Return every possible subset of dishes (by name) whose total cost
    is <= `budget`, including the empty plan. Each dish is used at most
    once per plan (a dish never repeats within one plan). `menu` has no
    duplicate dish names.

    Sort by cost first, then prune: once the running total plus the
    next (cheapest-remaining) candidate exceeds `budget`, every later
    candidate would overshoot too — stop trying more candidates at
    that level instead of checking each one.

    all_plans_within_budget([("soup", 3), ("bread", 2)], 4) ->
        [[], ["bread"], ["soup"]]   (any order; "soup"+"bread" = 5 > 4,
        so the full combo is excluded)

    Target: O(2^n) time worst case, collapsing far below that once the
    budget prunes most branches; O(n) extra space per plan.
    """
    raise NotImplementedError


def plans_hitting_exact(
    menu: list[tuple[str, float]], target: float, allow_repeats: bool
) -> list[list[str]]:
    """Return every plan (list of dish names) whose total cost equals
    `target` exactly. If `allow_repeats` is True, the same dish may be
    ordered more than once in a plan; if False, each dish is used at
    most once per plan. `menu` has no duplicate dish names.

    Same shape as `combination_sum` (ex02): sort by cost, and once the
    running total plus a candidate's cost overshoots `target`, stop
    trying later (pricier) candidates at that level.

    plans_hitting_exact([("tea", 2), ("cake", 5)], 4, True) ->
        [["tea", "tea"]]
    plans_hitting_exact([("tea", 2), ("cake", 5)], 7, False) ->
        [["tea", "cake"]]

    Target: exponential worst case, bounded by target / cheapest dish;
    O(n) extra space per plan.
    """
    raise NotImplementedError


def tasting_orders(dishes: list[str]) -> list[list[str]]:
    """Return every possible serving order (permutation) of `dishes`.
    `dishes` has at most 8 unique names.

    tasting_orders(["soup", "cake"]) ->
        [["soup", "cake"], ["cake", "soup"]]   (any order of the two)

    Target: O(n! * n) time (that's the output size), O(n) extra space.
    """
    raise NotImplementedError
