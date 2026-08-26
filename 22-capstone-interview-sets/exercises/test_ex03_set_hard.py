import random

import pytest
from ex03_set_hard import (
    LatencyMedianTracker,
    cheapest_delivery_with_stops,
    find_signature_occurrences,
    max_survival_value,
)

# --- max_survival_value -----------------------------------------------


def test_max_survival_value_typical():
    assert max_survival_value([1, 3, 4, 5], [1, 4, 5, 7], 7) == 9


def test_max_survival_value_nothing_fits():
    assert max_survival_value([2, 2, 2], [3, 3, 3], 1) == 0


def test_max_survival_value_zero_capacity():
    assert max_survival_value([1, 2], [10, 20], 0) == 0


def test_max_survival_value_take_everything():
    assert max_survival_value([1, 1, 1], [5, 5, 5], 3) == 15


def test_max_survival_value_single_item():
    assert max_survival_value([4], [10], 4) == 10
    assert max_survival_value([5], [10], 4) == 0


def test_max_survival_value_matches_brute_force_small_cases():
    rng = random.Random(3)
    for _ in range(20):
        n = rng.randint(1, 8)
        weights = [rng.randint(1, 6) for _ in range(n)]
        values = [rng.randint(1, 10) for _ in range(n)]
        capacity = rng.randint(0, 15)

        best = 0
        for mask in range(1 << n):
            w = sum(weights[i] for i in range(n) if mask & (1 << i))
            if w <= capacity:
                v = sum(values[i] for i in range(n) if mask & (1 << i))
                best = max(best, v)

        assert max_survival_value(weights, values, capacity) == best


def test_max_survival_value_large_efficiency():
    n = 300
    weights = list(range(1, n + 1))
    values = list(range(1, n + 1))
    capacity = 15_000
    result = max_survival_value(weights, values, capacity)
    assert result > 0


# --- cheapest_delivery_with_stops ------------------------------------------


def test_cheapest_delivery_with_stops_via_intermediate_hub():
    routes = [(0, 1, 100), (1, 2, 100), (0, 2, 500)]
    assert cheapest_delivery_with_stops(4, routes, 0, 2, 1) == 200


def test_cheapest_delivery_with_stops_zero_stops_forces_direct():
    routes = [(0, 1, 100), (1, 2, 100), (0, 2, 500)]
    assert cheapest_delivery_with_stops(4, routes, 0, 2, 0) == 500


def test_cheapest_delivery_with_stops_unreachable():
    assert cheapest_delivery_with_stops(2, [], 0, 1, 5) == -1


def test_cheapest_delivery_with_stops_same_source_and_destination():
    assert cheapest_delivery_with_stops(3, [(0, 1, 5)], 0, 0, 2) == 0


def test_cheapest_delivery_with_stops_not_enough_stops():
    routes = [(0, 1, 1), (1, 2, 1), (2, 3, 1)]
    # 0 -> 3 needs 2 intermediate hops (via 1 and 2); only 1 allowed.
    assert cheapest_delivery_with_stops(4, routes, 0, 3, 1) == -1
    assert cheapest_delivery_with_stops(4, routes, 0, 3, 2) == 3


def test_cheapest_delivery_with_stops_large_efficiency():
    n = 300
    routes = [(i, i + 1, 1) for i in range(n - 1)]
    assert cheapest_delivery_with_stops(n, routes, 0, n - 1, n) == n - 1
    assert cheapest_delivery_with_stops(n, routes, 0, n - 1, 2) == -1


# --- LatencyMedianTracker --------------------------------------------------


def test_latency_median_tracker_running_sequence():
    t = LatencyMedianTracker()
    t.add(5)
    assert t.median() == 5
    t.add(2)
    assert t.median() == 3.5
    t.add(8)
    assert t.median() == 5


def test_latency_median_tracker_empty_raises():
    t = LatencyMedianTracker()
    with pytest.raises(ValueError):
        t.median()


def test_latency_median_tracker_all_equal_values():
    t = LatencyMedianTracker()
    for _ in range(4):
        t.add(10)
    assert t.median() == 10


def test_latency_median_tracker_matches_brute_force():
    rng = random.Random(11)
    t = LatencyMedianTracker()
    seen: list[float] = []
    for _ in range(500):
        v = rng.uniform(0, 1000)
        t.add(v)
        seen.append(v)
        sorted_seen = sorted(seen)
        mid = len(sorted_seen) // 2
        if len(sorted_seen) % 2 == 1:
            expected = sorted_seen[mid]
        else:
            expected = (sorted_seen[mid - 1] + sorted_seen[mid]) / 2
        assert t.median() == pytest.approx(expected)


def test_latency_median_tracker_large_efficiency():
    rng = random.Random(21)
    t = LatencyMedianTracker()
    for _ in range(200_000):
        t.add(rng.uniform(0, 1000))
    assert isinstance(t.median(), float)


# --- find_signature_occurrences --------------------------------------------


def test_find_signature_occurrences_typical():
    assert find_signature_occurrences("abcabcabc", "abc") == [0, 3, 6]


def test_find_signature_occurrences_overlapping():
    assert find_signature_occurrences("aaaaa", "aa") == [0, 1, 2, 3]


def test_find_signature_occurrences_not_found():
    assert find_signature_occurrences("hello", "xyz") == []


def test_find_signature_occurrences_signature_equals_log():
    assert find_signature_occurrences("match", "match") == [0]


def test_find_signature_occurrences_single_char_signature():
    assert find_signature_occurrences("banana", "a") == [1, 3, 5]


def test_find_signature_occurrences_large_efficiency():
    log = "x" * 500_000 + "signature" + "x" * 500_000
    # A naive O(n*m) scan over a million-character log would be far too
    # slow to run in a test; KMP/Rabin-Karp finishes in O(n + m).
    assert find_signature_occurrences(log, "signature") == [500_000]
