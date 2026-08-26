from collections.abc import Callable


def first_bad_build(n: int, is_bad: Callable[[int], bool]) -> int:
    # Pattern: THE template. feasible(v) = is_bad(v) is monotone (False
    # ... False, True ... True) with build n guaranteed bad, so the
    # smallest feasible v is the answer.
    # Time: O(log n) calls to is_bad. Space: O(1).
    lo, hi = 1, n
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if is_bad(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo


def _rigs_needed(loads: list[int], hours: int, max_rigs: int) -> bool:
    """Greedy: can loads be split into <= max_rigs contiguous groups,
    each with total hours <= `hours`?"""
    rigs = 1
    current = 0
    for load in loads:
        if current + load > hours:
            rigs += 1
            current = load
        else:
            current += load
    return rigs <= max_rigs


def min_test_rigs(loads: list[int], hours: int) -> int:
    # Pattern: search on the answer. can(r) = "a contiguous split into
    # <= r groups each <= hours exists" is monotone in r (more groups
    # only make it easier), checked in O(n) with one greedy scan.
    # Time: O(n log n). Space: O(1).
    lo, hi = 1, len(loads)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if _rigs_needed(loads, hours, mid):
            hi = mid
        else:
            lo = mid + 1
    return lo


def find_version(tags: list[str], target: str) -> tuple[int, int]:
    # Pattern: boundary search (lower_bound / upper_bound) inlined
    # twice -- the first and last occurrence bracket the run of matches.
    # Time: O(log n). Space: O(1).
    n = len(tags)

    lo, hi = 0, n
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if tags[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    first = lo

    if first == n or tags[first] != target:
        return (-1, -1)

    lo, hi = first, n
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if tags[mid] <= target:
            lo = mid + 1
        else:
            hi = mid
    last = lo - 1

    return (first, last)
