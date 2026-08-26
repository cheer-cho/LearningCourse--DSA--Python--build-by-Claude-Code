import random

from ex05_kth_largest_stream import KthLargest


def test_kth_largest_worked_example():
    kl = KthLargest(3, [4, 5, 8, 2])
    assert kl.add(3) == 4
    assert kl.add(5) == 5
    assert kl.add(10) == 5
    assert kl.add(9) == 8


def test_kth_largest_k_one_tracks_running_max():
    kl = KthLargest(1, [3])
    assert kl.add(5) == 5
    assert kl.add(1) == 5
    assert kl.add(9) == 9


def test_kth_largest_starts_with_exactly_k_elements():
    kl = KthLargest(2, [1, 2])
    assert kl.add(3) == 2
    assert kl.add(0) == 2


def test_kth_largest_handles_duplicates():
    kl = KthLargest(2, [2, 2])
    assert kl.add(2) == 2
    assert kl.add(1) == 2


def test_kth_largest_starts_empty():
    kl = KthLargest(1, [])
    assert kl.add(-3) == -3
    assert kl.add(-1) == -1


def test_kth_largest_matches_brute_force_over_many_adds():
    rng = random.Random(21)
    k = 4
    initial = [rng.randint(-50, 50) for _ in range(k)]
    kl = KthLargest(k, list(initial))

    seen = list(initial)
    for _ in range(500):
        val = rng.randint(-50, 50)
        expected = sorted(seen + [val], reverse=True)[k - 1]
        assert kl.add(val) == expected
        seen.append(val)


def test_kth_largest_large_stream_efficiency():
    rng = random.Random(9)
    k = 50
    initial = [rng.randint(-10**6, 10**6) for _ in range(k)]
    kl = KthLargest(k, initial)
    last = None
    for _ in range(100_000):
        last = kl.add(rng.randint(-10**6, 10**6))
    assert last is not None
