from ex01_build_singly_list import ListNode, from_array
from ex03_fast_slow import cycle_start, has_cycle, middle_node


def make_cyclic(values: list[int], pos: int) -> "ListNode | None":
    """Build a chain from `values`, then link the last node's `.next`
    to the node at index `pos` (0-indexed) to create a cycle. Pass
    pos=-1 for no cycle at all.
    """
    head = from_array(values)
    if head is None or pos < 0:
        return head

    nodes = []
    cur = head
    while cur is not None:
        nodes.append(cur)
        cur = cur.next
    nodes[-1].next = nodes[pos]
    return head


def test_middle_node_odd_length():
    head = from_array([1, 2, 3])
    assert middle_node(head).value == 2


def test_middle_node_even_length_returns_second_middle():
    head = from_array([1, 2, 3, 4])
    assert middle_node(head).value == 3


def test_middle_node_single_element():
    head = from_array([7])
    assert middle_node(head).value == 7


def test_middle_node_empty():
    assert middle_node(None) is None


def test_has_cycle_false_for_acyclic_list():
    head = make_cyclic([1, 2, 3, 4], -1)
    assert has_cycle(head) is False


def test_has_cycle_true_when_tail_points_back_to_head():
    head = make_cyclic([1, 2, 3, 4], 0)
    assert has_cycle(head) is True


def test_has_cycle_true_for_cycle_in_the_middle():
    head = make_cyclic([1, 2, 3, 4, 5], 2)
    assert has_cycle(head) is True


def test_has_cycle_false_for_empty_list():
    assert has_cycle(None) is False


def test_has_cycle_false_for_single_node_no_cycle():
    head = from_array([1])
    assert has_cycle(head) is False


def test_has_cycle_true_for_single_node_self_loop():
    head = make_cyclic([1], 0)
    assert has_cycle(head) is True


def test_cycle_start_returns_none_when_no_cycle():
    head = make_cyclic([1, 2, 3], -1)
    assert cycle_start(head) is None


def test_cycle_start_finds_the_correct_node():
    head = make_cyclic([1, 2, 3, 4, 5], 2)
    # walk to the node at index 2 independently to know the expected node
    expected = head
    for _ in range(2):
        expected = expected.next
    assert cycle_start(head) is expected


def test_cycle_start_when_whole_list_is_the_cycle():
    head = make_cyclic([1, 2, 3], 0)
    assert cycle_start(head) is head
