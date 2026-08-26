def can_reach_end(nums: list[int]) -> bool:
    # Pattern: greedy furthest-reach sweep. Track the furthest index
    # reachable so far; if the sweep ever arrives at an index beyond
    # that, nothing before it could reach this far — stuck.
    # Complexity: O(n) time, O(1) space.
    furthest = 0
    last = len(nums) - 1
    for i, step in enumerate(nums):
        if i > furthest:
            return False
        furthest = max(furthest, i + step)
        if furthest >= last:
            return True
    return furthest >= last


def min_jumps(nums: list[int]) -> int:
    # Pattern: current-window / next-window greedy sweep. `window_end`
    # is the furthest reach of the jumps already spent; `next_furthest`
    # is the furthest reach achievable with one more jump. Spend a
    # jump exactly when the scan exhausts the current window; if that
    # spend gains no ground, the sweep is stuck — unreachable.
    # Complexity: O(n) time, O(1) space (vs. the O(n^2) DP that tries
    # every previous index for each position).
    if len(nums) <= 1:
        return 0

    jumps = 0
    window_end = 0
    next_furthest = 0
    last = len(nums) - 1

    for i in range(last):
        next_furthest = max(next_furthest, i + nums[i])
        if i == window_end:
            if next_furthest == window_end:
                return -1
            jumps += 1
            window_end = next_furthest
            if window_end >= last:
                return jumps

    return jumps if window_end >= last else -1
