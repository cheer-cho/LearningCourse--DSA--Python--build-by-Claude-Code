# Scenario: three "sort by a custom rule" problems — the day-to-day use
# of sorting as a tool rather than an algorithm to implement.
# Concepts: custom comparators/keys, multi-key + stability, ranking by
# an external order list.
# Run: uv run pytest 09-sorting -k ex06


def largest_concat_number(nums: list[int]) -> str:
    """Arrange the non-negative integers in `nums` so that concatenating
    them (as decimal strings, in the chosen order) forms the LARGEST
    possible number. Return that number as a string.

    Compare two candidates `a`, `b` by which concatenation is bigger:
    `a+b` (a's digits then b's) vs `b+a`. Handle the all-zeros case
    (must return "0", not "000").

    largest_concat_number([3, 30, 34, 5, 9]) -> "9534330"
    largest_concat_number([0, 0]) -> "0"
    largest_concat_number([]) -> ""

    Target complexity: O(n log n) time (one comparator-driven sort),
    O(n) space.
    """
    raise NotImplementedError


def sort_by_frequency(nums: list[int]) -> list[int]:
    """Return a NEW list of `nums` ordered by how often each value
    appears, LEAST frequent first. Break ties between equally-frequent
    values by sorting those values DESCENDING (multi-key sort). Does
    not modify `nums`.

    sort_by_frequency([1, 1, 2, 2, 3]) -> [3, 2, 2, 1, 1]
    # 3 appears once (rarest); 1 and 2 both appear twice, tie broken by
    # value descending so 2's pair comes before 1's pair.
    sort_by_frequency([]) -> []

    Target complexity: O(n log n) time, O(n) space.
    """
    raise NotImplementedError


def relative_order(nums: list[int], order: list[int]) -> list[int]:
    """Return a NEW list of `nums` sorted by each value's position in
    `order` (an external ranking list, no duplicates). Values not
    present in `order` go at the end, sorted ascending among
    themselves. Does not modify `nums`.

    relative_order([2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6])
        -> [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]
    relative_order([], [2, 1]) -> []

    Target complexity: O(n log n) time, O(n + m) space where m =
    len(order).
    """
    raise NotImplementedError
