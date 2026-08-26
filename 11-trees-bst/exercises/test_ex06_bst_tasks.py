import pytest
from ex01_build_bst import tree_from_level_array
from ex06_bst_tasks import kth_smallest, lca_bst, range_sum_bst


def test_kth_smallest_typical():
    root = tree_from_level_array([5, 3, 8, 1, 4])
    assert kth_smallest(root, 2) == 3


def test_kth_smallest_first():
    root = tree_from_level_array([5, 3, 8, 1, 4])
    assert kth_smallest(root, 1) == 1


def test_kth_smallest_last():
    root = tree_from_level_array([5, 3, 8, 1, 4])
    assert kth_smallest(root, 5) == 8


def test_kth_smallest_out_of_range_raises():
    root = tree_from_level_array([5, 3, 8])
    with pytest.raises(ValueError):
        kth_smallest(root, 10)


def test_lca_bst_split_at_internal_node():
    root = tree_from_level_array([6, 2, 8, 0, 4, 7, 9])
    assert lca_bst(root, 0, 4) == 2


def test_lca_bst_ancestor_is_one_of_the_targets():
    root = tree_from_level_array([6, 2, 8, 0, 4, 7, 9])
    assert lca_bst(root, 2, 4) == 2


def test_lca_bst_split_at_root():
    root = tree_from_level_array([6, 2, 8, 0, 4, 7, 9])
    assert lca_bst(root, 0, 9) == 6


def test_range_sum_bst_typical():
    root = tree_from_level_array([10, 5, 15, 3, 7, None, 18])
    assert range_sum_bst(root, 6, 15) == 32


def test_range_sum_bst_full_range():
    root = tree_from_level_array([10, 5, 15, 3, 7, None, 18])
    assert range_sum_bst(root, 0, 100) == 10 + 5 + 15 + 3 + 7 + 18


def test_range_sum_bst_no_matches():
    root = tree_from_level_array([10, 5, 15, 3, 7, None, 18])
    assert range_sum_bst(root, 100, 200) == 0


def test_range_sum_bst_empty_tree():
    assert range_sum_bst(None, 0, 10) == 0


def test_range_sum_bst_single_boundary_value():
    root = tree_from_level_array([10, 5, 15, 3, 7, None, 18])
    assert range_sum_bst(root, 15, 15) == 15
