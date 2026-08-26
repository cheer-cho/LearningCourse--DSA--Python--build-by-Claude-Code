import time

import pytest
from checkpoint_07 import PlayQueue


def test_add_last_and_play_next_is_fifo():
    q = PlayQueue(history_capacity=10)
    q.add_last("a")
    q.add_last("b")
    q.add_last("c")
    assert q.play_next() == "a"
    assert q.play_next() == "b"
    assert q.play_next() == "c"


def test_play_next_on_empty_queue_raises():
    q = PlayQueue(history_capacity=10)
    with pytest.raises(IndexError):
        q.play_next()


def test_play_now_jumps_the_line():
    q = PlayQueue(history_capacity=10)
    q.add_last("a")
    q.add_last("b")
    q.play_now("urgent")
    assert q.play_next() == "urgent"
    assert q.play_next() == "a"
    assert q.play_next() == "b"


def test_play_now_does_not_appear_in_history_until_played():
    q = PlayQueue(history_capacity=10)
    q.play_now("a")
    assert q.history(5) == []
    q.play_next()
    assert q.history(5) == ["a"]


def test_remove_first_occurrence_only():
    q = PlayQueue(history_capacity=10)
    q.add_last("a")
    q.add_last("b")
    q.add_last("a")
    assert q.remove("a") is True
    assert q.play_next() == "b"
    assert q.play_next() == "a"


def test_remove_missing_song_returns_false_and_leaves_queue_untouched():
    q = PlayQueue(history_capacity=10)
    q.add_last("a")
    q.add_last("b")
    assert q.remove("missing") is False
    assert q.play_next() == "a"
    assert q.play_next() == "b"


def test_remove_preserves_relative_order_of_remaining_songs():
    q = PlayQueue(history_capacity=10)
    for song in ("a", "b", "c", "d"):
        q.add_last(song)
    q.remove("b")
    played = [q.play_next() for _ in range(3)]
    assert played == ["a", "c", "d"]


def test_history_is_most_recent_first():
    q = PlayQueue(history_capacity=10)
    for song in ("a", "b", "c"):
        q.add_last(song)
    q.play_next()  # a
    q.play_next()  # b
    q.play_next()  # c
    assert q.history(3) == ["c", "b", "a"]


def test_history_k_larger_than_available_returns_what_exists():
    q = PlayQueue(history_capacity=10)
    q.add_last("a")
    q.play_next()
    assert q.history(5) == ["a"]


def test_history_capped_at_history_capacity_evicts_oldest_play():
    q = PlayQueue(history_capacity=2)
    for song in ("a", "b", "c"):
        q.add_last(song)
        q.play_next()
    # capacity 2: only the two most recent plays are remembered
    assert q.history(10) == ["c", "b"]


def test_history_records_repeated_plays_of_the_same_song():
    q = PlayQueue(history_capacity=10)
    q.add_last("a")
    q.play_next()
    q.add_last("a")
    q.play_next()
    assert q.history(10) == ["a", "a"]


def test_history_returns_at_most_k_even_with_more_capacity():
    q = PlayQueue(history_capacity=10)
    for song in ("a", "b", "c", "d"):
        q.add_last(song)
        q.play_next()
    assert q.history(2) == ["d", "c"]


def test_mixed_ops_efficiency_and_final_state():
    # Mixed-op efficiency test: add_last/play_next/play_now must stay
    # O(1) even under heavy sustained use — remove/history are O(n)/O(k)
    # by design (see their docstrings), so they're only sprinkled in
    # occasionally here rather than scaled with the main loop.
    q = PlayQueue(history_capacity=50)

    start = time.perf_counter()
    for i in range(50_000):
        q.add_last(f"song-{i}")
        if i % 4 == 0:
            q.play_now(f"urgent-{i}")
        if i % 2 == 0:
            q.play_next()
        if i % 5_000 == 0 and i > 0:
            q.remove(f"song-{i - 1}")
    elapsed = time.perf_counter() - start

    assert elapsed < 8.0  # generous sanity bound, not a tight benchmark
    assert len(q.history(50)) == 50
    # plenty of songs are still queued; every remaining play_next call
    # must still succeed without error
    for _ in range(100):
        q.play_next()
