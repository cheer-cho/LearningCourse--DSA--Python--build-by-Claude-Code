import time

import pytest
from checkpoint_02 import Shelf, compact, restock_merge, rotate_display


def test_shelf_starts_empty_with_capacity_one():
    shelf: Shelf[int] = Shelf()
    assert shelf.size() == 0
    assert shelf.capacity() == 1


def test_shelf_push_and_get():
    shelf: Shelf[str] = Shelf()
    shelf.push("wrench")
    shelf.push("hammer")
    assert shelf.size() == 2
    assert shelf.get(0) == "wrench"
    assert shelf.get(1) == "hammer"


def test_shelf_capacity_doubles():
    shelf: Shelf[int] = Shelf()
    capacities = []
    for i in range(5):
        shelf.push(i)
        capacities.append(shelf.capacity())
    assert sorted(set(capacities)) == [1, 2, 4, 8]


def test_shelf_pop_returns_last_pushed():
    shelf: Shelf[int] = Shelf()
    shelf.push(1)
    shelf.push(2)
    shelf.push(3)
    assert shelf.pop() == 3
    assert shelf.size() == 2


def test_shelf_pop_empty_raises():
    shelf: Shelf[int] = Shelf()
    with pytest.raises(IndexError):
        shelf.pop()


def test_shelf_get_out_of_bounds_raises():
    shelf: Shelf[int] = Shelf()
    shelf.push(1)
    with pytest.raises(IndexError):
        shelf.get(1)


def test_shelf_amortized_push_of_50_000_items_is_fast():
    shelf: Shelf[int] = Shelf()
    n = 50_000
    start = time.perf_counter()
    for i in range(n):
        shelf.push(i)
    elapsed = time.perf_counter() - start

    assert shelf.size() == n
    assert shelf.get(0) == 0
    assert shelf.get(n - 1) == n - 1
    assert elapsed < 5.0  # generous sanity bound, not a tight benchmark


def test_restock_merge_typical():
    assert restock_merge([1, 4, 6], [2, 3, 9]) == [1, 2, 3, 4, 6, 9]


def test_restock_merge_one_empty():
    assert restock_merge([], [5]) == [5]
    assert restock_merge([5], []) == [5]


def test_restock_merge_does_not_mutate_inputs():
    a, b = [1, 3], [2, 4]
    restock_merge(a, b)
    assert a == [1, 3]
    assert b == [2, 4]


def test_compact_typical():
    slots: list[int | None] = [7, None, 3, None, 9]
    new_len = compact(slots)
    assert new_len == 3
    assert slots[:new_len] == [7, 3, 9]


def test_compact_all_empty():
    slots: list[int | None] = [None, None]
    assert compact(slots) == 0


def test_compact_no_empties():
    slots: list[int | None] = [1, 2, 3]
    new_len = compact(slots)
    assert new_len == 3
    assert slots[:new_len] == [1, 2, 3]


def test_compact_empty_list():
    slots: list[int | None] = []
    assert compact(slots) == 0


def test_rotate_display_typical():
    items = ["a", "b", "c", "d"]
    rotate_display(items, 1)
    assert items == ["d", "a", "b", "c"]


def test_rotate_display_k_zero_is_a_no_op():
    items = ["a", "b", "c"]
    rotate_display(items, 0)
    assert items == ["a", "b", "c"]


def test_rotate_display_k_greater_than_length_wraps():
    items = ["a", "b", "c"]
    rotate_display(items, 4)  # 4 % 3 == 1
    assert items == ["c", "a", "b"]


def test_rotate_display_empty_list_does_not_crash():
    items: list[str] = []
    rotate_display(items, 3)
    assert items == []
