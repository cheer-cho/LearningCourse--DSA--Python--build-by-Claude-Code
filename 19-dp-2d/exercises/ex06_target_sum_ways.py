# Scenario: attach a '+' or '-' sign to every number in a list so the
# signed sum lands exactly on a target; count how many sign assignments
# achieve it.
# Pattern: subset-sum reduction -- turn a signed-assignment count into a
# 0/1 knapsack feasibility count.
# Run: uv run pytest 19-dp-2d -k ex06

from __future__ import annotations


def ways_to_target(nums: list[int], target: int) -> int:
    """Count the number of ways to assign '+' or '-' to every number in
    `nums` so the resulting signed sum equals `target`.

    THE REDUCTION (derive it, don't skip it):
    let P = the subset assigned '+', N = the subset assigned '-'.
      P + N = sum(nums)      (every number is in exactly one subset)
      P - N = target         (the signed sum we want)
    Adding the two equations: 2P = sum(nums) + target, so
      P = (sum(nums) + target) / 2.
    The problem becomes "how many subsets of nums sum to exactly P?" --
    a 0/1 subset-sum COUNT (each number used at most once).

    Preconditions (check first -- both make the reduction impossible):
    if (sum(nums) + target) is odd, P isn't an integer -- return 0.
    if abs(target) > sum(nums), no assignment can reach it -- return 0.

    STATE: dp[w] = number of subsets (of numbers seen so far) that sum
    to exactly w. BASE CASE: dp[0] = 1 (one way to make 0: pick none).
    Sweep w HIGH to LOW per number (the 0/1 direction rule) so each
    number is used at most once.

    Zeros: a zero can be '+' or '-' with no effect on the sum, so each
    zero DOUBLES the number of ways (it's still a real sign choice).

    ways_to_target([1, 1, 1, 1, 1], 3) -> 5
    ways_to_target([1, 0], 1) -> 2      (+1+0 and +1-0)
    ways_to_target([0, 0, 0], 0) -> 8   (2**3 sign choices, all valid)
    ways_to_target([1], 2) -> 0         (unreachable: max signed sum is 1)

    Target: O(n * P) time, O(P) space, where P = (sum(nums) + target) // 2.
    """
    raise NotImplementedError
