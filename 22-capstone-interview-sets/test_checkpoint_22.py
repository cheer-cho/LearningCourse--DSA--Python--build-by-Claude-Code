# Final mock checkpoint. Passing every test below means you have
# passed the course: you can recognize hash/prefix, union-find,
# greedy, and range-query patterns cold, with no labels attached.
import random

from checkpoint_22 import (
    VolumeTracker,
    count_ranges_with_total,
    earliest_shelter_network,
    max_nonoverlapping_meetings,
)

# --- count_ranges_with_total -------------------------------------------


def test_count_ranges_with_total_typical():
    assert count_ranges_with_total([3, -1, -2, 4, 1], 3) == 2


def test_count_ranges_with_total_empty():
    assert count_ranges_with_total([], 0) == 0


def test_count_ranges_with_total_single_element_match():
    assert count_ranges_with_total([5], 5) == 1


def test_count_ranges_with_total_no_matches():
    assert count_ranges_with_total([1, 2, 3], 100) == 0


def test_count_ranges_with_total_all_zeros_target_zero():
    assert count_ranges_with_total([0, 0, 0], 0) == 6


def test_count_ranges_with_total_matches_brute_force():
    rng = random.Random(9)
    deltas = [rng.randint(-5, 5) for _ in range(120)]
    target = 2

    brute = 0
    for i in range(len(deltas)):
        total = 0
        for j in range(i, len(deltas)):
            total += deltas[j]
            if total == target:
                brute += 1

    assert count_ranges_with_total(deltas, target) == brute


def test_count_ranges_with_total_large_efficiency():
    deltas = [1, -1] * 100_000
    assert count_ranges_with_total(deltas, 0) > 0


# --- earliest_shelter_network -------------------------------------------


def test_earliest_shelter_network_typical():
    roads = [(3, 2, 3), (0, 0, 1), (1, 1, 2)]
    assert earliest_shelter_network(4, roads) == 3


def test_earliest_shelter_network_never_connects():
    assert earliest_shelter_network(2, []) == -1


def test_earliest_shelter_network_trivial_single_shelter():
    assert earliest_shelter_network(1, []) == 0


def test_earliest_shelter_network_zero_shelters():
    assert earliest_shelter_network(0, []) == 0


def test_earliest_shelter_network_redundant_roads_ignored():
    # Extra roads after the network is already fully connected must
    # not change the earliest-connection time.
    roads = [(0, 0, 1), (1, 1, 2), (2, 2, 3), (5, 0, 3), (6, 1, 3)]
    assert earliest_shelter_network(4, roads) == 2


def test_earliest_shelter_network_large_efficiency():
    n = 50_000
    roads = [(i, i, i + 1) for i in range(n - 1)]
    random.Random(4).shuffle(roads)
    assert earliest_shelter_network(n, roads) == n - 2


# --- max_nonoverlapping_meetings -----------------------------------------


def test_max_nonoverlapping_meetings_typical():
    assert max_nonoverlapping_meetings([(1, 3), (2, 4), (3, 5)]) == 2


def test_max_nonoverlapping_meetings_touching_is_allowed():
    assert max_nonoverlapping_meetings([(1, 2), (2, 3)]) == 2


def test_max_nonoverlapping_meetings_empty():
    assert max_nonoverlapping_meetings([]) == 0


def test_max_nonoverlapping_meetings_all_overlap():
    assert max_nonoverlapping_meetings([(0, 10), (1, 9), (2, 8)]) == 1


def test_max_nonoverlapping_meetings_matches_brute_force():
    rng = random.Random(15)
    meetings = [(s, s + rng.randint(1, 5)) for s in range(8)]
    rng.shuffle(meetings)

    def overlaps(a, b):
        return a[0] < b[1] and b[0] < a[1]

    best = 0
    n = len(meetings)
    for mask in range(1 << n):
        chosen = [meetings[i] for i in range(n) if mask & (1 << i)]
        if all(not overlaps(chosen[i], chosen[j]) for i in range(len(chosen)) for j in range(i + 1, len(chosen))):
            best = max(best, len(chosen))

    assert max_nonoverlapping_meetings(meetings) == best


def test_max_nonoverlapping_meetings_large_efficiency():
    meetings = [(i, i + 1) for i in range(100_000)]
    assert max_nonoverlapping_meetings(meetings) == 100_000


# --- VolumeTracker ---------------------------------------------------------


def test_volume_tracker_basic_range_sums():
    t = VolumeTracker(5)
    t.update(0, 5)
    t.update(2, 3)
    t.update(4, 7)
    assert t.range_sum(0, 2) == 8
    assert t.range_sum(3, 4) == 7
    assert t.range_sum(0, 4) == 15


def test_volume_tracker_update_accumulates():
    t = VolumeTracker(3)
    t.update(1, 4)
    t.update(1, 6)
    assert t.range_sum(1, 1) == 10


def test_volume_tracker_negative_delta_correction():
    t = VolumeTracker(3)
    t.update(0, 10)
    t.update(0, -3)
    assert t.range_sum(0, 0) == 7


def test_volume_tracker_single_bucket_range():
    t = VolumeTracker(1)
    t.update(0, 42)
    assert t.range_sum(0, 0) == 42


def test_volume_tracker_matches_brute_force():
    rng = random.Random(17)
    n = 200
    t = VolumeTracker(n)
    brute = [0] * n
    for _ in range(500):
        idx = rng.randint(0, n - 1)
        delta = rng.randint(-10, 10)
        t.update(idx, delta)
        brute[idx] += delta

    for _ in range(50):
        left = rng.randint(0, n - 1)
        right = rng.randint(left, n - 1)
        assert t.range_sum(left, right) == sum(brute[left : right + 1])


def test_volume_tracker_large_efficiency():
    n = 200_000
    t = VolumeTracker(n)
    for i in range(0, n, 1000):
        t.update(i, 1)
    assert t.range_sum(0, n - 1) == n // 1000
