from ex02_call_tree_fib import fib_memo, fib_naive


class Counter:
    """Simple call counter used as the `tick` callback in tests."""

    def __init__(self) -> None:
        self.count = 0

    def __call__(self) -> None:
        self.count += 1


def test_fib_naive_base_case_zero():
    counter = Counter()
    assert fib_naive(0, counter) == 0
    assert counter.count == 1


def test_fib_naive_base_case_one():
    counter = Counter()
    assert fib_naive(1, counter) == 1
    assert counter.count == 1


def test_fib_naive_value_and_call_count_for_five():
    counter = Counter()
    assert fib_naive(5, counter) == 5
    assert counter.count == 15


def test_fib_naive_value_and_call_count_for_ten():
    counter = Counter()
    assert fib_naive(10, counter) == 55
    assert counter.count == 177


def test_fib_memo_base_case_zero():
    counter = Counter()
    assert fib_memo(0, counter) == 0
    assert counter.count == 1


def test_fib_memo_base_case_one():
    counter = Counter()
    assert fib_memo(1, counter) == 1
    # k=1 is itself a base case, so it never separately computes k=0.
    assert counter.count == 1


def test_fib_memo_tick_count_is_n_plus_one():
    counter = Counter()
    assert fib_memo(10, counter) == 55
    assert counter.count == 11


def test_fib_memo_matches_naive_value_for_larger_n():
    naive_counter = Counter()
    memo_counter = Counter()
    assert fib_naive(20, naive_counter) == fib_memo(20, memo_counter)
    assert memo_counter.count == 21
    # The whole point: naive's call tree dwarfs memo's linear tick count.
    assert naive_counter.count > memo_counter.count * 100


def test_fib_memo_fresh_cache_each_call():
    counter_a = Counter()
    counter_b = Counter()
    fib_memo(5, counter_a)
    fib_memo(5, counter_b)
    # Each top-level call starts its own cache, so tick counts repeat.
    assert counter_a.count == counter_b.count == 6
