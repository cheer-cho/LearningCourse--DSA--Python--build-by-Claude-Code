import pytest
from ex01_build_stack_queue import CircularQueue, Stack

# ---- Stack -----------------------------------------------------------


def test_stack_push_pop_lifo_order():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    assert s.pop() == 3
    assert s.pop() == 2
    assert s.pop() == 1


def test_stack_peek_does_not_remove():
    s = Stack()
    s.push(10)
    s.push(20)
    assert s.peek() == 20
    assert s.peek() == 20
    assert s.size() == 2


def test_stack_pop_on_empty_raises_underflow():
    s = Stack()
    with pytest.raises(IndexError):
        s.pop()


def test_stack_peek_on_empty_raises_underflow():
    s = Stack()
    with pytest.raises(IndexError):
        s.peek()


def test_stack_size_and_is_empty_track_state():
    s = Stack()
    assert s.is_empty()
    assert s.size() == 0
    s.push("a")
    assert not s.is_empty()
    assert s.size() == 1
    s.pop()
    assert s.is_empty()
    assert s.size() == 0


def test_stack_push_pop_interleaved():
    s = Stack()
    s.push(1)
    s.push(2)
    assert s.pop() == 2
    s.push(3)
    s.push(4)
    assert s.pop() == 4
    assert s.pop() == 3
    assert s.pop() == 1
    assert s.is_empty()


# ---- CircularQueue -----------------------------------------------------


def test_circular_queue_fifo_order():
    q = CircularQueue(capacity=4)
    q.enqueue("a")
    q.enqueue("b")
    q.enqueue("c")
    assert q.dequeue() == "a"
    assert q.dequeue() == "b"
    assert q.dequeue() == "c"


def test_circular_queue_front_does_not_remove():
    q = CircularQueue(capacity=3)
    q.enqueue(1)
    q.enqueue(2)
    assert q.front() == 1
    assert q.front() == 1
    assert q.size() == 2


def test_circular_queue_wraps_around_small_capacity():
    q = CircularQueue(capacity=3)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.dequeue() == 1
    q.enqueue(4)  # backing slot 0 gets reused here
    assert q.dequeue() == 2
    assert q.dequeue() == 3
    assert q.dequeue() == 4
    assert q.is_empty()


def test_circular_queue_enqueue_on_full_raises_overflow():
    q = CircularQueue(capacity=2)
    q.enqueue(1)
    q.enqueue(2)
    assert q.is_full()
    with pytest.raises(OverflowError):
        q.enqueue(3)


def test_circular_queue_dequeue_on_empty_raises_underflow():
    q = CircularQueue(capacity=2)
    with pytest.raises(IndexError):
        q.dequeue()


def test_circular_queue_front_on_empty_raises_underflow():
    q = CircularQueue(capacity=2)
    with pytest.raises(IndexError):
        q.front()


def test_circular_queue_is_full_and_is_empty():
    q = CircularQueue(capacity=1)
    assert q.is_empty()
    assert not q.is_full()
    q.enqueue(42)
    assert not q.is_empty()
    assert q.is_full()
    q.dequeue()
    assert q.is_empty()


def test_circular_queue_many_wraparound_ops_stay_fifo_and_fast():
    # Efficiency test: a shifting-based queue costs O(capacity) per
    # dequeue; a real ring buffer costs O(1). capacity=2000 with
    # 100_000 forced wrap-arounds punishes the O(n) approach (order of
    # 2*10^8 element moves) while a correct O(1) implementation finishes
    # instantly.
    capacity = 2000
    q = CircularQueue(capacity=capacity)
    for i in range(capacity):
        q.enqueue(i)

    next_value = capacity
    for expected in range(100_000):
        assert q.dequeue() == expected
        q.enqueue(next_value)
        next_value += 1

    assert q.size() == capacity
    assert q.front() == 100_000
