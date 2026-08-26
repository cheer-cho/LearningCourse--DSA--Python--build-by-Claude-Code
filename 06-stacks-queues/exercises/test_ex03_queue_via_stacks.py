import pytest
from ex03_queue_via_stacks import QueueFromStacks


def test_enqueue_dequeue_fifo_order():
    q = QueueFromStacks()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.dequeue() == 3


def test_dequeue_on_empty_raises():
    q = QueueFromStacks()
    with pytest.raises(IndexError):
        q.dequeue()


def test_front_peeks_without_removing():
    q = QueueFromStacks()
    q.enqueue("a")
    q.enqueue("b")
    assert q.front() == "a"
    assert q.size() == 2
    assert q.front() == "a"


def test_front_on_empty_raises():
    q = QueueFromStacks()
    with pytest.raises(IndexError):
        q.front()


def test_is_empty_and_size_track_state():
    q = QueueFromStacks()
    assert q.is_empty()
    assert q.size() == 0
    q.enqueue("a")
    assert not q.is_empty()
    assert q.size() == 1
    q.dequeue()
    assert q.is_empty()
    assert q.size() == 0


def test_interleaved_enqueue_dequeue_stays_fifo():
    q = QueueFromStacks()
    q.enqueue(1)
    q.enqueue(2)
    assert q.dequeue() == 1
    q.enqueue(3)
    assert q.dequeue() == 2
    q.enqueue(4)
    assert q.dequeue() == 3
    assert q.dequeue() == 4
    assert q.is_empty()


def test_enqueue_after_partial_drain_keeps_order():
    # Enqueuing while the "out" stack still holds items must not
    # disturb the order already poured into it.
    q = QueueFromStacks()
    for i in range(5):
        q.enqueue(i)
    assert q.dequeue() == 0
    assert q.dequeue() == 1
    q.enqueue(5)
    q.enqueue(6)
    for expected in range(2, 7):
        assert q.dequeue() == expected
    assert q.is_empty()


def test_large_interleaved_workload_is_fast():
    # Efficiency check: 100_000 enqueues followed by 100_000 dequeues
    # must stay linear overall (amortized O(1) dequeue), not blow up
    # from a per-call full re-pour.
    q = QueueFromStacks()
    for i in range(100_000):
        q.enqueue(i)
    for expected in range(100_000):
        assert q.dequeue() == expected
    assert q.is_empty()
