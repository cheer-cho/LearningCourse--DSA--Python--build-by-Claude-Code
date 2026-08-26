# Scenario: a delivery depot must load `weights` onto a truck IN ORDER
# (no reordering) across `d` days, one or more consecutive packages per
# day, without exceeding the truck's capacity on any day. A warehouse
# team has the same shape of problem: split a list into `k` contiguous
# chunks minimizing the biggest chunk. Pattern: search on the answer
# again — this time the answer is a CAPACITY, not a rate.
# Run: uv run pytest 10-binary-search -k ex05


def min_capacity(weights: list[int], d: int) -> int:
    """Return the minimum truck capacity that lets you ship every package
    in `weights`, IN THE GIVEN ORDER, within `d` days — each day you load
    one or more consecutive packages whose total weight is <= capacity.

    The predicate `can(cap)` = "can finish within d days at this
    capacity" is monotone: a bigger capacity never needs more days.
    Binary-search the smallest feasible capacity in
    `[max(weights), sum(weights)]` (you can never ship less than the
    heaviest single package; shipping everything in one day always
    works).

    min_capacity([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5) -> 15
    min_capacity([3, 2, 2, 4, 1, 4], 3) -> 6
    min_capacity([1, 2, 3, 1, 1], 4) -> 3

    Target: O(n log(sum(weights))) time, O(1) space.
    """
    raise NotImplementedError


def split_min_largest(nums: list[int], k: int) -> int:
    """Split `nums` into exactly `k` non-empty CONTIGUOUS parts (order
    preserved) to minimize the largest part's sum. Return that minimized
    largest sum.

    Same predicate as `min_capacity` — "can I split this into <= k parts
    each with sum <= X?" — just asked about a general list instead of a
    day-by-day shipping schedule. `1 <= k <= len(nums)`.

    split_min_largest([7, 2, 5, 10, 8], 2) -> 18
    split_min_largest([1, 2, 3, 4, 5], 1) -> 15
    split_min_largest([1, 4, 4], 3) -> 4

    Target: O(n log(sum(nums))) time, O(1) space.
    """
    raise NotImplementedError
