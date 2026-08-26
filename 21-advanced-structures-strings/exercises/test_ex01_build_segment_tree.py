from ex01_build_segment_tree import SegmentTree


def test_build_and_full_range_sum():
    st = SegmentTree([2, 5, 1, 4, 9, 3])
    assert st.range_sum(0, 5) == 24


def test_range_sum_sub_range():
    st = SegmentTree([2, 5, 1, 4, 9, 3])
    assert st.range_sum(1, 4) == 19
    assert st.range_sum(0, 2) == 8


def test_range_sum_single_element():
    st = SegmentTree([2, 5, 1, 4, 9, 3])
    assert st.range_sum(3, 3) == 4


def test_update_changes_future_queries():
    st = SegmentTree([2, 5, 1, 4])
    st.update(2, 10)
    assert st.range_sum(0, 3) == 21
    assert st.range_sum(2, 2) == 10


def test_update_does_not_affect_untouched_ranges():
    st = SegmentTree([1, 1, 1, 1, 1])
    st.update(0, 100)
    assert st.range_sum(1, 4) == 4


def test_single_element_tree():
    st = SegmentTree([7])
    assert st.range_sum(0, 0) == 7
    st.update(0, 3)
    assert st.range_sum(0, 0) == 3


def test_negative_values():
    st = SegmentTree([-5, 3, -2, 8])
    assert st.range_sum(0, 3) == 4
    st.update(1, -3)
    assert st.range_sum(0, 3) == -2


def test_empty_array_builds_without_error():
    st = SegmentTree([])
    assert isinstance(st, SegmentTree)


def test_multiple_updates_same_index():
    st = SegmentTree([0, 0, 0])
    st.update(1, 5)
    st.update(1, 9)
    st.update(1, 2)
    assert st.range_sum(0, 2) == 2


def test_segment_tree_efficiency_large_input():
    # n = 100,000, ~50,000 mixed update/query ops. A naive "rebuild a
    # prefix array on every update" approach is O(n) per update here
    # -- 50,000 * 100,000 operations, effectively infeasible. A real
    # O(log n) segment tree finishes this instantly.
    n = 100_000
    st = SegmentTree([1] * n)

    for i in range(0, n, 2):
        st.update(i, 2)
        if i % 20_000 == 0:
            # sprinkle in range queries so this is genuinely "mixed"
            assert st.range_sum(0, i) >= 0

    # every even index is now 2, every odd index is still 1
    assert st.range_sum(0, n - 1) == 150_000
    assert st.range_sum(0, 99) == 150
    assert st.range_sum(1, 1) == 1
