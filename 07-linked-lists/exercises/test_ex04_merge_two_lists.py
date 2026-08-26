from ex01_build_singly_list import from_array, to_array
from ex04_merge_two_lists import merge_sorted, remove_nth_from_end


def test_merge_sorted_interleaved():
    merged = merge_sorted(from_array([1, 3, 5]), from_array([2, 4, 6]))
    assert to_array(merged) == [1, 2, 3, 4, 5, 6]


def test_merge_sorted_one_empty():
    merged = merge_sorted(None, from_array([1, 2, 3]))
    assert to_array(merged) == [1, 2, 3]
    merged = merge_sorted(from_array([1, 2, 3]), None)
    assert to_array(merged) == [1, 2, 3]


def test_merge_sorted_both_empty():
    assert merge_sorted(None, None) is None


def test_merge_sorted_handles_duplicates():
    merged = merge_sorted(from_array([1, 1, 3]), from_array([1, 2]))
    assert to_array(merged) == [1, 1, 1, 2, 3]


def test_merge_sorted_different_lengths():
    merged = merge_sorted(from_array([1]), from_array([2, 3, 4, 5]))
    assert to_array(merged) == [1, 2, 3, 4, 5]


def test_merge_sorted_reuses_existing_nodes():
    a = from_array([1, 5])
    b = from_array([2, 3, 4])
    original_ids = set()
    cur = a
    while cur is not None:
        original_ids.add(id(cur))
        cur = cur.next
    cur = b
    while cur is not None:
        original_ids.add(id(cur))
        cur = cur.next

    merged = merge_sorted(a, b)
    cur = merged
    seen = 0
    while cur is not None:
        assert id(cur) in original_ids
        seen += 1
        cur = cur.next
    assert seen == len(original_ids)


def test_remove_nth_from_end_removes_tail():
    head = remove_nth_from_end(from_array([1, 2, 3, 4, 5]), 1)
    assert to_array(head) == [1, 2, 3, 4]


def test_remove_nth_from_end_removes_head():
    head = remove_nth_from_end(from_array([1, 2, 3, 4, 5]), 5)
    assert to_array(head) == [2, 3, 4, 5]


def test_remove_nth_from_end_removes_middle():
    head = remove_nth_from_end(from_array([1, 2, 3, 4, 5]), 2)
    assert to_array(head) == [1, 2, 3, 5]


def test_remove_nth_from_end_single_element_list():
    head = remove_nth_from_end(from_array([1]), 1)
    assert head is None
