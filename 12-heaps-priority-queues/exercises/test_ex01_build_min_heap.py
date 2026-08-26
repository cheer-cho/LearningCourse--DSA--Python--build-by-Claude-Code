import random

import pytest
from ex01_build_min_heap import MinHeap


def test_push_then_peek_returns_minimum():
    h = MinHeap()
    h.push(5)
    h.push(1)
    h.push(3)
    assert h.peek() == 1


def test_size_tracks_pushes():
    h = MinHeap()
    assert h.size() == 0
    h.push(1)
    h.push(2)
    assert h.size() == 2


def test_pop_returns_ascending_order():
    h = MinHeap()
    for val in [5, 1, 3, 9, 2]:
        h.push(val)
    popped = [h.pop() for _ in range(5)]
    assert popped == [1, 2, 3, 5, 9]


def test_pop_shrinks_size():
    h = MinHeap()
    h.push(1)
    h.push(2)
    h.pop()
    assert h.size() == 1


def test_pop_on_empty_heap_raises():
    h = MinHeap()
    with pytest.raises(IndexError):
        h.pop()


def test_peek_on_empty_heap_raises():
    h = MinHeap()
    with pytest.raises(IndexError):
        h.peek()


def test_pop_order_with_many_duplicates():
    h = MinHeap()
    values = [4] * 20 + [1] * 5 + [7] * 10
    for val in values:
        h.push(val)
    popped = [h.pop() for _ in range(len(values))]
    assert popped == sorted(values)


def test_heapify_empty_list():
    h = MinHeap.heapify([])
    assert h.size() == 0


def test_heapify_matches_sorted_pop_order():
    nums = [9, 3, 7, 1, 8, 2, 5, 4, 6, 0]
    h = MinHeap.heapify(nums)
    assert h.size() == len(nums)
    popped = [h.pop() for _ in range(len(nums))]
    assert popped == sorted(nums)


def test_heapify_does_not_mutate_input():
    nums = [3, 1, 2]
    original = list(nums)
    MinHeap.heapify(nums)
    assert nums == original


def test_heapify_large_input_is_a_valid_heap():
    rng = random.Random(12)
    nums = [rng.randint(-1000, 1000) for _ in range(2_000)]
    h = MinHeap.heapify(nums)
    popped = [h.pop() for _ in range(len(nums))]
    assert popped == sorted(nums)


def test_fuzz_against_sorted_list_oracle():
    rng = random.Random(7)
    h = MinHeap()
    oracle: list[int] = []

    for _ in range(1_000):
        if oracle and rng.random() < 0.4:
            oracle.sort()
            expected = oracle.pop(0)
            assert h.pop() == expected
        else:
            val = rng.randint(-10_000, 10_000)
            h.push(val)
            oracle.append(val)
        assert h.size() == len(oracle)

    oracle.sort()
    remaining = [h.pop() for _ in range(len(oracle))]
    assert remaining == oracle
