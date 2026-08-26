# Checkpoint 10 — Release bisector
#
# A release pipeline needs three binary-search tools: find exactly where
# a rollout turned bad, find the fewest test rigs that still hit a
# deadline, and find where a version tag lives among sorted, duplicated
# tags. Combines the classic template, search-on-answer, and boundary
# search -- everything from this module.
# Run: uv run pytest 10-binary-search -k checkpoint

from collections.abc import Callable


def first_bad_build(n: int, is_bad: Callable[[int], bool]) -> int:
    """Builds are numbered 1..n. Once a build is bad, every later build
    is also bad (monotone) -- and build `n` is guaranteed to be bad, so
    a first bad build always exists. `is_bad` is an expensive check
    (imagine it re-runs a full test suite); call it as few times as
    possible.

    Return the number of the first bad build.

    first_bad_build(5, lambda v: v >= 3) -> 3
    first_bad_build(1, lambda v: v >= 1) -> 1

    Target: O(log n) calls to is_bad, O(1) space.
    """
    raise NotImplementedError


def min_test_rigs(loads: list[int], hours: int) -> int:
    """`loads` lists, in a fixed order, how many hours each queued build
    needs on a test rig. Split `loads` into the fewest number of
    CONTIGUOUS groups (order preserved) so that no group's total hours
    exceeds `hours` -- that group count is the minimum number of test
    rigs needed to clear every build within the deadline, one rig per
    group. Every individual load is <= `hours`, so a valid split always
    exists.

    Binary-search the rig count `r` in `[1, len(loads)]`: `can(r)` =
    "does a contiguous split into <= r groups, each <= hours, exist?" is
    monotone (more groups only make it easier), and can be checked with
    one greedy left-to-right scan.

    min_test_rigs([1, 2, 3, 4, 5], 6) -> 3   (e.g. [1,2,3] [4] [5])
    min_test_rigs([1, 1, 1, 1], 4) -> 1
    min_test_rigs([5, 5, 5], 5) -> 3

    Target: O(n log n) time, O(1) space.
    """
    raise NotImplementedError


def find_version(tags: list[str], target: str) -> tuple[int, int]:
    """`tags` is a sorted (ascending, string order) list of release tags
    that may repeat. Return `(first, last)`: the first and last index
    where `target` occurs. Return `(-1, -1)` if `target` isn't present.

    find_version(["v1", "v2", "v2", "v2", "v3"], "v2") -> (1, 3)
    find_version(["v1", "v2", "v3"], "v9") -> (-1, -1)
    find_version([], "v1") -> (-1, -1)

    Target: O(log n) time, O(1) space.
    """
    raise NotImplementedError
