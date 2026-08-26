import pytest
from ex04_min_stack import MinStack


def test_get_min_after_pushes():
    s = MinStack()
    s.push(5)
    s.push(3)
    s.push(7)
    assert s.get_min() == 3


def test_get_min_updates_after_pop_restores_previous_min():
    s = MinStack()
    s.push(5)
    s.push(3)
    s.push(7)
    assert s.get_min() == 3
    s.pop()  # removes 7
    assert s.get_min() == 3
    s.pop()  # removes 3
    assert s.get_min() == 5


def test_get_min_handles_duplicate_minimums():
    s = MinStack()
    s.push(2)
    s.push(2)
    s.push(3)
    assert s.get_min() == 2
    s.pop()  # removes 3
    assert s.get_min() == 2
    s.pop()  # removes one of the 2s, the other is still the min
    assert s.get_min() == 2


def test_push_pop_lifo_order():
    s = MinStack()
    s.push(1)
    s.push(2)
    assert s.pop() == 2
    assert s.pop() == 1


def test_peek_does_not_remove():
    s = MinStack()
    s.push(4)
    s.push(1)
    assert s.peek() == 1
    assert s.peek() == 1


def test_pop_on_empty_raises():
    s = MinStack()
    with pytest.raises(IndexError):
        s.pop()


def test_peek_on_empty_raises():
    s = MinStack()
    with pytest.raises(IndexError):
        s.peek()


def test_get_min_on_empty_raises():
    s = MinStack()
    with pytest.raises(IndexError):
        s.get_min()


def test_size_and_is_empty_track_state():
    s = MinStack()
    assert s.is_empty()
    assert s.size() == 0
    s.push(3)
    s.push(9)
    assert not s.is_empty()
    assert s.size() == 2
    s.pop()
    assert s.size() == 1
    s.pop()
    assert s.is_empty()
    assert s.size() == 0


def test_heavily_interleaved_ops():
    s = MinStack()
    s.push(10)
    s.push(5)
    assert s.get_min() == 5
    s.push(2)
    assert s.get_min() == 2
    s.pop()  # removes 2
    assert s.get_min() == 5
    s.push(1)
    s.push(1)
    assert s.get_min() == 1
    s.pop()
    assert s.get_min() == 1
    s.pop()
    assert s.get_min() == 5
    s.pop()  # removes 5
    assert s.get_min() == 10
