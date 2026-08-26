from ex03_naive_vs_fast import has_duplicate_fast, has_duplicate_naive


class _Counter:
    def __init__(self) -> None:
        self.count = 0

    def tick(self) -> None:
        self.count += 1


def test_has_duplicate_naive_detects_a_duplicate():
    counter = _Counter()
    assert has_duplicate_naive([1, 2, 3, 2], counter.tick) is True


def test_has_duplicate_naive_no_duplicate_returns_false():
    counter = _Counter()
    assert has_duplicate_naive([1, 2, 3, 4], counter.tick) is False


def test_has_duplicate_naive_empty_and_single_tick_zero_times():
    counter = _Counter()
    assert has_duplicate_naive([], counter.tick) is False
    assert counter.count == 0

    counter = _Counter()
    assert has_duplicate_naive([5], counter.tick) is False
    assert counter.count == 0


def test_has_duplicate_naive_counts_every_pair_when_forced_to_full_scan():
    # No duplicate exists, so the naive version cannot shortcut -- it
    # must compare all n * (n - 1) / 2 pairs. This is what "forces
    # honesty": a cheating O(n) implementation would tick far less.
    counter = _Counter()
    nums = list(range(20))
    has_duplicate_naive(nums, counter.tick)
    assert counter.count == 20 * 19 // 2


def test_has_duplicate_fast_detects_a_duplicate():
    assert has_duplicate_fast([1, 2, 3, 2]) is True


def test_has_duplicate_fast_no_duplicate():
    assert has_duplicate_fast([1, 2, 3, 4]) is False


def test_has_duplicate_fast_empty_and_single():
    assert has_duplicate_fast([]) is False
    assert has_duplicate_fast([5]) is False


def test_has_duplicate_fast_handles_negatives_and_zero():
    assert has_duplicate_fast([-1, 0, 1, -1]) is True


def test_has_duplicate_fast_large_input_is_fast():
    nums = list(range(200_000))
    assert has_duplicate_fast(nums) is False
    nums[-1] = 0  # introduce a duplicate near the far end of the scan
    assert has_duplicate_fast(nums) is True
