import time

import pytest
from ex01_dynamic_array import DynamicArray


def test_starts_empty_with_capacity_one():
    arr: DynamicArray[int] = DynamicArray()
    assert arr.size() == 0
    assert len(arr) == 0
    assert arr.capacity() == 1


def test_push_increases_size():
    arr: DynamicArray[int] = DynamicArray()
    arr.push(10)
    arr.push(20)
    assert arr.size() == 2
    assert len(arr) == 2
    assert arr.get(0) == 10
    assert arr.get(1) == 20


def test_capacity_doubles_1_2_4_8():
    arr: DynamicArray[int] = DynamicArray()
    seen_capacities = []
    for i in range(8):
        arr.push(i)
        seen_capacities.append(arr.capacity())
    # capacity only ever grows by doubling, starting at 1
    assert seen_capacities[0] == 1  # 1 element fits in capacity 1
    assert seen_capacities[1] == 2  # 2nd element forces a grow to 2
    assert seen_capacities[2] == 4  # 3rd element forces a grow to 4
    assert seen_capacities[3] == 4  # 4th element still fits in capacity 4
    assert seen_capacities[7] == 8  # 5th..8th fit in capacity 8
    # distinct capacities visited, in order, are exactly the doubling series
    distinct = sorted(set(seen_capacities))
    assert distinct == [1, 2, 4, 8]


def test_get_out_of_bounds_raises():
    arr: DynamicArray[int] = DynamicArray()
    arr.push(1)
    with pytest.raises(IndexError):
        arr.get(1)
    with pytest.raises(IndexError):
        arr.get(-1)


def test_get_on_empty_array_raises():
    arr: DynamicArray[int] = DynamicArray()
    with pytest.raises(IndexError):
        arr.get(0)


def test_set_overwrites_without_changing_size():
    arr: DynamicArray[int] = DynamicArray()
    arr.push(1)
    arr.push(2)
    arr.set(0, 99)
    assert arr.get(0) == 99
    assert arr.size() == 2


def test_set_out_of_bounds_raises():
    arr: DynamicArray[int] = DynamicArray()
    arr.push(1)
    with pytest.raises(IndexError):
        arr.set(5, 0)


def test_pop_returns_last_and_shrinks_size():
    arr: DynamicArray[int] = DynamicArray()
    arr.push(1)
    arr.push(2)
    arr.push(3)
    assert arr.pop() == 3
    assert arr.size() == 2
    assert arr.get(1) == 2


def test_pop_empty_raises():
    arr: DynamicArray[int] = DynamicArray()
    with pytest.raises(IndexError):
        arr.pop()


def test_push_pop_interleaved_preserves_order():
    arr: DynamicArray[int] = DynamicArray()
    for i in range(5):
        arr.push(i)
    assert arr.pop() == 4
    arr.push(40)
    assert [arr.get(i) for i in range(arr.size())] == [0, 1, 2, 3, 40]


def test_amortized_push_of_100_000_elements_is_fast():
    # If push copied the whole buffer on every call (instead of only on a
    # doubling resize), 100_000 pushes would do ~5 billion element copies.
    # Amortized O(1) push finishes this near-instantly.
    arr: DynamicArray[int] = DynamicArray()
    n = 100_000
    start = time.perf_counter()
    for i in range(n):
        arr.push(i)
    elapsed = time.perf_counter() - start

    assert arr.size() == n
    assert arr.get(0) == 0
    assert arr.get(n - 1) == n - 1
    # generous sanity bound, not a tight benchmark
    assert elapsed < 5.0
