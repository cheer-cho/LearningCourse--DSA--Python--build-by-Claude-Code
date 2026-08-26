from ex01_stairs_framework import (
    climb_ways_memo,
    climb_ways_naive,
    climb_ways_optimized,
    climb_ways_table,
)


class Counter:
    """Simple call counter used as the `tick` callback in tests."""

    def __init__(self) -> None:
        self.count = 0

    def __call__(self) -> None:
        self.count += 1


# --- naive: value correctness + exponential-ish call counts ---


def test_naive_base_case_zero():
    counter = Counter()
    assert climb_ways_naive(0, counter) == 1
    assert counter.count == 1


def test_naive_base_case_one():
    counter = Counter()
    assert climb_ways_naive(1, counter) == 1
    assert counter.count == 1


def test_naive_value_and_call_count_for_five():
    counter = Counter()
    assert climb_ways_naive(5, counter) == 8
    assert counter.count == 15


def test_naive_value_and_call_count_for_ten():
    counter = Counter()
    assert climb_ways_naive(10, counter) == 89
    assert counter.count == 177


# --- memo: value correctness + linear tick count ---


def test_memo_base_case_zero():
    counter = Counter()
    assert climb_ways_memo(0, counter) == 1
    assert counter.count == 1


def test_memo_tick_count_is_n_plus_one():
    counter = Counter()
    assert climb_ways_memo(10, counter) == 89
    assert counter.count == 11


def test_memo_ticks_at_most_double_n():
    counter = Counter()
    climb_ways_memo(30, counter)
    assert counter.count <= 2 * 30


def test_memo_matches_naive_value_but_far_fewer_calls():
    naive_counter = Counter()
    memo_counter = Counter()
    assert climb_ways_naive(20, naive_counter) == climb_ways_memo(20, memo_counter)
    assert memo_counter.count == 21
    assert naive_counter.count > memo_counter.count * 100


def test_memo_fresh_cache_each_call():
    counter_a = Counter()
    counter_b = Counter()
    climb_ways_memo(5, counter_a)
    climb_ways_memo(5, counter_b)
    assert counter_a.count == counter_b.count == 6


# --- table: value correctness across small and larger n ---


def test_table_base_cases():
    assert climb_ways_table(0) == 1
    assert climb_ways_table(1) == 1


def test_table_matches_naive_for_small_n():
    for n in range(2, 11):
        counter = Counter()
        assert climb_ways_table(n) == climb_ways_naive(n, counter)


def test_table_handles_larger_n_without_recursion_limit():
    # n = 1_000 would blow a naive recursive call stack territory; the
    # table is a plain loop, so it's unaffected.
    assert climb_ways_table(1_000) > 0


# --- optimized: matches table, O(1) space ---


def test_optimized_matches_table_across_range():
    for n in range(31):
        assert climb_ways_optimized(n) == climb_ways_table(n)


def test_optimized_handles_large_n():
    assert climb_ways_optimized(1_000) == climb_ways_table(1_000)
