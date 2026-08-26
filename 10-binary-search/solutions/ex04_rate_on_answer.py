import math


def _hours_needed(piles: list[int], rate: int) -> int:
    return sum(math.ceil(pile / rate) for pile in piles)


def min_rate(piles: list[int], h: int) -> int:
    # Pattern: search on the answer. can(r) = "total hours at rate r is
    # <= h" is monotone -- raising r never raises the hours needed --
    # so binary-search the smallest feasible r in [1, max(piles)].
    # Time: O(n log(max(piles))). Space: O(1).
    lo, hi = 1, max(piles)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if _hours_needed(piles, mid) <= h:
            hi = mid
        else:
            lo = mid + 1
    return lo
