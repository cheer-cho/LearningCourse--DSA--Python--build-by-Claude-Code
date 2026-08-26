from ex01_build_singly_list import from_array, to_array
from ex05_reorder_list import reorder


def test_reorder_even_length():
    head = from_array([1, 2, 3, 4])
    reorder(head)
    assert to_array(head) == [1, 4, 2, 3]


def test_reorder_odd_length():
    head = from_array([1, 2, 3, 4, 5])
    reorder(head)
    assert to_array(head) == [1, 5, 2, 4, 3]


def test_reorder_two_elements():
    head = from_array([1, 2])
    reorder(head)
    assert to_array(head) == [1, 2]


def test_reorder_single_element_unchanged():
    head = from_array([1])
    reorder(head)
    assert to_array(head) == [1]


def test_reorder_empty_list_does_not_raise():
    reorder(None)  # just must not raise


def test_reorder_longer_even_length():
    head = from_array([1, 2, 3, 4, 5, 6])
    reorder(head)
    assert to_array(head) == [1, 6, 2, 5, 3, 4]
