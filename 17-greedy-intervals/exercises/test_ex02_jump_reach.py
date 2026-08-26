from ex02_jump_reach import can_reach_end, min_jumps


def test_can_reach_end_typical_reachable():
    assert can_reach_end([2, 3, 1, 1, 4]) is True


def test_can_reach_end_typical_stuck():
    assert can_reach_end([3, 2, 1, 0, 4]) is False


def test_can_reach_end_single_element_already_there():
    assert can_reach_end([0]) is True


def test_can_reach_end_all_zeros_except_first_fails_past_start():
    assert can_reach_end([1, 0, 0, 0]) is False


def test_can_reach_end_large_first_jump_covers_everything():
    assert can_reach_end([10, 0, 0, 0, 0]) is True


def test_can_reach_end_efficiency_large_input():
    n = 200_000
    nums = [1] * n  # only just barely reachable, one step at a time
    assert can_reach_end(nums) is True


def test_min_jumps_typical():
    assert min_jumps([2, 3, 1, 1, 4]) == 2


def test_min_jumps_every_step_forced():
    assert min_jumps([1, 1, 1, 1]) == 3


def test_min_jumps_already_at_end():
    assert min_jumps([5]) == 0


def test_min_jumps_one_big_jump_suffices():
    assert min_jumps([5, 1, 1, 1, 1]) == 1


def test_min_jumps_unreachable_returns_negative_one():
    assert min_jumps([3, 2, 1, 0, 4]) == -1


def test_min_jumps_trivially_reachable_single_hop():
    assert min_jumps([10, 1, 1, 1, 1]) == 1


def test_min_jumps_efficiency_large_input():
    n = 200_000
    nums = [1] * n
    assert min_jumps(nums) == n - 1
