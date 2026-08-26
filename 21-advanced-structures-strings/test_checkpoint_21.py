from checkpoint_21 import MetricsBoard


def test_window_total_full_range():
    board = MetricsBoard([5, 2, 8, 1, 9])
    assert board.window_total(0, 4) == 25


def test_window_total_sub_range():
    board = MetricsBoard([5, 2, 8, 1, 9])
    assert board.window_total(1, 3) == 11


def test_window_low_full_range():
    board = MetricsBoard([5, 2, 8, 1, 9])
    assert board.window_low(0, 4) == 1


def test_window_low_sub_range():
    board = MetricsBoard([5, 2, 8, 1, 9])
    assert board.window_low(0, 1) == 2


def test_record_updates_both_trees():
    board = MetricsBoard([5, 2, 8, 1, 9])
    board.record(2, 100)
    assert board.window_total(0, 4) == 117
    assert board.window_low(0, 4) == 1

    board.record(3, -50)
    assert board.window_total(0, 4) == 66
    assert board.window_low(0, 4) == -50


def test_record_single_sensor_board():
    board = MetricsBoard([7])
    assert board.window_total(0, 0) == 7
    assert board.window_low(0, 0) == 7
    board.record(0, 3)
    assert board.window_total(0, 0) == 3
    assert board.window_low(0, 0) == 3


def test_alert_scan_typical():
    board = MetricsBoard([1])
    result = board.alert_scan("ERROR: disk full ERROR: disk full", "ERROR")
    assert result == [0, 17]


def test_alert_scan_no_match():
    board = MetricsBoard([1])
    assert board.alert_scan("all clear", "ERROR") == []


def test_alert_scan_empty_signature():
    board = MetricsBoard([1])
    assert board.alert_scan("anything", "") == []


def test_alert_scan_overlapping_matches():
    board = MetricsBoard([1])
    assert board.alert_scan("aaaa", "aa") == [0, 1, 2]


def test_busiest_window_typical():
    board = MetricsBoard([1])
    assert board.busiest_window([1, 4, 2, 9, 7, 3], 3) == 19


def test_busiest_window_k_equals_length():
    board = MetricsBoard([1])
    assert board.busiest_window([2, 3, 4], 3) == 9


def test_busiest_window_negative_values():
    board = MetricsBoard([1])
    assert board.busiest_window([-5, -1, -9, -2], 2) == -6


def test_metrics_board_range_query_efficiency_large_input():
    # n = 100,000 sensors, ~50,000 mixed record/window_total/
    # window_low calls. A naive O(n)-per-update or O(n)-per-query
    # approach is infeasible at this scale; O(log n) trees are not.
    n = 100_000
    board = MetricsBoard([1] * n)

    for i in range(0, n, 2):
        board.record(i, 2)
        if i % 20_000 == 0:
            assert board.window_total(0, i) >= 0

    assert board.window_total(0, n - 1) == 150_000
    assert board.window_low(0, n - 1) == 1  # untouched odd indexes stay 1


def test_metrics_board_alert_scan_efficiency_large_input():
    # A 200,000-character log with the signature hidden near the end
    # -- infeasible for a naive O(n*m) scan at this scale, instant
    # for KMP or a rolling hash.
    board = MetricsBoard([1])
    n = 200_000
    signature = "CRITICAL_FAILURE"
    log_text = "x" * n + signature + "x" * n
    assert board.alert_scan(log_text, signature) == [n]


def test_metrics_board_busiest_window_efficiency_large_input():
    # n = 200,000 readings; a naive O(n*k) window-sum scan would be
    # far too slow here.
    board = MetricsBoard([1])
    n = 200_000
    k = 1_000
    readings = [1] * n
    readings[100_000:100_000 + k] = [5] * k
    assert board.busiest_window(readings, k) == 5 * k
