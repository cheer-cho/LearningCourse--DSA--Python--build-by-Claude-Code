from checkpoint_17 import coffee_run, merge_busy, plan_day, rooms_needed


def test_plan_day_typical():
    talks = [("A", 1, 3), ("B", 2, 4), ("C", 3, 6), ("D", 5, 7)]
    assert plan_day(talks) == ["A", "C"]


def test_plan_day_empty():
    assert plan_day([]) == []


def test_plan_day_single_talk():
    assert plan_day([("Keynote", 9, 10)]) == ["Keynote"]


def test_plan_day_all_disjoint_attends_all():
    talks = [("A", 1, 2), ("B", 3, 4), ("C", 5, 6)]
    assert plan_day(talks) == ["A", "B", "C"]


def test_plan_day_all_overlapping_attends_one():
    talks = [("A", 1, 5), ("B", 1, 5), ("C", 1, 5)]
    assert len(plan_day(talks)) == 1


def test_plan_day_touching_talks_both_attendable():
    talks = [("A", 1, 2), ("B", 2, 3)]
    assert plan_day(talks) == ["A", "B"]


def test_rooms_needed_typical():
    talks = [("A", 0, 30), ("B", 5, 10), ("C", 15, 20)]
    assert rooms_needed(talks) == 2


def test_rooms_needed_touching_shares_room():
    assert rooms_needed([("A", 1, 2), ("B", 2, 3)]) == 1


def test_rooms_needed_empty():
    assert rooms_needed([]) == 0


def test_rooms_needed_no_overlap_needs_one():
    talks = [("A", 1, 2), ("B", 5, 6)]
    assert rooms_needed(talks) == 1


def test_rooms_needed_efficiency_large_input():
    n = 100_000
    talks = [(f"t{i}", 0, 1000) for i in range(n // 2)]
    talks += [(f"u{i}", 2000 + i, 2001 + i) for i in range(n // 2)]
    assert rooms_needed(talks) == n // 2


def test_merge_busy_typical():
    calendars = [[(1, 3), (5, 8)], [(2, 4), (9, 10)]]
    result = merge_busy(calendars)
    assert result == [(1, 4), (5, 8), (9, 10)]


def test_merge_busy_empty_calendars():
    assert merge_busy([[], []]) == []


def test_merge_busy_no_calendars():
    assert merge_busy([]) == []


def test_merge_busy_touching_stays_separate():
    result = merge_busy([[(1, 2)], [(2, 3)]])
    assert result == [(1, 2), (2, 3)]


def test_merge_busy_single_calendar_with_overlaps():
    result = merge_busy([[(1, 5), (3, 7)]])
    assert result == [(1, 7)]


def test_merge_busy_efficiency_large_input():
    n = 50_000
    calendars = [[(i, i + 2)] for i in range(n)]  # heavily overlapping chain
    result = merge_busy(calendars)
    assert result == [(0, n + 1)]


def test_coffee_run_typical():
    assert coffee_run([3, -1, -2, 5, 2, -4, 3]) == (7, 0, 4)


def test_coffee_run_single_hour():
    assert coffee_run([-2]) == (-2, 0, 0)


def test_coffee_run_all_positive_is_whole_day():
    result = coffee_run([1, 2, 3])
    assert result == (6, 0, 2)


def test_coffee_run_bounds_are_consistent_with_total():
    energy = [4, -3, 5, -1, 2, -6, 3]
    best, start, end = coffee_run(energy)
    assert sum(energy[start : end + 1]) == best


def test_coffee_run_efficiency_large_input():
    n = 200_000
    energy = [-1] * n
    energy[100_000:100_050] = [10] * 50
    assert coffee_run(energy)[0] == 500
