from collections.abc import Callable


def sum_all(nums: list[int], tick: Callable[[], None]) -> int:
    # Pattern: single linear pass, one tick per element.
    # O(n) time, O(1) extra space.
    total = 0
    for x in nums:
        tick()
        total += x
    return total


def all_pairs(items: list[int], tick: Callable[[], None]) -> list[tuple[int, int]]:
    # Pattern: nested loop, every (a, b) combination, one tick per pair.
    # O(n^2) time and space -- the inner loop restarts fully for each
    # outer step, so total work multiplies rather than adds.
    pairs = []
    for a in items:
        for b in items:
            tick()
            pairs.append((a, b))
    return pairs


def halve_down(n: int, tick: Callable[[], None]) -> int:
    # Pattern: halving loop, one tick per remaining "level."
    # O(log n) time, O(1) extra space -- n shrinks by a factor of 2
    # each step, so the number of steps is floor(log2(n)) + 1.
    steps = 0
    while n >= 1:
        tick()
        n //= 2
        steps += 1
    return steps
