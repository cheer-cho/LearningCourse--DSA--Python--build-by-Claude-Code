from ex01_build_singly_list import from_array, to_array
from ex02_reverse_list import reverse_list, reverse_list_recursive


def test_reverse_list_typical():
    head = from_array([1, 2, 3, 4, 5])
    new_head = reverse_list(head)
    assert to_array(new_head) == [5, 4, 3, 2, 1]


def test_reverse_list_empty():
    assert reverse_list(None) is None


def test_reverse_list_single_element():
    head = from_array([9])
    new_head = reverse_list(head)
    assert to_array(new_head) == [9]


def test_reverse_list_two_elements():
    head = from_array([1, 2])
    new_head = reverse_list(head)
    assert to_array(new_head) == [2, 1]


def test_reverse_list_reuses_original_nodes_no_new_allocations():
    head = from_array([1, 2, 3])
    original_tail = head.next.next  # node holding 3
    new_head = reverse_list(head)
    assert new_head is original_tail  # old tail is the new head, same object


def test_reverse_list_recursive_typical():
    head = from_array([1, 2, 3, 4, 5])
    new_head = reverse_list_recursive(head)
    assert to_array(new_head) == [5, 4, 3, 2, 1]


def test_reverse_list_recursive_empty():
    assert reverse_list_recursive(None) is None


def test_reverse_list_recursive_single_element():
    head = from_array([9])
    new_head = reverse_list_recursive(head)
    assert to_array(new_head) == [9]


def test_reverse_list_recursive_matches_iterative():
    values = [3, 1, 4, 1, 5, 9, 2, 6]
    iterative = to_array(reverse_list(from_array(values)))
    recursive = to_array(reverse_list_recursive(from_array(values)))
    assert iterative == recursive == list(reversed(values))
