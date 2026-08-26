import pytest
from ex06_build_doubly_list import DoublyLinkedList


def test_push_back_appends_in_order():
    dll = DoublyLinkedList()
    dll.push_back(1)
    dll.push_back(2)
    dll.push_back(3)
    assert dll.to_array() == [1, 2, 3]
    assert dll.size() == 3


def test_push_front_prepends_in_order():
    dll = DoublyLinkedList()
    dll.push_front(3)
    dll.push_front(2)
    dll.push_front(1)
    assert dll.to_array() == [1, 2, 3]


def test_push_front_and_back_mixed():
    dll = DoublyLinkedList()
    dll.push_back(2)
    dll.push_front(1)
    dll.push_back(3)
    assert dll.to_array() == [1, 2, 3]


def test_push_returns_the_new_node():
    dll = DoublyLinkedList()
    node = dll.push_back(42)
    assert node.value == 42


def test_pop_front_empty_raises():
    dll = DoublyLinkedList()
    with pytest.raises(IndexError):
        dll.pop_front()


def test_pop_back_empty_raises():
    dll = DoublyLinkedList()
    with pytest.raises(IndexError):
        dll.pop_back()


def test_pop_front_returns_and_removes():
    dll = DoublyLinkedList()
    dll.push_back(1)
    dll.push_back(2)
    assert dll.pop_front() == 1
    assert dll.to_array() == [2]
    assert dll.size() == 1


def test_pop_back_returns_and_removes():
    dll = DoublyLinkedList()
    dll.push_back(1)
    dll.push_back(2)
    assert dll.pop_back() == 2
    assert dll.to_array() == [1]


def test_pop_last_element_empties_list_cleanly():
    dll = DoublyLinkedList()
    dll.push_back(1)
    dll.pop_front()
    assert dll.size() == 0
    assert dll.to_array() == []
    # must still work correctly after being emptied
    dll.push_back(5)
    assert dll.to_array() == [5]


def test_remove_node_middle():
    dll = DoublyLinkedList()
    dll.push_back(1)
    node2 = dll.push_back(2)
    dll.push_back(3)
    dll.remove_node(node2)
    assert dll.to_array() == [1, 3]
    assert dll.size() == 2


def test_remove_node_front():
    dll = DoublyLinkedList()
    node1 = dll.push_back(1)
    dll.push_back(2)
    dll.remove_node(node1)
    assert dll.to_array() == [2]


def test_remove_node_back():
    dll = DoublyLinkedList()
    dll.push_back(1)
    node2 = dll.push_back(2)
    dll.remove_node(node2)
    assert dll.to_array() == [1]


def test_remove_node_only_element():
    dll = DoublyLinkedList()
    node = dll.push_back(1)
    dll.remove_node(node)
    assert dll.to_array() == []
    assert dll.size() == 0
    with pytest.raises(IndexError):
        dll.pop_front()


def test_size_tracks_all_operations():
    dll = DoublyLinkedList()
    assert dll.size() == 0
    dll.push_back(1)
    dll.push_front(0)
    node = dll.push_back(2)
    assert dll.size() == 3
    dll.pop_front()
    assert dll.size() == 2
    dll.remove_node(node)
    assert dll.size() == 1
