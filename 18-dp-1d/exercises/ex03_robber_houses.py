# Scenario: houses stand in a row, each holding some value. Adjacent
# houses share an alarm wire — robbing two neighbors in the same night
# trips it. Maximize total value taken without ever picking adjacent
# houses. A second variant arranges the houses in a circle.
# Pattern: "min/max cost" DP where the CHOICE is binary (take / skip)
# and taking constrains your very next choice.
# Run: uv run pytest 18-dp-1d -k ex03

from __future__ import annotations


def max_loot(values: list[int]) -> int:
    """Return the maximum sum achievable by picking values from
    `values` such that no two picked indices are adjacent.

    STATE: dp[i] = max loot achievable using houses 0..i (free to
    include or exclude house i).
    CHOICE: skip house i (best is dp[i-1]) or rob it (its value plus
    the best NOT counting house i-1, i.e. dp[i-2]).
    RECURRENCE: dp[i] = max(dp[i-1], values[i] + dp[i-2]).
    BASE CASE: dp[-1] = 0 (no houses), dp[0] = values[0].

    max_loot([]) -> 0
    max_loot([5]) -> 5
    max_loot([2, 7, 9, 3, 1]) -> 12   (houses 0, 2, 4: 2 + 9 + 1)
    max_loot([5, 5, 10, 100, 10, 5]) -> 110

    Target: O(n) time, O(1) space.
    """
    raise NotImplementedError


def max_loot_circle(values: list[int]) -> int:
    """Same rule as `max_loot`, but the houses form a CIRCLE: house 0
    and house len(values)-1 are also adjacent (can't rob both).

    Reduction: in any valid selection, house 0 and the last house
    can't BOTH be picked (they're neighbors). So the optimal answer
    either excludes the last house entirely, or excludes the first
    house entirely — it can never need both present. That means the
    circular answer is just the better of two LINEAR `max_loot` runs:
    `max(max_loot(values[:-1]), max_loot(values[1:]))`. Each excludes
    exactly one end, so neither run can ever pick both wrap-around
    neighbors.

    max_loot_circle([]) -> 0
    max_loot_circle([5]) -> 5          (a single house has no neighbor)
    max_loot_circle([2, 3, 2]) -> 3    (0 and 2 are neighbors; best is house 1)
    max_loot_circle([1, 2, 3, 1]) -> 4 (houses 0 and 2: 1 + 3)

    Target: O(n) time, O(1) space.
    """
    raise NotImplementedError
