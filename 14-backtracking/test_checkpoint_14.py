from checkpoint_14 import all_plans_within_budget, plans_hitting_exact, tasting_orders


def as_set(list_of_lists: list[list[str]]) -> set[frozenset[str]]:
    return {frozenset(item) for item in list_of_lists}


def test_all_plans_within_budget_basic():
    menu = [("soup", 3.0), ("bread", 2.0)]
    result = all_plans_within_budget(menu, 4.0)
    expected = as_set([[], ["bread"], ["soup"]])
    assert as_set(result) == expected


def test_all_plans_within_budget_includes_empty_plan():
    result = all_plans_within_budget([("cake", 5.0)], 1.0)
    assert result == [[]]


def test_all_plans_within_budget_generous_budget_includes_everything():
    menu = [("tea", 1.0), ("soup", 2.0)]
    result = all_plans_within_budget(menu, 100.0)
    expected = as_set([[], ["tea"], ["soup"], ["tea", "soup"]])
    assert as_set(result) == expected


def test_all_plans_within_budget_every_plan_is_within_budget():
    menu = [("a", 4.0), ("b", 5.0), ("c", 1.0), ("d", 7.0)]
    costs = dict(menu)
    for plan in all_plans_within_budget(menu, 10.0):
        assert sum(costs[name] for name in plan) <= 10.0


def test_all_plans_within_budget_large_menu_is_fast_when_pruned():
    # 30 items with strictly increasing cost + a small budget: unpruned
    # this is 2**30 subsets (~1 billion) to check; sort + break-on-
    # overshoot means only the first handful of (cheap) items are ever
    # explored, so this must return almost instantly.
    menu = [(f"dish{i}", float(i)) for i in range(1, 31)]  # costs 1..30
    result = all_plans_within_budget(menu, 6.0)
    costs = dict(menu)
    assert len(result) > 0
    for plan in result:
        assert sum(costs[name] for name in plan) <= 6.0
    # every plan must be drawn only from the cheap dishes (cost <= 6)
    for plan in result:
        assert all(costs[name] <= 6.0 for name in plan)


def test_plans_hitting_exact_with_repeats():
    menu = [("tea", 2.0), ("cake", 5.0)]
    result = plans_hitting_exact(menu, 4.0, allow_repeats=True)
    assert result == [["tea", "tea"]]


def test_plans_hitting_exact_without_repeats():
    menu = [("tea", 2.0), ("cake", 5.0)]
    result = plans_hitting_exact(menu, 7.0, allow_repeats=False)
    assert result == [["tea", "cake"]]


def test_plans_hitting_exact_no_solution():
    # with repeats allowed, tea (2.0) and cake (5.0) can only ever sum
    # to an even amount, an odd multiple of 5, or a mix like 2a + 5b —
    # 3.0 is unreachable by any combination of the two.
    menu = [("tea", 2.0), ("cake", 5.0)]
    assert plans_hitting_exact(menu, 3.0, allow_repeats=True) == []


def test_plans_hitting_exact_every_plan_sums_to_target():
    menu = [("a", 1.0), ("b", 2.0), ("c", 3.0)]
    for plan in plans_hitting_exact(menu, 6.0, allow_repeats=True):
        costs = dict(menu)
        assert sum(costs[name] for name in plan) == 6.0


def test_tasting_orders_two_dishes():
    result = tasting_orders(["soup", "cake"])
    expected = {("soup", "cake"), ("cake", "soup")}
    assert {tuple(order) for order in result} == expected


def test_tasting_orders_count_is_n_factorial():
    dishes = ["a", "b", "c", "d"]
    assert len(tasting_orders(dishes)) == 24


def test_tasting_orders_single_dish():
    assert tasting_orders(["only"]) == [["only"]]


def test_tasting_orders_every_order_uses_each_dish_once():
    dishes = ["a", "b", "c"]
    for order in tasting_orders(dishes):
        assert sorted(order) == sorted(dishes)
