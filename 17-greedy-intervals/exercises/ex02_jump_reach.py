# Scenario: a platformer character stands on stepping stones; each
# stone's number is the furthest it can leap forward. Pattern: greedy
# furthest-reach sweep.
# Run: uv run pytest 17-greedy-intervals -k ex02


def can_reach_end(nums: list[int]) -> bool:
    """`nums[i]` is the furthest number of steps forward you may jump
    from index `i`. Starting at index 0, return whether you can reach
    the last index (you may land anywhere within a jump's reach, not
    only exactly `nums[i]` steps).

    Sweep left to right, tracking `furthest` = the furthest index
    reached so far. If you ever arrive at an index beyond `furthest`
    before updating it, you're stuck there — nothing before it could
    reach this far. You never need to try individual jump lengths.

    can_reach_end([2, 3, 1, 1, 4]) -> True
    can_reach_end([3, 2, 1, 0, 4]) -> False   (stuck at index 3)
    can_reach_end([0]) -> True                (already at the last index)

    Target: O(n) time, O(1) space.
    """
    raise NotImplementedError


def min_jumps(nums: list[int]) -> int:
    """Same setup as `can_reach_end` — return the MINIMUM number of
    jumps needed to reach the last index from index 0, or -1 if the
    last index is unreachable.

    Current-window / next-window sweep: track the furthest reach of
    the CURRENT jump (`window_end`) and the furthest reach achievable
    with ONE MORE jump (`next_furthest`), updated while scanning
    through the current window. When the scan reaches `window_end`,
    a jump is spent and the window advances to `next_furthest`. If a
    spent jump gains no ground (`next_furthest` hasn't moved past
    `window_end`), the sweep is stuck — return -1. This is O(n) —
    contrast with the DP formulation (module 18), which tries every
    previous index that could reach `i` for each `i`, O(n^2).

    min_jumps([2, 3, 1, 1, 4]) -> 2   (index0->1, index1->4)
    min_jumps([1, 1, 1, 1]) -> 3
    min_jumps([5]) -> 0               (already there, zero jumps needed)
    min_jumps([3, 2, 1, 0, 4]) -> -1  (stuck at index 3, can never reach index 4)

    Target: O(n) time, O(1) space.
    """
    raise NotImplementedError
