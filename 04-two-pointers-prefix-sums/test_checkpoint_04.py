from checkpoint_04 import GAP_SENTINEL, RangeGain, balanced_checkpoint, compact_gaps, flat_pairs


def test_flat_pairs_typical():
    assert flat_pairs([100, 150, 200, 250, 300], 450) == [(1, 4), (2, 3)]


def test_flat_pairs_no_match():
    assert flat_pairs([1, 2, 3], 10) == []


def test_flat_pairs_empty_list():
    assert flat_pairs([], 5) == []


def test_flat_pairs_multiple_pairs():
    assert flat_pairs([1, 2, 3, 4], 5) == [(0, 3), (1, 2)]


def test_compact_gaps_typical():
    readings = [10, GAP_SENTINEL, 12, GAP_SENTINEL, 15]
    count = compact_gaps(readings)
    assert count == 3
    assert readings[:count] == [10, 12, 15]


def test_compact_gaps_no_gaps():
    readings = [1, 2, 3]
    count = compact_gaps(readings)
    assert count == 3
    assert readings[:count] == [1, 2, 3]


def test_compact_gaps_all_gaps():
    readings = [GAP_SENTINEL, GAP_SENTINEL]
    count = compact_gaps(readings)
    assert count == 0


def test_compact_gaps_empty_list():
    readings: list[int] = []
    count = compact_gaps(readings)
    assert count == 0


def test_range_gain_typical_queries():
    rg = RangeGain([3, -1, 2, -4, 5])
    assert rg.query(0, 2) == 4
    assert rg.query(1, 4) == 2
    assert rg.query(0, 4) == 5


def test_range_gain_single_segment():
    rg = RangeGain([7])
    assert rg.query(0, 0) == 7


def test_balanced_checkpoint_typical():
    assert balanced_checkpoint([2, 1, -1, 4, 2, -3]) == 1


def test_balanced_checkpoint_no_balance_point():
    assert balanced_checkpoint([1, 2, 3]) == -1


def test_balanced_checkpoint_single_segment():
    assert balanced_checkpoint([0]) == 0


def test_range_gain_efficiency_many_queries_on_large_survey():
    n = 100_000
    readings = [1] * n
    rg = RangeGain(readings)
    # Every inclusive range (i, j) of all-1 deltas nets (j - i + 1).
    # 100_000 O(1) queries here would be infeasible if each one
    # re-summed its slice from scratch.
    for i in range(0, n, 2):
        j = n - 1 - (i % 4)
        if j <= i:
            continue
        assert rg.query(i, j) == j - i + 1
