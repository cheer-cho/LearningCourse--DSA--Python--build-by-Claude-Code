# Checkpoint 18 -- Freelancer calendar
#
# You're managing a freelancer's schedule across a line of days. Four
# independent questions about that calendar, each a straight instance
# of a pattern this module already built -- name the pattern, don't
# reinvent the recurrence.
# Run: uv run pytest 18-dp-1d -k checkpoint

from __future__ import annotations


def max_earnings(day_pay: list[int]) -> int:
    """`day_pay[i]` is the pay for taking a gig on day i. Gigs on
    back-to-back days conflict (the client needs a day of prep in
    between), so you can never take two ADJACENT days. Return the
    maximum total pay achievable.

    Same shape as house robber (ex03's `max_loot`): binary take/skip
    choice, dp[i] = max(dp[i-1], day_pay[i] + dp[i-2]).

    max_earnings([]) -> 0
    max_earnings([50]) -> 50
    max_earnings([30, 200, 40, 90]) -> 290   (days 1 and 3: 200 + 90)

    Target: O(n) time, O(1) space.
    """
    raise NotImplementedError


def min_gear_cost(day_costs: list[int]) -> int:
    """`day_costs[i]` is the cost to rent gear needed to work day i.
    You may start your first work day on day 0 or day 1 for free
    (no gear cost to simply BEGIN there), and from any work day you
    advance 1 or 2 days to your next one. Return the minimum total
    gear cost to get all the way past the last day (day
    len(day_costs), i.e. the calendar is finished).

    Same shape as ex02's `min_cost_climb`: dp[i] = min(dp[i-1] +
    day_costs[i-1], dp[i-2] + day_costs[i-2]), dp[0] = dp[1] = 0.

    min_gear_cost([10, 15, 20]) -> 15
    min_gear_cost([0, 0]) -> 0
    min_gear_cost([]) -> 0

    Target: O(n) time, O(1) space.
    """
    raise NotImplementedError


def ways_to_fill(n_days: int, block_sizes: list[int]) -> int:
    """Count the number of distinct ways to fully book a calendar of
    exactly `n_days` using gigs whose lengths come from `block_sizes`
    (any block size reusable any number of times). ORDER MATTERS: a
    3-day gig followed by a 2-day gig is a DIFFERENT booking from a
    2-day gig followed by a 3-day gig, even though both fill 5 days
    (this is what distinguishes it from a coin-change-COMBINATIONS
    count, where order would be ignored).

    STATE: dp[d] = number of distinct orderings of blocks that sum to
    exactly d days.
    CHOICE: which block size is placed LAST.
    RECURRENCE: dp[d] = sum(dp[d - b] for b in block_sizes if b <= d)
    -- structurally identical to ex01's climb_ways generalized from
    fixed steps {1, 2} to an arbitrary set of step sizes.
    BASE CASE: dp[0] = 1 (one way to book zero days: book nothing).

    ways_to_fill(0, [1, 2]) -> 1
    ways_to_fill(3, [1, 2]) -> 3     (1+1+1, 1+2, 2+1)
    ways_to_fill(4, [1, 2, 3]) -> 7
    ways_to_fill(5, [5]) -> 1

    Target: O(n_days * len(block_sizes)) time, O(n_days) space.
    """
    raise NotImplementedError


def longest_growth_streak(revenues: list[int]) -> int:
    """Return the length of the longest GROWTH STREAK in `revenues`:
    the longest strictly increasing subsequence (months don't need to
    be consecutive, but their original order is preserved and each
    picked value must exceed the one before it).

    Same shape as ex07's `lis_length` / `lis_length_fast`.

    longest_growth_streak([]) -> 0
    longest_growth_streak([3, 1, 4, 1, 5, 9, 2, 6]) -> 4  (1, 4, 5, 9 or 1, 4, 5, 6)
    longest_growth_streak([9, 8, 7]) -> 1

    Target: O(n log n) time, O(n) space.
    """
    raise NotImplementedError
