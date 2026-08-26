import time

import pytest
from ex01_build_singly_list import ListNode, SinglyLinkedList, from_array, to_array


def test_from_array_builds_chain_in_order():
    head = from_array([1, 2, 3])
    assert isinstance(head, ListNode)
    assert head.value == 1
    assert head.next.value == 2
    assert head.next.next.value == 3
    assert head.next.next.next is None


def test_from_array_empty_is_none():
    assert from_array([]) is None


def test_to_array_round_trips_from_array():
    assert to_array(from_array([5, 4, 3, 2, 1])) == [5, 4, 3, 2, 1]


def test_to_array_of_none_is_empty():
    assert to_array(None) == []


def test_to_array_single_element():
    assert to_array(from_array([42])) == [42]


def test_push_front_prepends():
    lst = SinglyLinkedList()
    lst.push_front(2)
    lst.push_front(1)
    assert lst.to_array() == [1, 2]


def test_push_back_appends():
    lst = SinglyLinkedList()
    lst.push_back(1)
    lst.push_back(2)
    lst.push_back(3)
    assert lst.to_array() == [1, 2, 3]


def test_push_back_after_push_front_keeps_order():
    lst = SinglyLinkedList()
    lst.push_front(2)
    lst.push_front(1)
    lst.push_back(3)
    assert lst.to_array() == [1, 2, 3]


def test_push_back_updates_tail_so_next_push_back_is_correct():
    lst = SinglyLinkedList()
    lst.push_back(1)
    lst.push_back(2)
    assert lst.tail.value == 2
    lst.push_back(3)
    assert lst.tail.value == 3
    assert lst.to_array() == [1, 2, 3]


def test_pop_front_empty_raises_index_error():
    lst = SinglyLinkedList()
    with pytest.raises(IndexError):
        lst.pop_front()


def test_pop_front_removes_and_returns_first_value():
    lst = SinglyLinkedList()
    lst.push_back(1)
    lst.push_back(2)
    assert lst.pop_front() == 1
    assert lst.to_array() == [2]


def test_pop_front_to_empty_resets_tail():
    lst = SinglyLinkedList()
    lst.push_back(1)
    lst.pop_front()
    assert lst.head is None
    assert lst.tail is None
    assert lst.size() == 0
    # pushing again after emptying must still work correctly
    lst.push_back(9)
    assert lst.to_array() == [9]
    assert lst.tail.value == 9


def test_find_returns_node_holding_value():
    lst = SinglyLinkedList()
    lst.push_back(1)
    lst.push_back(2)
    lst.push_back(3)
    node = lst.find(2)
    assert node is not None
    assert node.value == 2


def test_find_missing_value_returns_none():
    lst = SinglyLinkedList()
    lst.push_back(1)
    assert lst.find(99) is None


def test_delete_value_missing_returns_false():
    lst = SinglyLinkedList()
    lst.push_back(1)
    assert lst.delete_value(99) is False
    assert lst.to_array() == [1]


def test_delete_value_head():
    lst = SinglyLinkedList()
    for v in (1, 2, 3):
        lst.push_back(v)
    assert lst.delete_value(1) is True
    assert lst.to_array() == [2, 3]


def test_delete_value_middle():
    lst = SinglyLinkedList()
    for v in (1, 2, 3):
        lst.push_back(v)
    assert lst.delete_value(2) is True
    assert lst.to_array() == [1, 3]


def test_delete_value_tail_fixes_tail_pointer():
    lst = SinglyLinkedList()
    for v in (1, 2, 3):
        lst.push_back(v)
    assert lst.delete_value(3) is True
    assert lst.to_array() == [1, 2]
    assert lst.tail.value == 2
    lst.push_back(4)
    assert lst.to_array() == [1, 2, 4]


def test_delete_value_only_element_empties_list():
    lst = SinglyLinkedList()
    lst.push_back(1)
    assert lst.delete_value(1) is True
    assert lst.head is None
    assert lst.tail is None
    assert lst.size() == 0


def test_size_tracks_pushes_and_pops():
    lst = SinglyLinkedList()
    assert lst.size() == 0
    lst.push_back(1)
    lst.push_front(0)
    assert lst.size() == 2
    lst.pop_front()
    assert lst.size() == 1
    lst.delete_value(1)
    assert lst.size() == 0


def test_push_back_100_000_times_is_fast_and_correct():
    # Efficiency test: with a tail pointer, 100_000 push_backs is O(n)
    # total. Without one (walking to the end each time), this would be
    # O(n^2) and dramatically slower.
    lst = SinglyLinkedList()
    start = time.perf_counter()
    for i in range(100_000):
        lst.push_back(i)
    elapsed = time.perf_counter() - start

    assert lst.size() == 100_000
    assert lst.head.value == 0
    assert lst.tail.value == 99_999
    assert elapsed < 5.0  # generous: O(1) push_back finishes in well under a second
